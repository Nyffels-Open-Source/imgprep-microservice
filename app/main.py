from fastapi import FastAPI, UploadFile, File, Query
from fastapi.responses import Response
from app.processor import process_image
import io

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

@app.post("/optimize-jpeg", tags=["Optimization"])
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