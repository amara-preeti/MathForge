from fastapi import APIRouter
from pydantic import BaseModel
import sympy as sp
import numpy as np

router = APIRouter(prefix="/api/plotting", tags=["plotting"])

class PlotRequest(BaseModel):
    expression: str
    variable: str = 'x'
    x_min: float = -10.0
    x_max: float = 10.0
    points: int = 200

@router.post("/generate_2d")
def generate_2d_plot(req: PlotRequest):
    try:
        expr = sp.sympify(req.expression)
        var = sp.Symbol(req.variable)
        
        # Use lambdify to create a fast numpy-compatible function
        f = sp.lambdify(var, expr, modules=['numpy', 'math'])
        
        # Generate x values
        x_vals = np.linspace(req.x_min, req.x_max, req.points)
        
        # Evaluate y values
        y_vals = []
        for x in x_vals:
            try:
                val = f(x)
                if np.iscomplex(val) or np.isnan(val) or np.isinf(val):
                    y_vals.append(None)
                else:
                    y_vals.append(float(val))
            except:
                y_vals.append(None)
                
        return {
            "x": x_vals.tolist(),
            "y": y_vals
        }
    except Exception as e:
        return {"error": str(e)}
