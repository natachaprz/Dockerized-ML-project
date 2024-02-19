FROM python:3.9-slim
COPY requirements.txt /client/requirements.txt
WORKDIR /client
RUN pip install -r requirements.txt
COPY app.py app.py
CMD ["streamlit", "run", "app.py", "--server.port", "8501"]
