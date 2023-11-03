FROM python:3.9
WORKDIR /app
COPY marching_doubler.py .
ENTRYPOINT  ["python","./marching_doubler.py"]
