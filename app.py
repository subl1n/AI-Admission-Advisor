from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def home():
    return FileResponse("templates/index.html")

@app.get("/history")
def history():
    return FileResponse("templates/history.html")


@app.get("/about")
def about():
    return FileResponse("templates/about.html")