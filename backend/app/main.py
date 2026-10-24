from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import (
    symbolic, equations, matrix, calculus,
    notebook, plotting, projects,
    number_theory, physics
)
from app.core.database import engine, Base
from app.models import Project, Notebook

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MathForge API",
    description="Local backend for MathForge – Offline Computer Algebra, Numerical Computing & Scientific Experimentation Platform",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Core Math Engines ──────────────────────────────────────────
app.include_router(symbolic.router)
app.include_router(equations.router)
app.include_router(matrix.router)
app.include_router(calculus.router)
app.include_router(notebook.router)
app.include_router(plotting.router)
app.include_router(projects.router)

# ── New Engines ────────────────────────────────────────────────
app.include_router(number_theory.router)
app.include_router(physics.router)


@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Welcome to MathForge API v2.0",
        "engines": [
            "symbolic", "equations", "matrix", "calculus",
            "notebook", "plotting", "projects",
            "number_theory", "physics"
        ],
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/api/status", tags=["Root"])
def get_status():
    return {
        "status": "running",
        "version": "2.0.0",
        "engines": 9,
        "features": "fully operational"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
