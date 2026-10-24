from fastapi import APIRouter
from pydantic import BaseModel
import sympy as sp

router = APIRouter(prefix="/api/calculus", tags=["calculus"])

class CalculusRequest(BaseModel):
    expression: str
    variable: str | None = None
    value: str | None = None # For limits or eval
    degree: int | None = 5 # For Taylor series

@router.post("/limit")
def compute_limit(req: CalculusRequest):
    try:
        expr = sp.sympify(req.expression)
        var = sp.Symbol(req.variable) if req.variable else list(expr.free_symbols)[0]
        val = sp.sympify(req.value) if req.value else 0
        
        lim = sp.limit(expr, var, val)
        return {"result": str(lim), "latex": sp.latex(lim)}
    except Exception as e:
        return {"error": str(e)}

@router.post("/taylor")
def compute_taylor(req: CalculusRequest):
    try:
        expr = sp.sympify(req.expression)
        var = sp.Symbol(req.variable) if req.variable else list(expr.free_symbols)[0]
        val = sp.sympify(req.value) if req.value else 0
        n = req.degree if req.degree else 5
        
        series = sp.series(expr, var, val, n).removeO()
        return {"result": str(series), "latex": sp.latex(series)}
    except Exception as e:
        return {"error": str(e)}
