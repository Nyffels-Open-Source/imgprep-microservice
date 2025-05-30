# 🧼 imgprep-microservice

**Image Preprocessing Service for OCR Pipelines**  
Open source microservice developed by [Nyffels BV](https://nyffels.be)  
Contact: chesney@nyffels.be

GitHub Repository: [https://github.com/Nyffels-Open-Source/imgprep-microservice](https://github.com/Nyffels-Open-Source/imgprep-microservice)  
DockerHub: [https://hub.docker.com/repository/docker/nyffels/imgprep-microservice](https://hub.docker.com/repository/docker/nyffels/imgprep-microservice)  
Docker Image: `nyffels/imgprep-microservice:latest`

---

## 🔍 Overview

`imgprep-microservice` is a REST-based image preprocessing microservice designed to clean and optimize image input (JPEGs) before OCR.  
It works for single images as well as bulk ZIP files, and is ideal for automation pipelines or standalone use.

---

## 📦 Features

- Apply configurable optimizations to images:
  - Grayscale conversion
  - Denoising
  - Contrast enhancement
  - Deskewing
  - Rotation (auto/manual)
- Single or batch input (via ZIP)
- Optimized output for OCR engines like Tesseract, EasyOCR, Google Vision
- RESTful API via FastAPI
- Docker-ready

---

## ⚠️ Security Notice

> This service has **no built-in authentication or authorization**.  
> It is intended to run inside a private network or behind a secure gateway.

---

## 🚀 Quickstart (Docker)

```bash
docker pull nyffels/imgprep-microservice:latest

docker run -d \
  -p 8000:8000 \
  --name imgprep \
  nyffels/imgprep-microservice:latest
```

Access Swagger UI at: `http://localhost:8000/docs`

---

## 🔧 API Usage

### `POST /optimize-jpeg`

Optimizes a single image.

#### Request
- **Type:** `multipart/form-data`
- **Field:** `file` (JPEG image)
- **Query params:**
  - `grayscale` (bool)
  - `denoise` (bool)
  - `contrast` (bool)
  - `deskew` (bool)
  - `rotate` (str: "auto", "none", "0", "90", "180", "270")

#### Response
- Optimized JPEG image (`image/jpeg`)

---

### `POST /optimize-zip`

Processes a ZIP file containing one or more JPEGs.

#### Request
- **Type:** `multipart/form-data`
- **Field:** `file` (ZIP archive containing `.jpg` or `.jpeg` images)
- **Query params:** same as `/optimize-jpeg`

#### Response
- ZIP archive with optimized JPEGs (`application/zip`)

---

## 🛠 Tech Stack

- Python 3.11
- FastAPI
- OpenCV + Pillow
- pytesseract
- Docker

---

## 📂 Folder Structure

```
imgprep-microservice/
├── app/
│   ├── main.py            # FastAPI endpoints
│   ├── processor.py       # Image optimization pipeline
│   └── utils.py           # Operations (grayscale, denoise, deskew, etc.)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome!

Please create an issue first to discuss ideas or problems before submitting a pull request.

Let's build a clean OCR future together 💪

---

## 📄 License

MIT License © 2025 Nyffels BV  
See [`LICENSE`](./LICENSE) for full terms.
