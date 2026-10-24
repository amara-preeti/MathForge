#!/usr/bin/env python3
"""MathForge entry point."""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Main entry point for MathForge CLI."""
    import argparse
    parser = argparse.ArgumentParser(
        prog="mathforge",
        description="MathForge — Offline Computer Algebra & Scientific Computing Platform"
    )
    parser.add_argument("--version", action="version", version="MathForge 2.0.0")
    parser.add_argument("--server", action="store_true", help="Start the MathForge API server")
    parser.add_argument("--host", default="0.0.0.0", help="Server host (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8000, help="Server port (default: 8000)")
    parser.add_argument("--dev", action="store_true", help="Enable development/reload mode")
    parser.add_argument("--engine", help="Run a specific engine (symbolic, matrix, calculus, etc.)")
    parser.add_argument("--expr", help="Expression to evaluate")
    parser.add_argument("--format", choices=["text","latex","json"], default="text")

    args = parser.parse_args()

    if args.server:
        print(f"Starting MathForge API server on {args.host}:{args.port} ...")
        try:
            import uvicorn
            from backend.app.main import app
            uvicorn.run(
                "backend.app.main:app",
                host=args.host,
                port=args.port,
                reload=args.dev
            )
        except ImportError:
            print("ERROR: uvicorn not installed. Run: pip install -r backend/requirements.txt")
            sys.exit(1)
    elif args.engine and args.expr:
        print(f"[{args.engine}] Evaluating: {args.expr}")
        print(f"Result (format={args.format}): <computed>")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
