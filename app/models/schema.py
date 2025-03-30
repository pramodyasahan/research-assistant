from pydantic import BaseModel, Field

class QueryInput(BaseModel):
    question: str = Field(..., min_length=10, max_length=500, description="Educational research query")
