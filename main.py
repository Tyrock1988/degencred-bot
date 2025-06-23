from fastapi import FastAPI
import uvicorn
from bot.handlers import setup_handlers
from config import load_config

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    setup_handlers()
    uvicorn.run(app, host="0.0.0.0", port=8080)
