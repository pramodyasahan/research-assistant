from fastapi import FastAPI, HTTPException, Body

app = FastAPI()


@app.post('/question')
async def ask_question(payload: str = Body(min_length=10, max_length=100)):
    if not payload:
        raise HTTPException("Need to ask a question")

    return payload
