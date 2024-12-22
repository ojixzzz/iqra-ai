import faster_whisper
from io import BytesIO
from fastapi import FastAPI, UploadFile, Form
from typing import Annotated
from pydantic import BaseModel
from transformers import pipeline
from contextlib import asynccontextmanager
from datetime import datetime
from config import CLASIFICATION_MODEL, RECOGNITION_MODEL


whisper_clasification = None
whisper_recognition = None


def loadModel():
    global whisper_clasification
    global whisper_recognition
    whisper_clasification = pipeline("audio-classification", CLASIFICATION_MODEL)
    whisper_recognition = faster_whisper.WhisperModel("../whisper-quran", device="cpu", compute_type="int8")


@asynccontextmanager
async def lifespan(app: FastAPI):
    loadModel()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "Keren kamu :D"}


@app.post("/hijaiyah")
def hijaiyah(secret: Annotated[str, Form()], file: UploadFile):
    global whisper_clasification
    audio = file.file.read()
    startdate = datetime.now()
    classifier = whisper_clasification(audio)
    return {"result": classifier, "time": (datetime.now() - startdate)}


@app.post("/quran")
def quran(secret: Annotated[str, Form()], file: UploadFile):
    global whisper_recognition
    audio = file.file.read()
    startdate = datetime.now()
    segments, info = whisper_recognition.transcribe(BytesIO(audio), beam_size=5)
    result = []
    for segment in segments:
        result.append({"start": segment.start, "end": segment.end, "text": segment.text})

    return {"result": result, "time": (datetime.now() - startdate)}
