# coding: utf-8

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from predict import FineTuningNet
from pydantic import BaseModel


app = FastAPI()

# モデルの定義
net = FineTuningNet()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class PerfumeImg(BaseModel):
    base_64: str


@app.post("/perfume/")
def predict_perfume(img: PerfumeImg):
    return net.predcit_result(img.base_64)
