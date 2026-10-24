from fastapi import APIRouter
from pydantic import BaseModel
import sympy as sp

router = APIRouter(prefix="/api/symbolic", tags=["symbolic"])

class ExpressionRequest(BaseModel):
    expression: str
    variable: str | None = None

@router.post("/simplify")
def simplify_expression(req: ExpressionRequest):
    try:
        expr = sp.sympify(req.expression)
        simplified = sp.simplify(expr)
        return {"result": str(simplified), "latex": sp.latex(simplified)}
    except Exception as e:
        return {"error": str(e)}

@router.post("/expand")
def expand_expression(req: ExpressionRequest):
    try:
        expr = sp.sympify(req.expression)
        expanded = sp.expand(expr)
        return {"result": str(expanded), "latex": sp.latex(expanded)}
    except Exception as e:
        return {"error": str(e)}

@router.post("/factor")
def factor_expression(req: ExpressionRequest):
    try:
        expr = sp.sympify(req.expression)
        factored = sp.factor(expr)
        return {"result": str(factored), "latex": sp.latex(factored)}
    except Exception as e:
        return {"error": str(e)}

@router.post("/differentiate")
def differentiate_expression(req: ExpressionRequest):
    try:
        expr = sp.sympify(req.expression)
        if req.variable:
            var = sp.Symbol(req.variable)
        else:
            variables = list(expr.free_symbols)
            if not variables:
                return {"result": "0", "latex": "0"}
            var = variables[0]
        
        diff_expr = sp.diff(expr, var)
        return {"result": str(diff_expr), "latex": sp.latex(diff_expr)}
    except Exception as e:
        return {"error": str(e)}

@router.post("/integrate")
def integrate_expression(req: ExpressionRequest):
    try:
        expr = sp.sympify(req.expression)
        if req.variable:
            var = sp.Symbol(req.variable)
        else:
            variables = list(expr.free_symbols)
            if not variables:
                return {"result": f"{req.expression} * x", "latex": f"{sp.latex(expr)} \\cdot x"}
            var = variables[0]
            
        int_expr = sp.integrate(expr, var)
        return {"result": str(int_expr), "latex": sp.latex(int_expr)}
    except Exception as e:
        return {"error": str(e)}
