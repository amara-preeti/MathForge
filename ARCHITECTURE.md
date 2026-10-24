# MathForge Architecture

MathForge is a modular, offline-first computer algebra and numerical computing platform. 
The system is divided into two primary parts:

1. **Backend**: A local API server written in Python with FastAPI, performing calculations via specialized mathematical engines.
2. **Frontend**: A React+Vite application providing the user interface, notebooks, and visualizations.

## Key Engines

- **Symbolic Engine**: Handles symbolic mathematics, algebra, equation solving (SymPy based).
- **Matrix Engine**: Handles linear algebra, matrices, vectors (NumPy based).
- **Calculus Engine**: Handles limits, derivatives, integrals.
- **Notebook Engine**: Handles local execution of markdown, math, and code cells.
- **Numerical Engine**: Handles root finding, interpolation, numerical ODE solutions (SciPy based).

## Technologies
- Python 3.11+ (FastAPI, SymPy, NumPy, SciPy)
- React, TypeScript, Tailwind CSS, Vite
- SQLite (Local DB)

## Data Storage
All data is stored locally in the `workspace/` and `data/` directories, with calculations tracked in a local SQLite database.
