import sys
import io
import contextlib
import traceback
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/notebook", tags=["notebook"])

class CodeCellRequest(BaseModel):
    code: str
    
# Shared execution context for the notebook session
# Note: In a production app, this would be tied to a session ID.
notebook_globals = {}

@router.post("/execute")
def execute_cell(req: CodeCellRequest):
    # Capture stdout and stderr
    stdout_buffer = io.StringIO()
    stderr_buffer = io.StringIO()
    
    result = None
    error = None
    
    # Try compiling first to catch syntax errors
    try:
        compiled_code = compile(req.code, '<string>', 'exec')
    except Exception:
        error = traceback.format_exc()
        return {"stdout": "", "stderr": error, "result": None}

    with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
        try:
            # We want to support returning the last expression like jupyter does
            # We will try to evaluate the last statement if it's an expression
            import ast
            parsed_ast = ast.parse(req.code)
            
            if len(parsed_ast.body) > 0 and isinstance(parsed_ast.body[-1], ast.Expr):
                # Separate the last expression
                last_expr = parsed_ast.body.pop()
                
                # Execute everything except the last expression
                exec(compile(parsed_ast, '<string>', 'exec'), notebook_globals)
                
                # Evaluate the last expression
                expr_code = compile(ast.Expression(last_expr.value), '<string>', 'eval')
                result = eval(expr_code, notebook_globals)
            else:
                # Execute all as statements
                exec(compiled_code, notebook_globals)
                
        except Exception:
            error = traceback.format_exc()
            
    stdout_str = stdout_buffer.getvalue()
    stderr_str = stderr_buffer.getvalue()
    
    return {
        "stdout": stdout_str,
        "stderr": stderr_str + (error if error else ""),
        "result": str(result) if result is not None else None
    }

@router.post("/reset")
def reset_session():
    global notebook_globals
    notebook_globals = {}
    return {"message": "Session reset"}
