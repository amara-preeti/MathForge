from fastapi import APIRouter
from pydantic import BaseModel
import sympy as sp

router = APIRouter(prefix="/api/equations", tags=["equations"])

class EquationRequest(BaseModel):
    equation: str
    variable: str | None = None

@router.post("/solve")
def solve_equation(req: EquationRequest):
    try:
        # Split by '=' if present, otherwise assume it equals 0
        if '=' in req.equation:
            lhs_str, rhs_str = req.equation.split('=', 1)
            lhs = sp.sympify(lhs_str)
            rhs = sp.sympify(rhs_str)
            expr = lhs - rhs
        else:
            expr = sp.sympify(req.equation)
            
        if req.variable:
            var = sp.Symbol(req.variable)
        else:
            variables = list(expr.free_symbols)
            if not variables:
                return {"error": "No variables found"}
            var = variables[0]

        solutions = sp.solve(expr, var)
        
        return {
            "solutions": [str(s) for s in solutions],
            "latex_solutions": [sp.latex(s) for s in solutions]
        }
    except Exception as e:
        return {"error": str(e)}

class SystemEquationRequest(BaseModel):
    equations: list[str]
    variables: list[str] | None = None

@router.post("/solve_system")
def solve_system(req: SystemEquationRequest):
    try:
        parsed_eqs = []
        for eq_str in req.equations:
            if '=' in eq_str:
                lhs_str, rhs_str = eq_str.split('=', 1)
                parsed_eqs.append(sp.sympify(lhs_str) - sp.sympify(rhs_str))
            else:
                parsed_eqs.append(sp.sympify(eq_str))
                
        if req.variables:
            vars_to_solve = [sp.Symbol(v) for v in req.variables]
        else:
            vars_set = set()
            for eq in parsed_eqs:
                vars_set.update(eq.free_symbols)
            vars_to_solve = list(vars_set)
            
        solutions = sp.solve(parsed_eqs, vars_to_solve)
        
        # solutions can be a dict or a list of tuples depending on system type
        if isinstance(solutions, dict):
            return {
                "solutions": {str(k): str(v) for k, v in solutions.items()},
                "latex_solutions": {str(k): sp.latex(v) for k, v in solutions.items()}
            }
        elif isinstance(solutions, list):
            res = []
            for sol in solutions:
                res.append({str(var): str(val) for var, val in zip(vars_to_solve, sol)})
            return {"solutions_list": res}
        else:
            return {"solutions": str(solutions)}
            
    except Exception as e:
        return {"error": str(e)}
