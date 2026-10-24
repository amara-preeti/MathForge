import { useState } from 'react';
import { Atom, Thermometer, Zap, Waves, Clock, Weight, Globe } from 'lucide-react';

const API = 'http://localhost:8000/physics';

type TabId = 'mechanics' | 'thermodynamics' | 'electrostatics' | 'relativity' | 'quantum' | 'gravity' | 'waves';

interface Tab { id: TabId; label: string; icon: React.ReactNode; }

const TABS: Tab[] = [
  { id: 'mechanics',       label: 'Mechanics',       icon: <Weight size={16} /> },
  { id: 'thermodynamics',  label: 'Thermodynamics',  icon: <Thermometer size={16} /> },
  { id: 'electrostatics',  label: 'Electrostatics',  icon: <Zap size={16} /> },
  { id: 'relativity',      label: 'Relativity',      icon: <Clock size={16} /> },
  { id: 'quantum',         label: 'Quantum',         icon: <Atom size={16} /> },
  { id: 'gravity',         label: 'Gravity',         icon: <Globe size={16} /> },
  { id: 'waves',           label: 'Waves',           icon: <Waves size={16} /> },
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

// ── Mechanics Tab ────────────────────────────────────────────
function MechanicsTab() {
  const [v0, setV0] = useState('0');
  const [a, setA] = useState('9.8');
  const [t, setT] = useState('5');
  const [projV0, setProjV0] = useState('30');
  const [projAngle, setProjAngle] = useState('45');
  const [m1, setM1] = useState('2');
  const [v1, setV1] = useState('5');
  const [m2, setM2] = useState('3');
  const [v2, setV2] = useState('-2');
  const [collType, setCollType] = useState('elastic');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async (action: string) => {
    setLoading(true); setError(''); setResult(null);
    try {
      let data;
      if (action === 'kinematics') data = await post('/kinematics-1d', { v0: parseFloat(v0), a: parseFloat(a), t: parseFloat(t) });
      else if (action === 'projectile') data = await post('/projectile-motion', { v0: parseFloat(projV0), angle_deg: parseFloat(projAngle) });
      else if (action === 'collision') data = await post('/collision', { m1: parseFloat(m1), v1: parseFloat(v1), m2: parseFloat(m2), v2: parseFloat(v2), collision_type: collType });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <h3 className="section-title">1D Kinematics (v₀ + at)</h3>
      <div className="form-row">
        <div className="form-group"><label className="form-label">v₀ (m/s)</label>
          <input className="form-input" value={v0} onChange={e => setV0(e.target.value)} type="number" /></div>
        <div className="form-group"><label className="form-label">a (m/s²)</label>
          <input className="form-input" value={a} onChange={e => setA(e.target.value)} type="number" /></div>
        <div className="form-group"><label className="form-label">t (s)</label>
          <input className="form-input" value={t} onChange={e => setT(e.target.value)} type="number" /></div>
      </div>
      <button className="btn btn-primary" onClick={() => run('kinematics')} disabled={loading}>📐 Compute Kinematics</button>

      <div className="divider" />
      <h3 className="section-title">Projectile Motion</h3>
      <div className="form-row">
        <div className="form-group"><label className="form-label">v₀ (m/s)</label>
          <input className="form-input" value={projV0} onChange={e => setProjV0(e.target.value)} type="number" /></div>
        <div className="form-group"><label className="form-label">Angle (°)</label>
          <input className="form-input" value={projAngle} onChange={e => setProjAngle(e.target.value)} type="number" /></div>
      </div>
      <button className="btn btn-secondary" onClick={() => run('projectile')} disabled={loading}>🎯 Launch Projectile</button>

      <div className="divider" />
      <h3 className="section-title">1D Collision</h3>
      <div className="form-row">
        {[['m₁', m1, setM1], ['v₁', v1, setV1], ['m₂', m2, setM2], ['v₂', v2, setV2]].map(([label, val, setter]) => (
          <div key={label as string} className="form-group">
            <label className="form-label">{label as string} (kg or m/s)</label>
            <input className="form-input" value={val as string} onChange={e => (setter as (v: string) => void)(e.target.value)} type="number" />
          </div>
        ))}
      </div>
      <div className="form-group">
        <label className="form-label">Collision Type</label>
        <select className="form-select" value={collType} onChange={e => setCollType(e.target.value)}>
          <option value="elastic">Elastic</option>
          <option value="inelastic">Perfectly Inelastic</option>
        </select>
      </div>
      <button className="btn btn-secondary" onClick={() => run('collision')} disabled={loading}>💥 Compute Collision</button>

      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── Thermodynamics Tab ────────────────────────────────────────
function ThermodynamicsTab() {
  const [P, setP] = useState('');
  const [V, setV] = useState('0.0224');
  const [n, setN] = useState('1');
  const [T, setT] = useState('273.15');
  const [Thot, setThot] = useState('800');
  const [Tcold, setTcold] = useState('300');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async (action: string) => {
    setLoading(true); setError(''); setResult(null);
    try {
      let data;
      if (action === 'gas') data = await post('/ideal-gas', {
        P: P ? parseFloat(P) : null,
        V: V ? parseFloat(V) : null,
        n: n ? parseFloat(n) : null,
        T: T ? parseFloat(T) : null
      });
      else if (action === 'carnot') data = await post('/carnot', { T_hot: parseFloat(Thot), T_cold: parseFloat(Tcold) });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <h3 className="section-title">Ideal Gas Law (PV = nRT) — Leave one blank to solve</h3>
      <div className="form-row">
        {[['P (Pa)', P, setP], ['V (m³)', V, setV], ['n (mol)', n, setN], ['T (K)', T, setT]].map(([label, val, setter]) => (
          <div key={label as string} className="form-group">
            <label className="form-label">{label as string}</label>
            <input className="form-input" value={val as string}
              onChange={e => (setter as (v: string) => void)(e.target.value)} type="number" placeholder="Leave blank to solve" />
          </div>
        ))}
      </div>
      <button className="btn btn-primary" onClick={() => run('gas')} disabled={loading}>🔬 Solve Ideal Gas</button>

      <div className="divider" />
      <h3 className="section-title">Carnot Engine</h3>
      <div className="form-row">
        <div className="form-group"><label className="form-label">T_hot (K)</label>
          <input className="form-input" value={Thot} onChange={e => setThot(e.target.value)} type="number" /></div>
        <div className="form-group"><label className="form-label">T_cold (K)</label>
          <input className="form-input" value={Tcold} onChange={e => setTcold(e.target.value)} type="number" /></div>
      </div>
      <button className="btn btn-secondary" onClick={() => run('carnot')} disabled={loading}>⚙️ Carnot Efficiency</button>

      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── Electrostatics Tab ────────────────────────────────────────
function ElectrostaticsTab() {
  const [q1, setQ1] = useState('1e-6');
  const [q2, setQ2] = useState('-2e-6');
  const [r, setR] = useState('0.1');
  const [V, setV] = useState('');
  const [I, setI] = useState('2');
  const [R, setR2] = useState('5');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async (action: string) => {
    setLoading(true); setError(''); setResult(null);
    try {
      let data;
      if (action === 'coulomb') data = await post('/coulombs-law', { q1: parseFloat(q1), q2: parseFloat(q2), r: parseFloat(r) });
      else if (action === 'efield') data = await post('/electric-field', { q: parseFloat(q1), r: parseFloat(r) });
      else if (action === 'ohm') data = await post('/ohms-law', {
        V: V ? parseFloat(V) : null,
        I: I ? parseFloat(I) : null,
        R: R ? parseFloat(R) : null
      });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <h3 className="section-title">Coulomb's Law</h3>
      <div className="form-row">
        <div className="form-group"><label className="form-label">q₁ (C)</label>
          <input className="form-input" value={q1} onChange={e => setQ1(e.target.value)} /></div>
        <div className="form-group"><label className="form-label">q₂ (C)</label>
          <input className="form-input" value={q2} onChange={e => setQ2(e.target.value)} /></div>
        <div className="form-group"><label className="form-label">r (m)</label>
          <input className="form-input" value={r} onChange={e => setR(e.target.value)} type="number" /></div>
      </div>
      <div className="button-grid">
        <button className="btn btn-primary" onClick={() => run('coulomb')} disabled={loading}>⚡ Coulomb Force</button>
        <button className="btn btn-secondary" onClick={() => run('efield')} disabled={loading}>🌀 Electric Field</button>
      </div>

      <div className="divider" />
      <h3 className="section-title">Ohm's Law (V = IR) — Leave one blank</h3>
      <div className="form-row">
        {[['V (V)', V, setV], ['I (A)', I, setI], ['R (Ω)', R, setR2]].map(([label, val, setter]) => (
          <div key={label as string} className="form-group">
            <label className="form-label">{label as string}</label>
            <input className="form-input" value={val as string}
              onChange={e => (setter as (v: string) => void)(e.target.value)} type="number" placeholder="Leave blank to solve" />
          </div>
        ))}
      </div>
      <button className="btn btn-secondary" onClick={() => run('ohm')} disabled={loading}>🔌 Ohm's Law</button>

      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── Relativity Tab ────────────────────────────────────────────
function RelativityTab() {
  const [v, setV] = useState('2.4e8');
  const [t0, setT0] = useState('1');
  const [L0, setL0] = useState('1');
  const [m, setM] = useState('1');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async (action: string) => {
    setLoading(true); setError(''); setResult(null);
    try {
      let data;
      if (action === 'lorentz') data = await post('/lorentz-factor', { v: parseFloat(v) });
      else if (action === 'dilation') data = await post('/time-dilation', { t0: parseFloat(t0), v: parseFloat(v) });
      else if (action === 'contraction') data = await post('/length-contraction', { L0: parseFloat(L0), v: parseFloat(v) });
      else if (action === 'massenergy') data = await post('/mass-energy', { m: parseFloat(m) });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <div className="info-box">Special relativity (c = 299,792,458 m/s)</div>
      <div className="form-group">
        <label className="form-label">Velocity v (m/s)</label>
        <input className="form-input" value={v} onChange={e => setV(e.target.value)} />
      </div>
      <div className="form-row">
        <div className="form-group"><label className="form-label">Proper Time t₀ (s)</label>
          <input className="form-input" value={t0} onChange={e => setT0(e.target.value)} type="number" /></div>
        <div className="form-group"><label className="form-label">Rest Length L₀ (m)</label>
          <input className="form-input" value={L0} onChange={e => setL0(e.target.value)} type="number" /></div>
      </div>
      <div className="button-grid">
        <button className="btn btn-primary" onClick={() => run('lorentz')} disabled={loading}>γ Lorentz Factor</button>
        <button className="btn btn-primary" onClick={() => run('dilation')} disabled={loading}>⏰ Time Dilation</button>
        <button className="btn btn-primary" onClick={() => run('contraction')} disabled={loading}>📏 Length Contraction</button>
      </div>
      <div className="divider" />
      <div className="form-group"><label className="form-label">Mass m (kg)</label>
        <input className="form-input" value={m} onChange={e => setM(e.target.value)} type="number" /></div>
      <button className="btn btn-secondary" onClick={() => run('massenergy')} disabled={loading}>E = mc² Mass-Energy</button>

      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── Quantum Tab ────────────────────────────────────────────────
function QuantumTab() {
  const [mass, setMass] = useState('9.109e-31');
  const [vel, setVel] = useState('1e6');
  const [freq, setFreq] = useState('8e14');
  const [workFn, setWorkFn] = useState('4.7');
  const [deltaX, setDeltaX] = useState('1e-10');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async (action: string) => {
    setLoading(true); setError(''); setResult(null);
    try {
      let data;
      if (action === 'debroglie') data = await post('/de-broglie', { m: parseFloat(mass), v: parseFloat(vel) });
      else if (action === 'heisenberg') data = await post('/heisenberg', { delta_x: parseFloat(deltaX), delta_p: null });
      else if (action === 'photoelectric') data = await post('/photoelectric', { freq: parseFloat(freq), work_function_eV: parseFloat(workFn) });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <h3 className="section-title">de Broglie Wavelength λ = h/mv</h3>
      <div className="form-row">
        <div className="form-group"><label className="form-label">Mass (kg)</label>
          <input className="form-input" value={mass} onChange={e => setMass(e.target.value)} /></div>
        <div className="form-group"><label className="form-label">Velocity (m/s)</label>
          <input className="form-input" value={vel} onChange={e => setVel(e.target.value)} /></div>
      </div>
      <button className="btn btn-primary" onClick={() => run('debroglie')} disabled={loading}>λ de Broglie</button>

      <div className="divider" />
      <h3 className="section-title">Heisenberg Uncertainty Δx·Δp ≥ ℏ/2</h3>
      <div className="form-group"><label className="form-label">Δx (m)</label>
        <input className="form-input" value={deltaX} onChange={e => setDeltaX(e.target.value)} /></div>
      <button className="btn btn-secondary" onClick={() => run('heisenberg')} disabled={loading}>🔬 Heisenberg</button>

      <div className="divider" />
      <h3 className="section-title">Photoelectric Effect (KE = hf - φ)</h3>
      <div className="form-row">
        <div className="form-group"><label className="form-label">Frequency (Hz)</label>
          <input className="form-input" value={freq} onChange={e => setFreq(e.target.value)} /></div>
        <div className="form-group"><label className="form-label">Work Function (eV)</label>
          <input className="form-input" value={workFn} onChange={e => setWorkFn(e.target.value)} type="number" /></div>
      </div>
      <button className="btn btn-secondary" onClick={() => run('photoelectric')} disabled={loading}>☀️ Photoelectric</button>

      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── Gravity Tab ────────────────────────────────────────────────
function GravityTab() {
  const [M, setM] = useState('5.972e24');
  const [r, setR] = useState('6.371e6');
  const [m2, setM2] = useState('1000');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async (action: string) => {
    setLoading(true); setError(''); setResult(null);
    try {
      let data;
      if (action === 'force') data = await post('/gravity', { m1: parseFloat(M), m2: parseFloat(m2), r: parseFloat(r) });
      else if (action === 'orbital') data = await post('/orbital-velocity', { M: parseFloat(M), r: parseFloat(r) });
      else if (action === 'escape') data = await post('/escape-velocity', { M: parseFloat(M), r: parseFloat(r) });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <div className="info-box">Default values: Earth (M=5.972×10²⁴ kg, R=6.371×10⁶ m)</div>
      <div className="form-row">
        <div className="form-group"><label className="form-label">Central Mass M (kg)</label>
          <input className="form-input" value={M} onChange={e => setM(e.target.value)} /></div>
        <div className="form-group"><label className="form-label">Radius / Distance r (m)</label>
          <input className="form-input" value={r} onChange={e => setR(e.target.value)} /></div>
        <div className="form-group"><label className="form-label">Object Mass m₂ (kg)</label>
          <input className="form-input" value={m2} onChange={e => setM2(e.target.value)} /></div>
      </div>
      <div className="button-grid">
        <button className="btn btn-primary" onClick={() => run('force')} disabled={loading}>🌍 Gravitational Force</button>
        <button className="btn btn-primary" onClick={() => run('orbital')} disabled={loading}>🛸 Orbital Velocity</button>
        <button className="btn btn-secondary" onClick={() => run('escape')} disabled={loading}>🚀 Escape Velocity</button>
      </div>
      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── Waves Tab ──────────────────────────────────────────────────
function WavesTab() {
  const [wv, setWv] = useState('');
  const [wf, setWf] = useState('440');
  const [wl, setWl] = useState('0.7727');
  const [fSrc, setFSrc] = useState('440');
  const [vSnd, setVSnd] = useState('343');
  const [vObs, setVObs] = useState('10');
  const [result, setResult] = useState<object | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const run = async (action: string) => {
    setLoading(true); setError(''); setResult(null);
    try {
      let data;
      if (action === 'wave') data = await post('/wave', {
        v: wv ? parseFloat(wv) : null,
        f: wf ? parseFloat(wf) : null,
        lamda: wl ? parseFloat(wl) : null
      });
      else if (action === 'doppler') data = await post('/doppler', {
        f_source: parseFloat(fSrc),
        v_sound: parseFloat(vSnd),
        v_observer: parseFloat(vObs)
      });
      setResult(data);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Unknown error');
    }
    setLoading(false);
  };

  return (
    <div className="tab-content">
      <h3 className="section-title">Wave Equation v = fλ — Leave one blank</h3>
      <div className="form-row">
        {[['Speed v (m/s)', wv, setWv], ['Frequency f (Hz)', wf, setWf], ['Wavelength λ (m)', wl, setWl]].map(([label, val, setter]) => (
          <div key={label as string} className="form-group">
            <label className="form-label">{label as string}</label>
            <input className="form-input" value={val as string}
              onChange={e => (setter as (v: string) => void)(e.target.value)} type="number" placeholder="Leave blank to solve" />
          </div>
        ))}
      </div>
      <button className="btn btn-primary" onClick={() => run('wave')} disabled={loading}>🌊 Solve Wave</button>

      <div className="divider" />
      <h3 className="section-title">Doppler Effect</h3>
      <div className="form-row">
        {[['Source Freq (Hz)', fSrc, setFSrc], ['Sound Speed (m/s)', vSnd, setVSnd], ['Observer Speed (m/s)', vObs, setVObs]].map(([label, val, setter]) => (
          <div key={label as string} className="form-group">
            <label className="form-label">{label as string}</label>
            <input className="form-input" value={val as string}
              onChange={e => (setter as (v: string) => void)(e.target.value)} type="number" />
          </div>
        ))}
      </div>
      <button className="btn btn-secondary" onClick={() => run('doppler')} disabled={loading}>📡 Doppler Shift</button>

      {error && <div className="error-box">{error}</div>}
      {loading && <div className="loading">Computing...</div>}
      <ResultBox data={result} />
    </div>
  );
}

// ── Main Component ────────────────────────────────────────────
export default function PhysicsSandbox() {
  const [activeTab, setActiveTab] = useState<TabId>('mechanics');

  const TAB_COMPONENTS: Record<TabId, React.ReactNode> = {
    mechanics:      <MechanicsTab />,
    thermodynamics: <ThermodynamicsTab />,
    electrostatics: <ElectrostaticsTab />,
    relativity:     <RelativityTab />,
    quantum:        <QuantumTab />,
    gravity:        <GravityTab />,
    waves:          <WavesTab />,
  };

  return (
    <div className="lab-container">
      <div className="lab-header">
        <div className="lab-header-icon">
          <Atom size={28} />
        </div>
        <div>
          <h1 className="lab-title">Physics Sandbox</h1>
          <p className="lab-subtitle">
            Mechanics, Thermodynamics, Electrostatics, Special Relativity, Quantum Mechanics, Gravity, Waves
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
