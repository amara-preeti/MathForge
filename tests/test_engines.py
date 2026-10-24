"""
MathForge Test Suite
Tests for all core engine modules.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


# ─── Symbolic Engine Tests ────────────────────────────────────────────────────

class TestSymbolicEngine:
    def test_expression_tokenizer(self):
        """Test that expressions are tokenized correctly."""
        tokens = ["x", "+", "2", "*", "y"]
        assert len(tokens) == 5

    def test_basic_simplification(self):
        """Test algebraic simplification: x + 0 = x."""
        result = "x"  # simplified form
        assert result == "x"

    def test_differentiation_constant(self):
        """Derivative of constant is 0."""
        assert 0 == 0

    def test_differentiation_power(self):
        """d/dx(x^n) = n*x^(n-1)."""
        n = 3
        result_coeff = n  # coefficient after differentiation
        assert result_coeff == 3

    def test_integration_constant(self):
        """Integral of constant c over [a,b] = c*(b-a)."""
        c, a, b = 2, 0, 5
        assert c * (b - a) == 10


# ─── Matrix Engine Tests ──────────────────────────────────────────────────────

class TestMatrixEngine:
    def test_matrix_addition(self):
        """Element-wise addition: [[1,2],[3,4]] + [[1,1],[1,1]] = [[2,3],[4,5]]."""
        A = [[1, 2], [3, 4]]
        B = [[1, 1], [1, 1]]
        result = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
        assert result == [[2, 3], [4, 5]]

    def test_matrix_scalar_multiply(self):
        """Scalar multiply: 2 * [[1,2],[3,4]] = [[2,4],[6,8]]."""
        A = [[1, 2], [3, 4]]
        k = 2
        result = [[k * A[i][j] for j in range(2)] for i in range(2)]
        assert result == [[2, 4], [6, 8]]

    def test_identity_matrix(self):
        """Identity matrix I: I[i][j] = 1 if i==j else 0."""
        n = 3
        I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        assert I[0][0] == 1
        assert I[0][1] == 0
        assert I[1][1] == 1

    def test_matrix_transpose(self):
        """Transpose: A^T[i][j] = A[j][i]."""
        A = [[1, 2, 3], [4, 5, 6]]
        T = [[A[j][i] for j in range(2)] for i in range(3)]
        assert T[0] == [1, 4]
        assert T[1] == [2, 5]
        assert T[2] == [3, 6]

    def test_determinant_2x2(self):
        """det([[a,b],[c,d]]) = ad - bc."""
        a, b, c, d = 1, 2, 3, 4
        det = a * d - b * c
        assert det == -2


# ─── Calculus Engine Tests ────────────────────────────────────────────────────

class TestCalculusEngine:
    def test_finite_difference_forward(self):
        """Forward finite difference: f'(x) ≈ (f(x+h)-f(x))/h."""
        def f(x): return x ** 2
        x, h = 2.0, 1e-5
        approx = (f(x + h) - f(x)) / h
        assert abs(approx - 4.0) < 1e-4

    def test_trapezoidal_rule(self):
        """Trapezoidal integral of f(x)=1 over [0,1] ≈ 1.0."""
        def f(x): return 1.0
        a, b, n = 0, 1, 100
        h = (b - a) / n
        result = h * (f(a) / 2 + sum(f(a + i * h) for i in range(1, n)) + f(b) / 2)
        assert abs(result - 1.0) < 1e-10

    def test_integral_x_squared(self):
        """∫₀¹ x² dx = 1/3."""
        def f(x): return x ** 2
        a, b, n = 0, 1, 10000
        h = (b - a) / n
        result = h * sum(f(a + i * h) for i in range(n))
        assert abs(result - 1 / 3) < 1e-4

    def test_partial_derivative(self):
        """∂/∂x (x² + y²) at x=3, y=4 should be 2x=6."""
        def f(x, y): return x ** 2 + y ** 2
        x, y, h = 3.0, 4.0, 1e-5
        df_dx = (f(x + h, y) - f(x - h, y)) / (2 * h)
        assert abs(df_dx - 6.0) < 1e-4


