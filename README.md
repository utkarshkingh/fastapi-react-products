# fastapi-react-products

A product catalog app. A FastAPI backend serves product data. A React frontend shows and edits it.

## Overview

| Item     | Detail                                |
| -------- | ------------------------------------- |
| Backend  | FastAPI, Pydantic                     |
| Frontend | React 18, Axios                       |
| Data     | One in-memory product (no database)   |
| Status   | Learning project. Backend incomplete. |

## Contents

| Path                | Purpose                                          |
| ------------------- | ------------------------------------------------ |
| `main.py`           | FastAPI app. Has one endpoint: `GET /`.          |
| `models.py`         | `Product` model: id, name, description, price, quantity. |
| `frontend/`         | React app. Lists, filters, sorts, adds, edits, and deletes products. |

## Run

Backend:

```bash
pip install "fastapi[standard]"
fastapi dev main.py
```

The API starts on `http://localhost:8000`.

Frontend:

```bash
cd frontend
npm install
npm start
```

The app starts on `http://localhost:3000`.

## Known gap

The frontend calls `/products/` with GET, POST, PUT, and DELETE. The backend does not have these endpoints yet. The frontend shows "Failed to fetch products" until they exist.
