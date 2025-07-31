from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/ping")
async def ping():
    return PlainTextResponse("pong", status_code=200)


@app.get("/home", response_class=HTMLResponse)
async def home():
    return HTMLResponse(content="<h1>Welcome home!</h1>", status_code=200)


