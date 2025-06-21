# Base python Image
FROM python:3.11-slim

# Set a working directory
WORKDIR /app

# Install dependencies
COPY pyproject.toml poetry.lock* ./

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --only main

#Copy files
COPY src/ ./src/

#Making sure the model is also copied
COPY src/model/spam_model.joblib ./src/model/spam_model.joblib

#Expose fast API port
EXPOSE 8000

#Start API
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port","8000"]