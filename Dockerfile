# User Directory Backend API Docker file
FROM python:3.9.21-slim-bullseye
ENV app_name="User Directory Backend API"
RUN addgroup appgroup
RUN useradd -G appgroup appuser
WORKDIR /user-dir-api
COPY *.py .
COPY requirements.txt .
RUN python3 -m venv env
RUN pip install -U python-dotenv
RUN pip install -r requirements.txt
USER appuser
EXPOSE 9090
CMD uvicorn main:app --port 9090 --host 0.0.0.0