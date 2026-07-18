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

@app.get("/application/{id}")
def application(id: int, request: Request):

    database = get_applications()

    application = database[id]

    application["analysis"] = markdown.markdown(application["analysis"])

    return templates.TemplateResponse(
        request=request,
        name="application.html",
        context={
            "application": application
        }
    )


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

    analysis = analyze_profile(data)
    
    data["analysis"] = analysis
    
    save_application(data)

    analysis_html = markdown.markdown(analysis)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "request": request,
            "analysis": analysis_html
        }
    )