import json
from fastapi import FastAPI, Form
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