from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel, EmailStr
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

# Basic file-based storage for view counts (until Phase 3 DB integration)
VIEWS_FILE = "views.json"

def get_views():
    if not os.path.exists(VIEWS_FILE):
        return {}
    with open(VIEWS_FILE, "r") as f:
        return json.load(f)

def save_views(views):
    with open(VIEWS_FILE, "w") as f:
        json.dump(views, f)

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}

@app.post("/api/contact")
async def contact(form: ContactForm):
    # In a real scenario, this would send an email or save to a DB
    print(f"New contact message from {form.email}: {form.message}")
    return {"message": "Thank you! Your message has been received."}

@app.get("/api/projects/{slug}/view")
async def increment_view(slug: str):
    views = get_views()
    views[slug] = views.get(slug, 0) + 1
    save_views(views)
    return {"views": views[slug]}

@app.get("/api/projects/{slug}/views")
async def get_project_views(slug: str):
    views = get_views()
    return {"views": views.get(slug, 0)}
