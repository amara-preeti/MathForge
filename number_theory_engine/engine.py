"""
Number Theory Engine
====================
A comprehensive number theory computation engine covering:
- Prime number generation, testing, and factorization
- GCD, LCM, modular arithmetic
- Continued fractions and Diophantine equations
- Euler's totient function, Mobius function
- Quadratic residues and Legendre symbols
- Chinese Remainder Theorem
- Primitive roots and discrete logarithms
- Elliptic curve basics over finite fields
"""

from __future__ import annotations
import math
import random
from typing import Generator, List, Optional, Tuple, Dict, Any
from functools import lru_cache
from sympy import (
    isprime, nextprime, prevprime, factorint, primefactors,
    gcd, lcm, totient, mobius, legendre_symbol, jacobi_symbol,
    sqrt_mod, nthroot_mod, discrete_log, primitive_root,
    continued_fraction, continued_fraction_convergents,
    n_order, quadratic_residues,
    perfect_power, mersenne_prime_exponent,
    divisors, proper_divisors, divisor_count, divisor_sigma,
    is_abundant, is_deficient, is_perfect,
    primeomega, primepi, prime,
    Integer, Rational
)
import sympy


class NumberTheoryEngine:
    """
    Full-featured number theory engine using SymPy as the underlying CAS.
    All methods are pure functions that return JSON-serializable results.
    """

    # ──────────────────────────────────────────────
    # Prime Numbers
    # ──────────────────────────────────────────────

    @staticmethod
    def is_prime(n: int) -> Dict[str, Any]:
        """Test whether n is a prime number (deterministic for n < 3.3×10^24)."""
        result = isprime(n)
        return {
            "n": n,
            "is_prime": result,
            "method": "sympy_isprime",
            "note": "Uses Miller-Rabin + BPSW for large numbers"
        }

    @staticmethod
    def next_prime(n: int) -> Dict[str, Any]:
        """Return the smallest prime > n."""
        p = int(nextprime(n))
        return {"n": n, "next_prime": p}

    @staticmethod
    def prev_prime(n: int) -> Optional[Dict[str, Any]]:
        """Return the largest prime < n, or None if n <= 2."""
        if n <= 2:
            return {"n": n, "prev_prime": None, "note": "No prime < 2"}
        p = int(prevprime(n))
        return {"n": n, "prev_prime": p}

    @staticmethod
    def nth_prime(n: int) -> Dict[str, Any]:
        """Return the n-th prime (1-indexed: prime(1) = 2)."""
        if n < 1:
            raise ValueError("n must be >= 1")
        p = int(prime(n))
        return {"n": n, "nth_prime": p}

    @staticmethod
    def prime_range(start: int, end: int) -> Dict[str, Any]:
        """Return all primes in [start, end]."""
        primes = list(sympy.primerange(start, end + 1))
        return {
            "start": start,
            "end": end,
            "primes": primes,
            "count": len(primes)
        }

    @staticmethod
    def prime_counting(n: int) -> Dict[str, Any]:
        """Return π(n), the number of primes ≤ n."""
        count = int(primepi(n))
        return {"n": n, "pi_n": count}

    @staticmethod
    def prime_factorization(n: int) -> Dict[str, Any]:
        """Return the prime factorization of n as a dict {prime: exponent}."""
        if n <= 1:
            raise ValueError("n must be > 1")
        factors = factorint(n)
        factors_str = {str(k): v for k, v in factors.items()}
        formatted = " × ".join(
            f"{p}^{e}" if e > 1 else str(p)
            for p, e in sorted(factors.items())
        )
        return {
            "n": n,
            "factors": {int(k): int(v) for k, v in factors.items()},
            "formatted": formatted,
            "prime_factors": sorted([int(p) for p in factors.keys()])
        }

    @staticmethod
    def sieve_of_eratosthenes(limit: int) -> Dict[str, Any]:
        """Pure Python sieve returning all primes up to limit."""
        if limit < 2:
            return {"limit": limit, "primes": [], "count": 0}
        sieve = bytearray([1]) * (limit + 1)
        sieve[0] = sieve[1] = 0
        for i in range(2, int(limit**0.5) + 1):
            if sieve[i]:
                sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
        primes = [i for i, v in enumerate(sieve) if v]
        return {"limit": limit, "primes": primes, "count": len(primes)}

    # ──────────────────────────────────────────────
    # GCD / LCM
    # ──────────────────────────────────────────────

    @staticmethod
    def compute_gcd(*args: int) -> Dict[str, Any]:
        """Compute GCD of two or more integers."""
        if len(args) < 2:
            raise ValueError("Need at least 2 arguments")
        result = math.gcd(*args)
        steps = NumberTheoryEngine._euclidean_steps(args[0], args[1]) if len(args) == 2 else []
        return {
            "inputs": list(args),
            "gcd": result,
            "euclidean_steps": steps
        }

    @staticmethod
    def compute_lcm(*args: int) -> Dict[str, Any]:
        """Compute LCM of two or more integers."""
        if len(args) < 2:
            raise ValueError("Need at least 2 arguments")
        result = math.lcm(*args)
        return {"inputs": list(args), "lcm": result}

    @staticmethod
    def _euclidean_steps(a: int, b: int) -> List[Dict[str, int]]:
        """Show Euclidean algorithm steps for gcd(a, b)."""
        steps = []
        while b:
            q, r = divmod(a, b)
            steps.append({"a": a, "b": b, "q": q, "r": r})
            a, b = b, r
        return steps

    @staticmethod
    def extended_gcd(a: int, b: int) -> Dict[str, Any]:
        """Extended Euclidean algorithm: returns gcd, x, y s.t. ax + by = gcd."""
        def _ext(a, b):
            if b == 0:
                return a, 1, 0
            g, x, y = _ext(b, a % b)
            return g, y, x - (a // b) * y
        g, x, y = _ext(a, b)
        return {
            "a": a, "b": b,
            "gcd": g, "x": x, "y": y,
            "verification": f"{a}×{x} + {b}×{y} = {a*x + b*y}"
        }

    # ──────────────────────────────────────────────
    # Modular Arithmetic
    # ──────────────────────────────────────────────

    @staticmethod
    def modular_exponentiation(base: int, exp: int, mod: int) -> Dict[str, Any]:
        """Compute base^exp mod m using fast exponentiation."""
        if mod <= 0:
            raise ValueError("Modulus must be positive")
        result = pow(base, exp, mod)
        return {"base": base, "exponent": exp, "modulus": mod, "result": result}

    @staticmethod
    def modular_inverse(a: int, m: int) -> Dict[str, Any]:
        """Compute a^(-1) mod m (exists iff gcd(a,m) = 1)."""
        if math.gcd(a, m) != 1:
            return {
                "a": a, "m": m,
                "inverse": None,
                "error": f"gcd({a},{m}) ≠ 1, inverse does not exist"
            }
        inv = pow(a, -1, m)
        return {
            "a": a, "m": m,
            "inverse": inv,
            "verification": f"{a} × {inv} ≡ {(a * inv) % m} (mod {m})"
        }

    @staticmethod
    def solve_linear_congruence(a: int, b: int, m: int) -> Dict[str, Any]:
        """Solve ax ≡ b (mod m)."""
        g = math.gcd(a, m)
        if b % g != 0:
            return {
                "equation": f"{a}x ≡ {b} (mod {m})",
                "solutions": [],
                "note": f"No solution: gcd({a},{m})={g} does not divide {b}"
            }
        a1, b1, m1 = a // g, b // g, m // g
        x0 = (b1 * pow(a1, -1, m1)) % m1
        solutions = [x0 + i * m1 for i in range(g)]
        return {
            "equation": f"{a}x ≡ {b} (mod {m})",
            "solutions": solutions,
            "general": f"x ≡ {x0} (mod {m1})",
            "num_solutions": g
        }

    @staticmethod
    def chinese_remainder_theorem(remainders: List[int], moduli: List[int]) -> Dict[str, Any]:
        """Solve system of congruences x ≡ r_i (mod m_i) via CRT."""
        if len(remainders) != len(moduli):
            raise ValueError("remainders and moduli must have same length")
        # Check pairwise coprime
        for i in range(len(moduli)):
            for j in range(i + 1, len(moduli)):
                if math.gcd(moduli[i], moduli[j]) != 1:
                    return {
                        "remainders": remainders,
                        "moduli": moduli,
                        "solution": None,
                        "error": f"Moduli {moduli[i]} and {moduli[j]} are not coprime"
                    }
        M = math.prod(moduli)
        x = sum(
            r * (M // m) * pow(M // m, -1, m)
            for r, m in zip(remainders, moduli)
        ) % M
        congruences = [f"x ≡ {r} (mod {m})" for r, m in zip(remainders, moduli)]
        return {
            "congruences": congruences,
            "solution": x,
            "modulus": M,
            "general": f"x ≡ {x} (mod {M})"
        }

    # ──────────────────────────────────────────────
    # Euler's Totient & Multiplicative Functions
    # ──────────────────────────────────────────────

    @staticmethod
    def euler_totient(n: int) -> Dict[str, Any]:
        """Compute φ(n) = number of integers in [1,n] coprime to n."""
        phi = int(totient(n))
        factors = factorint(n)
        return {
            "n": n,
            "totient": phi,
            "formula": "φ(n) = n × ∏(1 - 1/p) for prime p | n",
            "prime_factors_used": sorted([int(p) for p in factors.keys()])
        }

    @staticmethod
    def mobius_function(n: int) -> Dict[str, Any]:
        """
        Compute μ(n):
          0  if n has a squared prime factor
          1  if n = 1 or n has an even number of distinct prime factors
         -1  if n has an odd number of distinct prime factors
        """
        mu = int(mobius(n))
        factors = factorint(n)
        return {
            "n": n,
            "mobius": mu,
            "prime_factors": {int(k): int(v) for k, v in factors.items()},
            "interpretation": {
                0: "n has a squared prime factor (squarefree = False)",
                1: "n is squarefree with even # distinct prime factors",
                -1: "n is squarefree with odd # distinct prime factors"
            }[mu]
        }

    @staticmethod
    def divisors_of(n: int) -> Dict[str, Any]:
        """Return all divisors of n, divisor count τ(n), and divisor sum σ(n)."""
        divs = sorted([int(d) for d in divisors(n)])
        tau = int(divisor_count(n))
        sigma = int(divisor_sigma(n))
        return {
            "n": n,
            "divisors": divs,
            "tau": tau,      # σ_0(n)
            "sigma": sigma,  # σ_1(n)
            "perfect": sigma == 2 * n,
            "abundant": sigma > 2 * n,
            "deficient": sigma < 2 * n
        }

    # ──────────────────────────────────────────────
    # Quadratic Residues & Legendre / Jacobi Symbols
    # ──────────────────────────────────────────────

    @staticmethod
    def legendre(a: int, p: int) -> Dict[str, Any]:
        """Compute the Legendre symbol (a/p) for odd prime p."""
        if not isprime(p):
            raise ValueError(f"{p} must be an odd prime for Legendre symbol")
        val = int(legendre_symbol(a, p))
        meaning = {1: "QR", -1: "QNR", 0: "divisible by p"}[val]
        return {
            "a": a, "p": p,
            "legendre": val,
            "meaning": meaning
        }

    @staticmethod
    def jacobi(a: int, n: int) -> Dict[str, Any]:
        """Compute the Jacobi symbol (a/n) for odd positive n."""
        val = int(jacobi_symbol(a, n))
        return {"a": a, "n": n, "jacobi": val}

    @staticmethod
    def quadratic_residues_mod(p: int) -> Dict[str, Any]:
        """Return all quadratic residues mod p (p must be prime)."""
        qrs = sorted([int(x) for x in quadratic_residues(p)])
        return {
            "modulus": p,
            "quadratic_residues": qrs,
            "count": len(qrs)
        }

    @staticmethod
    def modular_sqrt(a: int, p: int) -> Dict[str, Any]:
        """Compute sqrt(a) mod p (Tonelli-Shanks), returns all solutions."""
        sols = sqrt_mod(a, p, all_roots=True)
        if sols is None:
            return {"a": a, "p": p, "roots": [], "note": "No modular square root"}
        sols = sorted([int(s) for s in sols])
        return {"a": a, "p": p, "roots": sols}

    # ──────────────────────────────────────────────
    # Primitive Roots & Discrete Log
    # ──────────────────────────────────────────────

    @staticmethod
    def find_primitive_root(p: int) -> Dict[str, Any]:
        """Find the smallest primitive root mod p."""
        if not isprime(p):
            raise ValueError(f"{p} must be prime")
        g = int(primitive_root(p))
        return {
            "p": p,
            "primitive_root": g,
            "order": p - 1,
            "note": "g^k generates all non-zero residues mod p"
        }

    @staticmethod
    def order_of_element(a: int, n: int) -> Dict[str, Any]:
        """Return the multiplicative order of a mod n (smallest k s.t. a^k ≡ 1)."""
        if math.gcd(a, n) != 1:
            return {"a": a, "n": n, "order": None, "error": "gcd(a,n) ≠ 1"}
        k = int(n_order(a, n))
        return {"a": a, "n": n, "order": k}

    @staticmethod
    def discrete_logarithm(a: int, b: int, p: int) -> Dict[str, Any]:
        """Solve a^x ≡ b (mod p) using baby-step giant-step."""
        try:
            x = int(discrete_log(p, b, a))
            return {
                "equation": f"{a}^x ≡ {b} (mod {p})",
                "x": x,
                "verification": f"{a}^{x} mod {p} = {pow(a, x, p)}"
            }
        except Exception as e:
            return {
                "equation": f"{a}^x ≡ {b} (mod {p})",
                "x": None,
                "error": str(e)
            }

    # ──────────────────────────────────────────────
    # Continued Fractions
    # ──────────────────────────────────────────────

    @staticmethod
    def continued_fraction_expansion(n: float, max_terms: int = 20) -> Dict[str, Any]:
        """
        Compute the continued fraction expansion of a real number.
        Returns coefficients [a0; a1, a2, ...] and convergents.
        """
        from sympy import Rational as Rat, sqrt as sym_sqrt, pi, E
        from sympy.ntheory.continued_fraction import continued_fraction_iterator
        rat = sympy.Rational(n).limit_denominator(10**15)
        cf = continued_fraction(rat)
        coeffs = [int(c) for c in cf]
        convergents = []
        for conv in continued_fraction_convergents(cf):
            p_val = int(conv.p)
            q_val = int(conv.q)
            convergents.append({"p": p_val, "q": q_val, "value": p_val / q_val})
            if len(convergents) >= max_terms:
                break
        return {
            "number": float(n),
            "coefficients": coeffs[:max_terms],
            "convergents": convergents,
            "notation": "[" + str(coeffs[0]) + "; " + ", ".join(map(str, coeffs[1:])) + "]"
        }

    # ──────────────────────────────────────────────
    # Special Number Checks
    # ──────────────────────────────────────────────

    @staticmethod
    def check_perfect_power(n: int) -> Dict[str, Any]:
        """Check if n = a^b for integers a,b > 1."""
        result = perfect_power(n)
        if result:
            a, b = result
            return {"n": n, "is_perfect_power": True, "base": int(a), "exponent": int(b)}
        return {"n": n, "is_perfect_power": False}

    @staticmethod
    def number_classification(n: int) -> Dict[str, Any]:
        """Classify n: prime, composite, perfect, abundant, deficient, etc."""
        classifications = []
        if n < 2:
            classifications.append("trivial")
        elif isprime(n):
            classifications.append("prime")
        else:
            classifications.append("composite")

        sig = int(divisor_sigma(n))
        if sig == 2 * n:
            classifications.append("perfect")
        elif sig > 2 * n:
            classifications.append("abundant")
        else:
            classifications.append("deficient")

        if perfect_power(n):
            classifications.append("perfect_power")

        return {
            "n": n,
            "classifications": classifications,
            "divisor_sum": sig
        }

    # ──────────────────────────────────────────────
    # Diophantine Equations
    # ──────────────────────────────────────────────

    @staticmethod
    def linear_diophantine(a: int, b: int, c: int) -> Dict[str, Any]:
        """
        Solve ax + by = c for integers x, y.
        Returns particular solution + general solution.
        """
        g = math.gcd(abs(a), abs(b))
        if c % g != 0:
            return {
                "equation": f"{a}x + {b}y = {c}",
                "solvable": False,
                "note": f"gcd({a},{b})={g} does not divide {c}"
            }
        a1, b1, c1 = a // g, b // g, c // g
        _, x0, y0 = NumberTheoryEngine.extended_gcd(a1, b1).values()
        # Exclude 'verification' string key
        ext = NumberTheoryEngine._ext_gcd_raw(a1, b1)
        x0_r, y0_r = ext
        x_part = x0_r * c1
        y_part = y0_r * c1
        return {
            "equation": f"{a}x + {b}y = {c}",
            "solvable": True,
            "particular_solution": {"x": x_part, "y": y_part},
            "general_solution": {
                "x": f"{x_part} + {b1}t",
                "y": f"{y_part} - {a1}t",
                "note": "t ∈ ℤ"
            }
        }

    @staticmethod
    def _ext_gcd_raw(a: int, b: int) -> Tuple[int, int]:
        if b == 0:
            return 1, 0
        x, y = NumberTheoryEngine._ext_gcd_raw(b, a % b)
        return y, x - (a // b) * y

    # ──────────────────────────────────────────────
    # Fermat & Mersenne Numbers
    # ──────────────────────────────────────────────

    @staticmethod
    def fermat_number(n: int) -> Dict[str, Any]:
        """Compute F_n = 2^(2^n) + 1."""
        val = 2**(2**n) + 1
        is_p = isprime(val) if n <= 4 else None  # Only known for small n
        return {
            "n": n,
            "fermat_number": val,
            "is_prime": is_p,
            "digits": len(str(val))
        }

    @staticmethod
    def mersenne_number(p: int) -> Dict[str, Any]:
        """Compute M_p = 2^p - 1 and test primality."""
        if not isprime(p):
            return {"p": p, "mersenne": None, "error": "p must be prime"}
        val = 2**p - 1
        # Lucas-Lehmer test via sympy for reasonably sized p
        is_mp = isprime(val) if p <= 127 else None
        return {
            "p": p,
            "mersenne": val,
            "is_mersenne_prime": is_mp,
            "digits": len(str(val))
        }
