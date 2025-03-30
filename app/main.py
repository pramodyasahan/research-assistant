from fastapi import FastAPI, HTTPException, Body
from app.models.schema import QueryInput

app = FastAPI()


@app.post('/question')
async def ask_question(payload: QueryInput):
    if not payload:
        raise HTTPException("Need to ask a question")

    return payload
