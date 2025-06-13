FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Install chromium and chromedriver
RUN apt update && apt install -y chromium chromium-driver

EXPOSE 5000

CMD ["python", "main.py"]
