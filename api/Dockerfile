FROM python:3.11-slim

WORKDIR /app

COPY /requirments.txt .

RUN pip install -U pip

RUN pip install -r requirments.txt

COPY . .

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]