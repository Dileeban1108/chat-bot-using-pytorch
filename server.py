from fastapi import FastAPI
from pydantic import BaseModel
from chat import get_response as get_intent_response, bot_name
from openAI import get_response_from_gpt

app = FastAPI(title=f"ChatBot - {bot_name}")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    msg = req.message.strip()
    response = get_intent_response(msg)
    if response in ["I do not understand...😰"]:
        response = get_response_from_gpt(msg)
    return {"bot_name": bot_name, "response": response}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)