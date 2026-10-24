# MathForge

**Offline Computer Algebra, Numerical Computing & Scientific Experimentation Platform.**

MathForge is a full-stack mathematical computing platform with 35+ specialized engines covering symbolic math, matrix operations, calculus, statistics, machine learning, signal processing, physics simulation, and more — all accessible via a modern React frontend and a FastAPI backend.

---

## Installation

### Prerequisites
- Python 3.11+
- Node.js 18+
- Git

### Backend
```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### Frontend
```bash
cd frontend
npm install
```

---

## Build

### Backend (production)
```bash
cd backend
pip install -r requirements.txt
python -m pytest tests/ -v
```

### Frontend (production bundle)
```bash
cd frontend
npm run build
# Output: frontend/dist/
```

### Docker (full stack)
```bash
docker-compose up --build
```

---

## Run

### Development mode

**Backend** (terminal 1):
```bash
cd backend
venv\Scripts\activate   # Windows
uvicorn app.main:app --reload --port 8000
```

**Frontend** (terminal 2):
```bash
cd frontend
npm run dev
# Open http://localhost:5173
```

### Using helper scripts (Windows)
```powershell
scripts\run_backend.ps1   # terminal 1
scripts\run_frontend.ps1  # terminal 2
```

---

## Testing

```bash
# Backend unit + integration tests
cd backend
pytest tests/ -v --cov=app --cov-report=term-missing

# Frontend tests
cd frontend
npm test
```

---

## Project Structure

```
MathForge/
├── backend/           # FastAPI application
│   └── app/           # Routers, engines, models
├── frontend/          # React + TypeScript UI
│   └── src/           # Components, pages, hooks
├── symbolic_engine/   # Symbolic math (CAS)
├── matrix_engine/     # Linear algebra
├── calculus_engine/   # Differentiation & integration
├── statistics_engine/ # Statistical analysis
├── ml_engine/         # Machine learning
├── physics_engine/    # Physics simulation
├── signal_engine/     # Signal processing
├── number_theory_engine/ # Number theory
├── geometry_engine/   # Computational geometry
├── graph_engine/      # Graph algorithms
├── optimization_engine/  # Optimization methods
├── tests/             # All test suites
├── docs/              # Documentation
└── scripts/           # Dev helper scripts
```

---

## API

The REST API is available at `http://localhost:8000/api`.

Interactive docs: `http://localhost:8000/docs` (Swagger UI)

Key endpoints:
- `POST /api/symbolic/simplify` — Simplify expressions
- `POST /api/matrix/decompose` — Matrix decompositions
- `POST /api/calculus/integrate` — Numerical/symbolic integration
- `POST /api/stats/test` — Hypothesis testing
- `POST /api/ml/train` — Train ML models

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
