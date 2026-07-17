from database import save_application, get_applications
import json
import markdown
from fastapi import FastAPI, Form, Request
from ai import analyze_profile
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home():
    return FileResponse("templates/index.html")


@app.get("/history")
def history(request: Request):

    database = get_applications()

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
    request: Request,
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

    save_application(data)
    analysis = analyze_profile(data)

analysis_html = markdown.markdown(
    analysis
)

    return templates.TemplateResponse(
    request=request,
    name="result.html",
    context={
        "request": request,
        "analysis": analysis_html
    }
)