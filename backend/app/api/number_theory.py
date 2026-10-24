"""FastAPI router for Number Theory Engine."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Any
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from number_theory_engine.engine import NumberTheoryEngine

router = APIRouter(prefix="/number-theory", tags=["Number Theory"])
engine = NumberTheoryEngine()


class IntRequest(BaseModel):
    n: int

class TwoIntRequest(BaseModel):
    a: int
    b: int

class ThreeIntRequest(BaseModel):
    a: int
    b: int
    c: int

class ModExpRequest(BaseModel):
    base: int
    exp: int
    mod: int

class PrimeRangeRequest(BaseModel):
    start: int
    end: int

class CRTRequest(BaseModel):
    remainders: List[int]
    moduli: List[int]

class LinearCongruenceRequest(BaseModel):
    a: int
    b: int
    m: int

class ContinuedFractionRequest(BaseModel):
    n: float
    max_terms: int = 20

class DiscreteLogRequest(BaseModel):
    a: int
    b: int
    p: int

class FermatRequest(BaseModel):
    n: int

class MersenneRequest(BaseModel):
    p: int


@router.post("/is-prime")
def is_prime(req: IntRequest):
    try:
        return engine.is_prime(req.n)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/next-prime")
def next_prime(req: IntRequest):
    try:
        return engine.next_prime(req.n)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/prev-prime")
def prev_prime(req: IntRequest):
    try:
        return engine.prev_prime(req.n)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/nth-prime")
def nth_prime(req: IntRequest):
    try:
        return engine.nth_prime(req.n)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/prime-range")
def prime_range(req: PrimeRangeRequest):
    try:
        return engine.prime_range(req.start, req.end)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/prime-counting")
def prime_counting(req: IntRequest):
    try:
        return engine.prime_counting(req.n)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/prime-factorization")
def prime_factorization(req: IntRequest):
    try:
        return engine.prime_factorization(req.n)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/sieve")
def sieve(req: IntRequest):
    try:
        return engine.sieve_of_eratosthenes(req.n)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/gcd")
def compute_gcd(req: TwoIntRequest):
    try:
        return engine.compute_gcd(req.a, req.b)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/lcm")
def compute_lcm(req: TwoIntRequest):
    try:
        return engine.compute_lcm(req.a, req.b)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/extended-gcd")
def extended_gcd(req: TwoIntRequest):
    try:
        return engine.extended_gcd(req.a, req.b)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/modular-exp")
def modular_exp(req: ModExpRequest):
    try:
        return engine.modular_exponentiation(req.base, req.exp, req.mod)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/modular-inverse")
def modular_inverse(req: TwoIntRequest):
    try:
        return engine.modular_inverse(req.a, req.b)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/linear-congruence")
def linear_congruence(req: LinearCongruenceRequest):
    try:
        return engine.solve_linear_congruence(req.a, req.b, req.m)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/crt")
def crt(req: CRTRequest):
    try:
        return engine.chinese_remainder_theorem(req.remainders, req.moduli)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/euler-totient")
def euler_totient(req: IntRequest):
    try:
        return engine.euler_totient(req.n)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/mobius")
def mobius(req: IntRequest):
    try:
        return engine.mobius_function(req.n)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/divisors")
def divisors(req: IntRequest):
    try:
        return engine.divisors_of(req.n)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/continued-fraction")
def continued_fraction(req: ContinuedFractionRequest):
    try:
        return engine.continued_fraction_expansion(req.n, req.max_terms)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/discrete-log")
def discrete_log(req: DiscreteLogRequest):
    try:
        return engine.discrete_logarithm(req.a, req.b, req.p)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/number-classification")
def number_classification(req: IntRequest):
    try:
        return engine.number_classification(req.n)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/fermat-number")
def fermat_number(req: FermatRequest):
    try:
        return engine.fermat_number(req.n)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/mersenne-number")
def mersenne_number(req: MersenneRequest):
    try:
        return engine.mersenne_number(req.p)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/linear-diophantine")
def linear_diophantine(req: ThreeIntRequest):
    try:
        return engine.linear_diophantine(req.a, req.b, req.c)
    except Exception as e:
        raise HTTPException(400, str(e))
