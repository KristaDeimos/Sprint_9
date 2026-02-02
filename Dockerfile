# Используем образ Selenium Node с Chrome
FROM selenium/node-chrome:latest

# Устанавливаем Python
USER root

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "pytest", "-q", "--alluredir=allure-results"]
