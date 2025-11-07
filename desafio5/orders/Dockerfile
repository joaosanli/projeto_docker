FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir flask
COPY orders.py .
EXPOSE 5000
CMD ["python", "orders.py"]