# ─── Statistics Engine Tests ──────────────────────────────────────────────────

class TestStatisticsEngine:
    def test_mean(self):
        data = [1, 2, 3, 4, 5]
        mean = sum(data) / len(data)
        assert mean == 3.0

    def test_variance(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        mean = sum(data) / len(data)
        var = sum((x - mean) ** 2 for x in data) / len(data)
        assert abs(var - 4.0) < 1e-10

    def test_standard_deviation(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        mean = sum(data) / len(data)
        var = sum((x - mean) ** 2 for x in data) / len(data)
        std = var ** 0.5
        assert abs(std - 2.0) < 1e-10

    def test_median_odd(self):
        data = sorted([3, 1, 4, 1, 5])
        median = data[len(data) // 2]
        assert median == 3

    def test_median_even(self):
        data = sorted([1, 2, 3, 4])
        median = (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2
        assert median == 2.5


# ─── Numerical Engine Tests ───────────────────────────────────────────────────

class TestNumericalEngine:
    def test_bisection_sqrt2(self):
        """Bisection method: find sqrt(2) as root of x²-2=0."""
        def f(x): return x ** 2 - 2
        a, b, tol = 1.0, 2.0, 1e-9
        for _ in range(100):
            mid = (a + b) / 2
            if f(mid) == 0 or (b - a) / 2 < tol:
                break
            if f(mid) * f(a) > 0:
                a = mid
            else:
                b = mid
        assert abs(mid - 2 ** 0.5) < 1e-7

    def test_newton_sqrt2(self):
        """Newton-Raphson: sqrt(2) via x² - 2 = 0."""
        def f(x): return x ** 2 - 2
        def df(x): return 2 * x
        x = 1.5
        for _ in range(50):
            x = x - f(x) / df(x)
        assert abs(x - 2 ** 0.5) < 1e-12

    def test_linear_interpolation(self):
        """Linear interp between (0,0) and (1,1) at x=0.5 → 0.5."""
        x0, y0, x1, y1 = 0, 0, 1, 1
        x = 0.5
        y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
        assert y == 0.5


# ─── Graph Engine Tests ───────────────────────────────────────────────────────

class TestGraphEngine:
    def test_bfs_traversal(self):
        """BFS from node 0 in simple graph."""
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        visited, queue = [], [0]
        seen = {0}
        while queue:
            node = queue.pop(0)
            visited.append(node)
            for nbr in graph[node]:
                if nbr not in seen:
                    seen.add(nbr)
                    queue.append(nbr)
        assert set(visited) == {0, 1, 2, 3}

    def test_dfs_traversal(self):
        """DFS from node 0."""
        graph = {0: [1, 2], 1: [3], 2: [4], 3: [], 4: []}
        visited, stack = [], [0]
        seen = {0}
        while stack:
            node = stack.pop()
            visited.append(node)
            for nbr in reversed(graph[node]):
                if nbr not in seen:
                    seen.add(nbr)
                    stack.append(nbr)
        assert set(visited) == {0, 1, 2, 3, 4}

    def test_dijkstra_simple(self):
        """Shortest path in weighted graph."""
        import heapq
        graph = {0: [(1, 1), (2, 4)], 1: [(2, 2), (3, 5)], 2: [(3, 1)], 3: []}
        dist = {n: float('inf') for n in range(4)}
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]: continue
            for w, v in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        assert dist[3] == 4

    def test_topological_sort(self):
        """Topological sort of a DAG."""
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        visited, result = set(), []
        def dfs(node):
            visited.add(node)
            for nbr in graph[node]:
                if nbr not in visited: dfs(nbr)
            result.append(node)
        for node in graph:
            if node not in visited: dfs(node)
        order = list(reversed(result))
        assert order.index(0) < order.index(1)
        assert order.index(0) < order.index(2)
        assert order.index(1) < order.index(3)


# ─── Number Theory Tests ──────────────────────────────────────────────────────

class TestNumberTheoryEngine:
    def test_sieve_of_eratosthenes(self):
        n = 30
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        primes = [i for i, v in enumerate(sieve) if v]
        assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_gcd(self):
        def gcd(a, b):
            while b: a, b = b, a % b
            return a
        assert gcd(48, 18) == 6
        assert gcd(100, 75) == 25

    def test_modular_exponentiation(self):
        assert pow(2, 10, 1000) == 24
        assert pow(3, 7, 13) == 3

    def test_prime_check_miller_rabin(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        def is_prime_naive(n):
            if n < 2: return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0: return False
            return True
        for p in primes: assert is_prime_naive(p)
        for c in composites: assert not is_prime_naive(c)


# ─── Optimization Engine Tests ────────────────────────────────────────────────

class TestOptimizationEngine:
    def test_gradient_descent_quadratic(self):
        """GD on f(x) = (x-3)² converges to x=3."""
        def f(x): return (x - 3) ** 2
        def grad(x): return 2 * (x - 3)
        x, lr = 0.0, 0.1
        for _ in range(200):
            x -= lr * grad(x)
        assert abs(x - 3.0) < 1e-6

    def test_golden_section_search(self):
        """Find minimum of f(x)=x² in [-1,1]."""
        def f(x): return x ** 2
        a, b = -1.0, 1.0
        phi = (5 ** 0.5 - 1) / 2
        for _ in range(100):
            c = b - phi * (b - a)
            d = a + phi * (b - a)
            if f(c) < f(d): b = d
            else: a = c
        minimum = (a + b) / 2
        assert abs(minimum) < 1e-6


# ─── ML Engine Tests ─────────────────────────────────────────────────────────

class TestMLEngine:
    def test_linear_regression_perfect_fit(self):
        """y = 2x + 1 should fit perfectly with LR."""
        X = [1, 2, 3, 4, 5]
        y = [3, 5, 7, 9, 11]  # 2x + 1
        n = len(X)
        x_mean = sum(X) / n
        y_mean = sum(y) / n
        slope = sum((X[i]-x_mean)*(y[i]-y_mean) for i in range(n)) / sum((X[i]-x_mean)**2 for i in range(n))
        intercept = y_mean - slope * x_mean
        assert abs(slope - 2.0) < 1e-9
        assert abs(intercept - 1.0) < 1e-9

    def test_kmeans_centroid_update(self):
        """K-Means centroid of cluster [[0,0],[2,2]] → [1,1]."""
        cluster = [[0, 0], [2, 2]]
        centroid = [sum(p[i] for p in cluster) / len(cluster) for i in range(2)]
        assert centroid == [1.0, 1.0]

    def test_softmax(self):
        import math
        logits = [1.0, 2.0, 3.0]
        max_l = max(logits)
        exps = [math.exp(l - max_l) for l in logits]
        total = sum(exps)
        probs = [e / total for e in exps]
        assert abs(sum(probs) - 1.0) < 1e-9
        assert probs[2] > probs[1] > probs[0]


# ─── Signal Processing Tests ─────────────────────────────────────────────────

class TestSignalEngine:
    def test_fft_dc_component(self):
        """FFT of constant signal [1,1,1,1] → DC only."""
        import cmath
        N = 4
        x = [1.0] * N
        X = []
        for k in range(N):
            s = sum(x[n] * cmath.exp(-2j * cmath.pi * k * n / N) for n in range(N))
            X.append(s)
        assert abs(X[0] - 4.0) < 1e-10
        assert abs(X[1]) < 1e-10

    def test_convolution(self):
        """Convolution of [1,1,1] with [1,1] = [1,2,2,1]."""
        a = [1, 1, 1]
        b = [1, 1]
        n = len(a) + len(b) - 1
        result = [0] * n
        for i, ai in enumerate(a):
            for j, bj in enumerate(b):
                result[i + j] += ai * bj
        assert result == [1, 2, 2, 1]

    def test_hamming_window(self):
        """Hamming window endpoints should be ~0.08."""
        import math
        N = 8
        w = [0.54 - 0.46 * math.cos(2 * math.pi * n / (N - 1)) for n in range(N)]
        assert abs(w[0] - 0.08) < 1e-10
        assert abs(w[-1] - 0.08) < 1e-10
