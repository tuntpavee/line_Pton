FROM python:3.10-slim
WORKDIR /app
# If requirements.txt lives in project root, build from root; otherwise put it in backend/
COPY ../requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
