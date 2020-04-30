# coding: utf-8
from torchvision.models import resnet18
from io import BytesIO
import base64

# モデル学習
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
import pytorch_lightning as pl
from PIL import Image

import cv2
import numpy as np


def encode_base64(pil_img):
    base_64 = pil_img.copy()
    buffered = BytesIO()
    base_64.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue())


def round_probability(_prob):
    return round(_prob * 100, 2)


def transform(img):
    _transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return _transform(img)


class FineTuningNet(pl.LightningModule):

    def __init__(self):
        super().__init__()

        self.conv = resnet18(pretrained=True)
        self.fc1 = nn.Linear(1000, 100)
        self.fc2 = nn.Linear(100, 3)

        # 学習済みのパラメータを固定
        for param in self.conv.parameters():
            param.requires_grad = False

        self.eval()
        self.freeze()
        self.load_state_dict(
            torch.load(
                './models/model_0429.pt',
                map_location='cpu'))

        # open cv
        self.face_cascade = cv2.CascadeClassifier(
            './opencv/haarcascade_frontalface_alt.xml')

    def forward(self, x):
        x = self.conv(x)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return x

    def predict_img(self, _img):
        base64_img = encode_base64(_img)

        _img = transform(_img).unsqueeze(0)
        # 予測
        y = self(_img)

        probability = F.softmax(y, dim=1)[0].tolist()
        probability = list(map(round_probability, probability))

        return {
            'かしゆか': probability[0],
            'あーちゃん': probability[1],
            'のっち': probability[2],
            'base64': base64_img
        }

    def predcit_result(self, _base64_img):

        _base64_img = Image.open(BytesIO(base64.b64decode(_base64_img)))
        origin_image = np.array(_base64_img, dtype=np.uint8)
        origin_image = cv2.cvtColor(origin_image, cv2.COLOR_RGB2BGR)
        base_image = origin_image.copy()
        faces = self.face_cascade.detectMultiScale(origin_image, 1.1, 3)

        results = []

        if len(faces) > 0:
            print('start')
            for face in faces:
                x, y, w, h = face
                face_img = cv2.cvtColor(
                    base_image[y:y + h, x:x + w], cv2.COLOR_BGR2RGB)
                face_img = Image.fromarray(face_img)
                results.append(self.predict_img(face_img))
                origin_image = cv2.rectangle(
                    origin_image, (x, y), (x + w, y + h), (0, 0, 255), 10)

            origin_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2RGB)
            return {
                'results': results,
                'face_img': encode_base64(Image.fromarray(origin_image))
            }
        else:
            print('NoFace')
            return {
                'results': False,
            }
