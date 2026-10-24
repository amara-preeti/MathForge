import { useState } from 'react';
import { Calculator, Hash, Binary, GitBranch, Zap, Infinity, Search, Layers } from 'lucide-react';

const API = 'http://localhost:8000/number-theory';

type TabId = 'primes' | 'gcd' | 'modular' | 'crt' | 'totient' | 'continued' | 'diophantine' | 'classify';

interface Tab { id: TabId; label: string; icon: React.ReactNode; }

const TABS: Tab[] = [
  { id: 'primes',      label: 'Primes',         icon: <Hash size={16} /> },
  { id: 'gcd',         label: 'GCD / LCM',       icon: <Calculator size={16} /> },
  { id: 'modular',     label: 'Modular Arith.',  icon: <Binary size={16} /> },
  { id: 'crt',         label: 'CRT',             icon: <GitBranch size={16} /> },
  { id: 'totient',     label: 'Totient',         icon: <Zap size={16} /> },
  { id: 'continued',   label: 'Cont. Fractions', icon: <Infinity size={16} /> },
  { id: 'diophantine', label: 'Diophantine',     icon: <Layers size={16} /> },
  { id: 'classify',    label: 'Classify',        icon: <Search size={16} /> },
];

async function post(endpoint: string, body: object) {
  const res = await fetch(`${API}${endpoint}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error((await res.json()).detail || 'Error');
  return res.json();
}

function ResultBox({ data }: { data: object | null }) {
  if (!data) return null;
  return (
    <div className="result-box">
      <pre className="result-pre">{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

// ── Prime Tab ────────────────────────────────────────────────
function PrimesTab() {
  const [n, setN] = useState('97');
  const [rangeStart, setRangeStart] = useState('1');
  const [rangeEnd, setRangeEnd] = useState('100');
  const [sieveLimit, setSieveLimit] = useState('50');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async (action: string) => {
    setLoading(true); setError(''); setResult(null);
    try {
      let data;
      if (action === 'is_prime') data = await post('/is-prime', { n: parseInt(n) });
      else if (action === 'next') data = await post('/next-prime', { n: parseInt(n) });
      else if (action === 'prev') data = await post('/prev-prime', { n: parseInt(n) });
      else if (action === 'nth') data = await post('/nth-prime', { n: parseInt(n) });
      else if (action === 'factorize') data = await post('/prime-factorization', { n: parseInt(n) });
      else if (action === 'counting') data = await post('/prime-counting', { n: parseInt(n) });
      else if (action === 'range') data = await post('/prime-range', { start: parseInt(rangeStart), end: parseInt(rangeEnd) });
      else if (action === 'sieve') data = await post('/sieve', { n: parseInt(sieveLimit) });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <div className="form-group">
        <label className="form-label">Integer n</label>
        <input className="form-input" value={n} onChange={e => setN(e.target.value)} type="number" />
      </div>
      <div className="button-grid">
        {[
          { label: '🔍 Is Prime?', action: 'is_prime' },
          { label: '→ Next Prime', action: 'next' },
          { label: '← Prev Prime', action: 'prev' },
          { label: '# Nth Prime', action: 'nth' },
          { label: '∏ Factorize', action: 'factorize' },
          { label: 'π(n) Counting', action: 'counting' },
        ].map(b => (
          <button key={b.action} className="btn btn-primary" onClick={() => run(b.action)} disabled={loading}>
            {b.label}
          </button>
        ))}
      </div>

      <div className="divider" />
      <div className="form-row">
        <div className="form-group">
          <label className="form-label">Range Start</label>
          <input className="form-input" value={rangeStart} onChange={e => setRangeStart(e.target.value)} type="number" />
        </div>
        <div className="form-group">
          <label className="form-label">Range End</label>
          <input className="form-input" value={rangeEnd} onChange={e => setRangeEnd(e.target.value)} type="number" />
        </div>
      </div>
      <button className="btn btn-secondary" onClick={() => run('range')} disabled={loading}>
        📋 Primes in Range
      </button>

      <div className="divider" />
      <div className="form-group">
        <label className="form-label">Sieve Limit</label>
        <input className="form-input" value={sieveLimit} onChange={e => setSieveLimit(e.target.value)} type="number" />
      </div>
      <button className="btn btn-secondary" onClick={() => run('sieve')} disabled={loading}>
        🔲 Sieve of Eratosthenes
      </button>

      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── GCD Tab ──────────────────────────────────────────────────
function GcdTab() {
  const [a, setA] = useState('48');
  const [b, setB] = useState('18');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async (action: string) => {
    setLoading(true); setError(''); setResult(null);
    try {
      const ai = parseInt(a), bi = parseInt(b);
      let data;
      if (action === 'gcd') data = await post('/gcd', { a: ai, b: bi });
      else if (action === 'lcm') data = await post('/lcm', { a: ai, b: bi });
      else if (action === 'ext') data = await post('/extended-gcd', { a: ai, b: bi });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <div className="form-row">
        <div className="form-group">
          <label className="form-label">a</label>
          <input className="form-input" value={a} onChange={e => setA(e.target.value)} type="number" />
        </div>
        <div className="form-group">
          <label className="form-label">b</label>
          <input className="form-input" value={b} onChange={e => setB(e.target.value)} type="number" />
        </div>
      </div>
      <div className="button-grid">
        <button className="btn btn-primary" onClick={() => run('gcd')} disabled={loading}>GCD(a,b)</button>
        <button className="btn btn-primary" onClick={() => run('lcm')} disabled={loading}>LCM(a,b)</button>
        <button className="btn btn-secondary" onClick={() => run('ext')} disabled={loading}>Extended GCD (Bézout)</button>
      </div>
      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── Modular Arithmetic Tab ────────────────────────────────────
function ModularTab() {
  const [base, setBase] = useState('3');
  const [exp, setExp] = useState('200');
  const [mod, setMod] = useState('13');
  const [a, setA] = useState('7');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async (action: string) => {
    setLoading(true); setError(''); setResult(null);
    try {
      let data;
      if (action === 'modexp') data = await post('/modular-exp', { base: parseInt(base), exp: parseInt(exp), mod: parseInt(mod) });
      else if (action === 'inverse') data = await post('/modular-inverse', { a: parseInt(a), b: parseInt(mod) });
      else if (action === 'congruence') data = await post('/linear-congruence', { a: parseInt(a), b: parseInt(base), m: parseInt(mod) });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <div className="form-group">
        <label className="form-label">Modulus m</label>
        <input className="form-input" value={mod} onChange={e => setMod(e.target.value)} type="number" />
      </div>
      <div className="form-row">
        <div className="form-group">
          <label className="form-label">Base</label>
          <input className="form-input" value={base} onChange={e => setBase(e.target.value)} type="number" />
        </div>
        <div className="form-group">
          <label className="form-label">Exponent</label>
          <input className="form-input" value={exp} onChange={e => setExp(e.target.value)} type="number" />
        </div>
      </div>
      <button className="btn btn-primary" onClick={() => run('modexp')} disabled={loading}>
        base^exp (mod m)
      </button>

      <div className="divider" />
      <div className="form-group">
        <label className="form-label">a (for inverse: a⁻¹ mod m)</label>
        <input className="form-input" value={a} onChange={e => setA(e.target.value)} type="number" />
      </div>
      <div className="button-grid">
        <button className="btn btn-secondary" onClick={() => run('inverse')} disabled={loading}>
          Modular Inverse a⁻¹ mod m
        </button>
        <button className="btn btn-secondary" onClick={() => run('congruence')} disabled={loading}>
          Solve ax ≡ b (mod m)
        </button>
      </div>
      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── CRT Tab ───────────────────────────────────────────────────
function CrtTab() {
  const [remainders, setRemainders] = useState('2, 3, 2');
  const [moduli, setModuli] = useState('3, 5, 7');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async () => {
    setLoading(true); setError(''); setResult(null);
    try {
      const r = remainders.split(',').map(s => parseInt(s.trim()));
      const m = moduli.split(',').map(s => parseInt(s.trim()));
      const data = await post('/crt', { remainders: r, moduli: m });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <div className="info-box">
        Chinese Remainder Theorem: solve system of congruences x ≡ rᵢ (mod mᵢ)
      </div>
      <div className="form-group">
        <label className="form-label">Remainders (comma-separated)</label>
        <input className="form-input" value={remainders} onChange={e => setRemainders(e.target.value)} placeholder="2, 3, 2" />
      </div>
      <div className="form-group">
        <label className="form-label">Moduli (comma-separated, pairwise coprime)</label>
        <input className="form-input" value={moduli} onChange={e => setModuli(e.target.value)} placeholder="3, 5, 7" />
      </div>
      <button className="btn btn-primary" onClick={run} disabled={loading}>
        🔢 Solve CRT System
      </button>
      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── Totient Tab ───────────────────────────────────────────────
function TotientTab() {
  const [n, setN] = useState('36');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async (action: string) => {
    setLoading(true); setError(''); setResult(null);
    try {
      let data;
      if (action === 'totient') data = await post('/euler-totient', { n: parseInt(n) });
      else if (action === 'mobius') data = await post('/mobius', { n: parseInt(n) });
      else if (action === 'divisors') data = await post('/divisors', { n: parseInt(n) });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <div className="form-group">
        <label className="form-label">n</label>
        <input className="form-input" value={n} onChange={e => setN(e.target.value)} type="number" />
      </div>
      <div className="button-grid">
        <button className="btn btn-primary" onClick={() => run('totient')} disabled={loading}>φ(n) Euler Totient</button>
        <button className="btn btn-primary" onClick={() => run('mobius')} disabled={loading}>μ(n) Möbius Function</button>
        <button className="btn btn-secondary" onClick={() => run('divisors')} disabled={loading}>τ(n), σ(n) Divisors</button>
      </div>
      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── Continued Fractions Tab ───────────────────────────────────
function ContinuedFractionTab() {
  const [n, setN] = useState('3.14159265');
  const [maxTerms, setMaxTerms] = useState('15');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async () => {
    setLoading(true); setError(''); setResult(null);
    try {
      const data = await post('/continued-fraction', { n: parseFloat(n), max_terms: parseInt(maxTerms) });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <div className="info-box">
        Compute continued fraction [a₀; a₁, a₂, ...] and convergents p_n/q_n.
      </div>
      <div className="form-row">
        <div className="form-group">
          <label className="form-label">Number</label>
          <input className="form-input" value={n} onChange={e => setN(e.target.value)} />
        </div>
        <div className="form-group">
          <label className="form-label">Max Terms</label>
          <input className="form-input" value={maxTerms} onChange={e => setMaxTerms(e.target.value)} type="number" />
        </div>
      </div>
      <button className="btn btn-primary" onClick={run} disabled={loading}>∞ Expand</button>
      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── Diophantine Tab ───────────────────────────────────────────
function DiophantineTab() {
  const [a, setA] = useState('6');
  const [b, setB] = useState('10');
  const [c, setC] = useState('14');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async () => {
    setLoading(true); setError(''); setResult(null);
    try {
      const data = await post('/linear-diophantine', { a: parseInt(a), b: parseInt(b), c: parseInt(c) });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <div className="info-box">Solve ax + by = c for integers x, y</div>
      <div className="form-row">
        <div className="form-group"><label className="form-label">a</label>
          <input className="form-input" value={a} onChange={e => setA(e.target.value)} type="number" />
        </div>
        <div className="form-group"><label className="form-label">b</label>
          <input className="form-input" value={b} onChange={e => setB(e.target.value)} type="number" />
        </div>
        <div className="form-group"><label className="form-label">c</label>
          <input className="form-input" value={c} onChange={e => setC(e.target.value)} type="number" />
        </div>
      </div>
      <button className="btn btn-primary" onClick={run} disabled={loading}>🔢 Solve ax + by = c</button>
      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── Classify Tab ──────────────────────────────────────────────
function ClassifyTab() {
  const [n, setN] = useState('28');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async (action: string) => {
    setLoading(true); setError(''); setResult(null);
    try {
      let data;
      if (action === 'classify') data = await post('/number-classification', { n: parseInt(n) });
      else if (action === 'fermat') data = await post('/fermat-number', { n: parseInt(n) });
      else if (action === 'mersenne') data = await post('/mersenne-number', { p: parseInt(n) });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <div className="form-group">
        <label className="form-label">n</label>
        <input className="form-input" value={n} onChange={e => setN(e.target.value)} type="number" />
      </div>
      <div className="button-grid">
        <button className="btn btn-primary" onClick={() => run('classify')} disabled={loading}>🏷️ Classify n</button>
        <button className="btn btn-secondary" onClick={() => run('fermat')} disabled={loading}>F_n Fermat Number</button>
        <button className="btn btn-secondary" onClick={() => run('mersenne')} disabled={loading}>M_p Mersenne Number</button>
      </div>
      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── Main Component ────────────────────────────────────────────
export default function NumberTheoryLab() {
  const [activeTab, setActiveTab] = useState<TabId>('primes');

  const TAB_COMPONENTS: Record<TabId, React.ReactNode> = {
    primes:      <PrimesTab />,
    gcd:         <GcdTab />,
    modular:     <ModularTab />,
    crt:         <CrtTab />,
    totient:     <TotientTab />,
    continued:   <ContinuedFractionTab />,
    diophantine: <DiophantineTab />,
    classify:    <ClassifyTab />,
  };

  return (
    <div className="lab-container">
      <div className="lab-header">
        <div className="lab-header-icon">
          <Hash size={28} />
        </div>
        <div>
          <h1 className="lab-title">Number Theory Lab</h1>
          <p className="lab-subtitle">
            Primes, GCD/LCM, modular arithmetic, CRT, Euler's totient, continued fractions, Diophantine equations
          </p>
        </div>
      </div>

      <div className="tab-bar">
        {TABS.map(tab => (
          <button
            key={tab.id}
            className={`tab-btn ${activeTab === tab.id ? 'tab-btn-active' : ''}`}
            onClick={() => setActiveTab(tab.id)}
          >
            {tab.icon}
            <span>{tab.label}</span>
          </button>
        ))}
      </div>

      <div className="lab-body">
        {TAB_COMPONENTS[activeTab]}
      </div>
    </div>
  );
}
