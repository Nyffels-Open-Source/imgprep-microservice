from fastapi import FastAPI, UploadFile, File, Query
from fastapi.responses import Response
from app.processor import process_image
import io
import zipfile
from fastapi.responses import StreamingResponse

app = FastAPI(
    title="imgprep-microservice",
    version="1.0",
    description="""
    A lightweight microservice for preprocessing images before OCR.

    This service applies grayscale, denoising, contrast enhancement, deskewing, and rotation
    to optimize image quality for OCR engines like Tesseract, EasyOCR, and Google Vision.

    Use the /optimize-jpeg endpoint to process one JPEG image at a time.
    """
)

@app.get("/health", tags=["Health"])
def health():
    """
    Check if the service is running.

    Returns a simple JSON status message.
    """
    return {"status": "ok"}

@app.post("/optimize-jpeg", tags=["OptimizationJpeg"])
async def optimize_jpeg(
    file: UploadFile = File(..., description="Image to optimize for OCR (JPEG, PNG, BMP, TIFF, WEBP)"),
    grayscale: bool = Query(False, description="Convert image to grayscale (recommended for OCR)"),
    denoise: bool = Query(False, description="Apply denoising filter to reduce background noise"),
    contrast: bool = Query(False, description="Enhance image contrast via histogram equalization"),
    deskew: bool = Query(False, description="Try to automatically straighten tilted images"),
    rotate: str = Query("none", description="Rotate the image. Options: none, auto, 0, 90, 180, 270")
):
    """
    Optimize a JPEG image for OCR usage.

    Apply a configurable sequence of image enhancements such as grayscale conversion,
    denoising, contrast adjustment, deskewing, and rotation.

    Returns the optimized image as JPEG.
    """
    img_bytes = await file.read()
    optimized = process_image(img_bytes, grayscale, denoise, contrast, deskew, rotate)
    return Response(content=optimized, media_type="image/jpeg")

@app.post("/optimize-zip", tags=["OptimizationZip"])
async def optimize_zip(
    file: UploadFile = File(..., description="ZIP file with JPEG images"),
    grayscale: bool = Query(False),
    denoise: bool = Query(False),
    contrast: bool = Query(False),
    deskew: bool = Query(False),
    rotate: str = Query("none")
):
    zip_data = await file.read()
    zip_input = zipfile.ZipFile(io.BytesIO(zip_data))

    output_io = io.BytesIO()
    with zipfile.ZipFile(output_io, mode="w", compression=zipfile.ZIP_DEFLATED) as zip_out:
        for name in zip_input.namelist():
            if name.lower().endswith(".jpg") or name.lower().endswith(".jpeg"):
                with zip_input.open(name) as img_file:
                    img_bytes = img_file.read()
                    processed = process_image(img_bytes, grayscale, denoise, contrast, deskew, rotate)
                    zip_out.writestr(name, processed)

    output_io.seek(0)
    return StreamingResponse(output_io, media_type="application/zip", headers={
        "Content-Disposition": "attachment; filename=optimized_images.zip"
    })
