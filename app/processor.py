import cv2
import numpy as np
from app.utils import apply_grayscale, apply_denoise, apply_contrast, apply_deskew, apply_rotation
import io
from PIL import Image

def process_image(img_bytes, grayscale, denoise, contrast, deskew, rotate):
    image = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    img = np.array(image)

    if grayscale:
        img = apply_grayscale(img)
    if denoise:
        img = apply_denoise(img)
    if contrast:
        img = apply_contrast(img)
    if deskew:
        img = apply_deskew(img)
    if rotate and rotate.lower() != "none":
        img = apply_rotation(img, rotate)

    _, jpeg = cv2.imencode(".jpg", img)
    return jpeg.tobytes()