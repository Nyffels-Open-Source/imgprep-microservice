# 🧼 imgprep-microservice

**Image Preprocessing Service for OCR Pipelines**  
Open source microservice developed by [Nyffels BV](https://nyffels.be)  
Contact: chesney@nyffels.be

GitHub Repository: [https://github.com/Nyffels-Open-Source/imgprep-microservice](https://github.com/Nyffels-Open-Source/imgprep-microservice)  
DockerHub: [https://hub.docker.com/repository/docker/nyffels/imgprep-microservice](https://hub.docker.com/repository/docker/nyffels/imgprep-microservice)  
Docker Image: `nyffels/imgprep-microservice:latest`

---

## 🔍 Overview

`imgprep-microservice` is a REST-based image preprocessing microservice designed to clean and optimize JPEG input before OCR (Optical Character Recognition). It is built for automation pipelines but also works standalone.

---

## 📦 Features

- Apply configurable optimizations to images:
  - Grayscale conversion
  - Denoising
  - Contrast enhancement
  - Deskewing
  - Rotation (auto/manual)
- Optimized output for OCR engines like Tesseract, EasyOCR, Google Vision etc.
- RESTful API via FastAPI
- Docker-ready

---

## ⚠️ Security Notice

> This service has **no built-in authentication or authorization**.
> It is meant to run inside a private network or behind a secured gateway.

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
Optimizes a JPEG image for OCR using optional parameters.

#### Request
- **Type:** `multipart/form-data`
- **Field:** `file` (JPEG image)
- **Optional query/body params:**
  - `grayscale` (bool)
  - `denoise` (bool)
  - `contrast` (bool)
  - `deskew` (bool)
  - `rotate` ("auto" or angle: 0, 90, 180, 270)

#### Response
- Optimized JPEG image (`image/jpeg`)

---

## 🛠 Tech Stack

- Python 3.11
- FastAPI
- OpenCV + Pillow
- Docker

---

## 📂 Folder Structure

```
imgprep-microservice/
├── app/
│   ├── main.py            # FastAPI app
│   ├── processor.py       # Image optimization pipeline
│   └── utils.py           # Individual operations (deskew, contrast, etc.)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome!

However, **please create an issue first** to propose an improvement, bugfix or new feature before opening a pull request.

Let's build a clean OCR future together 💪

---

## 📄 License

MIT License © 2025 Nyffels BV

See [`LICENSE`](./LICENSE) for full terms.
