from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r") as file:
        return file.read()

@app.get("/greet", response_class=HTMLResponse)
def greet(name: str):
    return f"<h1>Hello, {name}!</h1>"
