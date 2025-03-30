from fastapi import FastAPI, HTTPException, status
from models.schema import QueryInput
from utils.filters import is_valid_question

app = FastAPI()


@app.post('/question')
async def ask_question(payload: QueryInput):
    if not is_valid_question(payload.question):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Only educational research query are accepted")

    return payload.question
