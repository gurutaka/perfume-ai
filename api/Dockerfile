FROM python:3.6


RUN pip install fastapi uvicorn
RUN pip install torch torchvision pytorch-lightning
RUN pip install numpy

RUN apt-get update -y && apt-get install -y libopencv-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install  opencv-python

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port ${PORT}