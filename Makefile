# MathForge Makefile
# Provides standard build, run, test, and deploy targets

.PHONY: all install build run dev test lint clean docker-build docker-run help

PYTHON := python
PIP    := pip
NPM    := npm
PORT   := 8000
HOST   := 0.0.0.0

all: install

## ─── Installation ─────────────────────────────────────────────────────────────

install: install-backend install-frontend  ## Install all dependencies
	@echo "MathForge dependencies installed."

install-backend:  ## Install Python backend dependencies
	cd backend && $(PIP) install -r requirements.txt

install-frontend:  ## Install Node.js frontend dependencies
	cd frontend && $(NPM) install

## ─── Build ────────────────────────────────────────────────────────────────────

build: build-backend build-frontend  ## Build all components

build-backend:  ## No-op for Python backend (interpreted)
	@echo "Backend ready (Python — no build step required)"

build-frontend:  ## Build frontend production bundle
	cd frontend && $(NPM) run build

## ─── Run ──────────────────────────────────────────────────────────────────────

run: run-backend  ## Start backend API server

run-backend:  ## Start FastAPI backend
	$(PYTHON) main.py --server --host $(HOST) --port $(PORT)

run-frontend:  ## Start frontend dev server
	cd frontend && $(NPM) run dev

dev:  ## Start backend in dev/reload mode
	$(PYTHON) main.py --server --dev --host $(HOST) --port $(PORT)

## ─── Testing ──────────────────────────────────────────────────────────────────

test: test-backend test-frontend  ## Run all tests

test-backend:  ## Run Python tests with pytest
	$(PYTHON) -m pytest tests/ -v --tb=short

test-coverage:  ## Run tests with coverage report
	$(PYTHON) -m pytest tests/ -v --cov=. --cov-report=term-missing --cov-report=xml

test-frontend:  ## Run frontend Jest tests
	cd frontend && $(NPM) test -- --watchAll=false

lint:  ## Run linters (ruff + mypy + eslint)
	ruff check . --exclude=frontend,venv,node_modules
	cd frontend && $(NPM) run lint

## ─── Docker ───────────────────────────────────────────────────────────────────

docker-build:  ## Build Docker images
	docker-compose build

docker-run:  ## Start all services with Docker Compose
	docker-compose up

docker-stop:  ## Stop Docker services
	docker-compose down

## ─── Utility ──────────────────────────────────────────────────────────────────

clean:  ## Remove build artifacts and caches
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	rm -rf frontend/dist frontend/.next .pytest_cache .mypy_cache coverage.xml

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
