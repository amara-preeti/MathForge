from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import numpy as np

router = APIRouter(prefix="/api/matrix", tags=["matrix"])

class MatrixRequest(BaseModel):
    matrix: list[list[float]]

class MatrixBinaryRequest(BaseModel):
    matrix_a: list[list[float]]
    matrix_b: list[list[float]]
    operation: str

def format_matrix(m):
    if isinstance(m, np.ndarray):
        return m.tolist()
    return m

@router.post("/properties")
def matrix_properties(req: MatrixRequest):
    try:
        mat = np.array(req.matrix)
        det = np.linalg.det(mat) if mat.shape[0] == mat.shape[1] else None
        rank = np.linalg.matrix_rank(mat)
        trace = np.trace(mat) if mat.shape[0] == mat.shape[1] else None
        
        try:
            inv = np.linalg.inv(mat).tolist() if det and det != 0 else None
        except:
            inv = None

        return {
            "determinant": det,
            "rank": int(rank),
            "trace": trace,
            "inverse": inv,
            "shape": mat.shape
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/eigen")
def matrix_eigen(req: MatrixRequest):
    try:
        mat = np.array(req.matrix)
        if mat.shape[0] != mat.shape[1]:
            raise ValueError("Matrix must be square for eigenvalues")
            
        eigenvalues, eigenvectors = np.linalg.eig(mat)
        
        # Format complex numbers if necessary
        return {
            "eigenvalues": [str(v) for v in eigenvalues],
            "eigenvectors": [[str(v) for v in row] for row in eigenvectors.T]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/operate")
def matrix_operate(req: MatrixBinaryRequest):
    try:
        A = np.array(req.matrix_a)
        B = np.array(req.matrix_b)
        op = req.operation.lower()
        
        if op == "add":
            res = A + B
        elif op == "subtract":
            res = A - B
        elif op == "multiply":
            res = np.matmul(A, B)
        else:
            raise ValueError("Invalid operation")
            
        return {"result": format_matrix(res)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
