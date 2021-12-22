# Pull the FastAPI image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Work Directory
WORKDIR /app

# Install Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy Project
COPY . .
