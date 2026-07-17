import json
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home():
    return FileResponse("templates/index.html")


@app.get("/history")
def history(request: Request):

    with open("db.json", "r") as file:
        database = json.load(file)

    return templates.TemplateResponse(
    request=request,
    name="history.html",
    context={
        "applications": database
    }
)


@app.get("/about")
def about():
    return FileResponse("templates/about.html")


@app.post("/analyze")
def analyze(
    gpa: str = Form(...),
    ielts: str = Form(...),
    sat: str = Form(...),
    portfolio: str = Form(...),
    universities: str = Form(...)
):
    data = {
        "gpa": gpa,
        "ielts": ielts,
        "sat": sat,
        "portfolio": portfolio,
        "universities": universities
    }

    with open("db.json", "r") as file:
        database = json.load(file)

    database.append(data)

    with open("db.json", "w") as file:
        json.dump(database, file, indent=4)

    return {
        "message": "Saved successfully!"
    }