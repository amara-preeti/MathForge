from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import json

from app.core.database import get_db
from app.models import Project, Notebook

router = APIRouter(prefix="/api/projects", tags=["projects"])

class ProjectCreate(BaseModel):
    name: str
    description: str | None = None

class NotebookCreate(BaseModel):
    title: str
    cells_json: str = "[]"

@router.get("/")
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()

@router.post("/")
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = Project(name=project.name, description=project.description)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get("/{project_id}/notebooks")
def get_notebooks(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project.notebooks

@router.post("/{project_id}/notebooks")
def create_notebook(project_id: int, notebook: NotebookCreate, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    db_notebook = Notebook(title=notebook.title, cells_json=notebook.cells_json, project_id=project_id)
    db.add(db_notebook)
    db.commit()
    db.refresh(db_notebook)
    return db_notebook

@router.put("/notebooks/{notebook_id}")
def update_notebook(notebook_id: int, notebook: NotebookCreate, db: Session = Depends(get_db)):
    db_notebook = db.query(Notebook).filter(Notebook.id == notebook_id).first()
    if not db_notebook:
        raise HTTPException(status_code=404, detail="Notebook not found")
    
    db_notebook.title = notebook.title
    db_notebook.cells_json = notebook.cells_json
    db.commit()
    db.refresh(db_notebook)
    return db_notebook
