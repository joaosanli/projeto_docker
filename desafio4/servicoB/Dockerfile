FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir flask requests
COPY server.py .
EXPOSE 5000
CMD ["python", "server.py"]
