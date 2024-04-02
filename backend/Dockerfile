FROM python:3.9

WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

# Clone mkey repository
RUN git clone https://github.com/zoogie/mkey.git /mkey

RUN pip install --no-cache-dir --upgrade pip
RUN pip install pycryptodome

CMD ["python", "backend.py"]
