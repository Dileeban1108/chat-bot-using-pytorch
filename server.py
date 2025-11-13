from fastapi import FastAPI
from pydantic import BaseModel
from chat import get_response as get_intent_response, bot_name
from openAI import get_response_from_gpt
import uvicorn

app = FastAPI(title=f"ChatBot - {bot_name}")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    message = req.message.strip()

    if not message:
        return {"response": "Please enter a message."}

    # Step 1: Try local intent-based response
    response = get_intent_response(message)

    # Step 2: Fallback to GPT if needed
    if response in ["I do not understand...😰"]:
        response = get_response_from_gpt(message)

    return {"bot_name": bot_name, "response": response}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
