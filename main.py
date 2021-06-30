from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from use_case import get_question
from react_presenter import format_question

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/question")
def get_next_question():
    message = get_question()
    formatted_message = format_question(message)
    return {"message": formatted_message}
