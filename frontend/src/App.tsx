import { useState, useEffect } from 'react'
import './App.css'
import { SymbolicCalculator } from './features/SymbolicCalculator'
import { EquationSolver } from './features/EquationSolver'
import { CalculusLab } from './features/CalculusLab'
import { MatrixLab } from './features/MatrixLab'
import { NotebookLab } from './features/NotebookLab'
import { PlottingStudio } from './features/PlottingStudio'
import { ProjectManager } from './features/ProjectManager'
import NumberTheoryLab from './features/NumberTheoryLab'
import PhysicsSandbox from './features/PhysicsSandbox'
import {
  LayoutDashboard, Function, PenTool, Sigma, Grid2X2,
  BookOpen, BarChart2, FolderOpen, Hash, Atom,
  ChevronRight, Wifi, WifiOff
} from 'lucide-react'

type TabId =
  | 'dashboard' | 'symbolic' | 'equation' | 'calculus'
  | 'matrix' | 'notebook' | 'plotting' | 'projects'
  | 'number_theory' | 'physics'

interface NavItem { id: TabId; label: string; icon: React.ReactNode; group: string; }

const NAV_ITEMS: NavItem[] = [
  { id: 'dashboard',     label: 'Dashboard',         icon: <LayoutDashboard size={16}/>, group: 'General' },
  { id: 'projects',      label: 'Projects',          icon: <FolderOpen size={16}/>,      group: 'General' },
  { id: 'symbolic',      label: 'Symbolic CAS',      icon: <Function size={16}/>,        group: 'Algebra' },
  { id: 'equation',      label: 'Equation Solver',   icon: <PenTool size={16}/>,         group: 'Algebra' },
  { id: 'matrix',        label: 'Matrix Lab',        icon: <Grid2X2 size={16}/>,         group: 'Algebra' },
  { id: 'calculus',      label: 'Calculus Lab',      icon: <Sigma size={16}/>,           group: 'Analysis' },
  { id: 'plotting',      label: 'Plotting Studio',   icon: <BarChart2 size={16}/>,       group: 'Analysis' },
  { id: 'notebook',      label: 'Notebook',          icon: <BookOpen size={16}/>,        group: 'Analysis' },
  { id: 'number_theory', label: 'Number Theory',     icon: <Hash size={16}/>,            group: 'Science' },
  { id: 'physics',       label: 'Physics Sandbox',   icon: <Atom size={16}/>,            group: 'Science' },
]

const GROUPS = ['General', 'Algebra', 'Analysis', 'Science']

const DASHBOARD_CARDS = [
  { id: 'symbolic',      title: 'Symbolic CAS',     desc: 'Simplify, factor, expand, integrate, differentiate algebraic expressions.',   color: '#3b82f6', icon: '∑' },
  { id: 'equation',      title: 'Equation Solver',  desc: 'Solve polynomial, transcendental, and systems of equations symbolically.',    color: '#10b981', icon: '=' },
  { id: 'matrix',        title: 'Matrix Lab',       desc: 'Determinants, eigenvalues, SVD, LU decomposition, and more.',                 color: '#f59e0b', icon: '⊞' },
  { id: 'calculus',      title: 'Calculus Lab',     desc: 'Limits, derivatives, integrals, Taylor series, and convergence analysis.',    color: '#8b5cf6', icon: '∂' },
  { id: 'plotting',      title: 'Plotting Studio',  desc: 'Interactive 2D/3D plots, parametric curves, and function visualization.',    color: '#ec4899', icon: '📈' },
  { id: 'notebook',      title: 'Notebook Engine',  desc: 'Jupyter-like cells — execute Python, Markdown, and math in sequence.',       color: '#06b6d4', icon: '📓' },
  { id: 'number_theory', title: 'Number Theory',    desc: 'Primes, GCD/LCM, modular arithmetic, CRT, Diophantine equations, and more.', color: '#f97316', icon: '#' },
  { id: 'physics',       title: 'Physics Sandbox',  desc: 'Mechanics, thermodynamics, relativity, quantum mechanics, and optics.',      color: '#ef4444', icon: '⚛' },
  { id: 'projects',      title: 'Projects',         desc: 'Organize, save, and resume your mathematical experiments and workspaces.',   color: '#64748b', icon: '📁' },
]

function App() {
  const [status, setStatus] = useState<'running' | 'offline' | 'loading'>('loading')
  const [activeTab, setActiveTab] = useState<TabId>('dashboard')
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false)

  useEffect(() => {
    const check = () => {
      fetch('http://127.0.0.1:8000/api/status')
        .then(res => res.json())
        .then(data => setStatus(data.status === 'running' ? 'running' : 'offline'))
        .catch(() => setStatus('offline'))
    }
    check()
    const id = setInterval(check, 15000)
    return () => clearInterval(id)
  }, [])

  return (
    <div className="app-shell">
      {/* Sidebar */}
      <aside className={`sidebar ${sidebarCollapsed ? 'sidebar-collapsed' : ''}`}>
        <div className="sidebar-header">
          {!sidebarCollapsed && (
            <div className="logo-area">
              <span className="logo-icon">∀</span>
              <div>
                <div className="logo-name">MathForge</div>
                <div className="logo-version">v2.0 · Offline Platform</div>
              </div>
            </div>
          )}
          <button className="collapse-btn" onClick={() => setSidebarCollapsed(!sidebarCollapsed)}
            title={sidebarCollapsed ? 'Expand' : 'Collapse'}>
            <ChevronRight size={16} style={{ transform: sidebarCollapsed ? 'none' : 'rotate(180deg)', transition: 'transform 0.2s' }} />
          </button>
        </div>

        <nav className="sidebar-nav">
          {GROUPS.map(group => (
            <div key={group} className="nav-group">
              {!sidebarCollapsed && <div className="nav-group-label">{group}</div>}
              {NAV_ITEMS.filter(item => item.group === group).map(item => (
                <button
                  key={item.id}
                  className={`nav-item ${activeTab === item.id ? 'nav-item-active' : ''}`}
                  onClick={() => setActiveTab(item.id)}
                  title={sidebarCollapsed ? item.label : undefined}
                >
                  <span className="nav-item-icon">{item.icon}</span>
                  {!sidebarCollapsed && <span className="nav-item-label">{item.label}</span>}
                </button>
              ))}
            </div>
          ))}
        </nav>

        <div className="sidebar-footer">
          {status === 'running' ? (
            <div className="status-badge status-online">
              <Wifi size={12} />
              {!sidebarCollapsed && <span>API Online</span>}
            </div>
          ) : status === 'offline' ? (
            <div className="status-badge status-offline">
              <WifiOff size={12} />
              {!sidebarCollapsed && <span>API Offline</span>}
            </div>
          ) : (
            <div className="status-badge status-loading">
              {!sidebarCollapsed && <span>Connecting...</span>}
            </div>
          )}
        </div>
      </aside>

      {/* Main Content */}
      <main className="main-content">
        {activeTab === 'dashboard' && (
          <div className="dashboard">
            <div className="dashboard-hero">
              <h1 className="dashboard-title">Welcome to <span className="gradient-text">MathForge</span></h1>
              <p className="dashboard-subtitle">
                Offline-first Computer Algebra, Numerical Computing & Scientific Experimentation Platform.
                Select a module below to get started.
              </p>
              <div className={`api-status-banner ${status === 'running' ? 'api-online' : 'api-offline'}`}>
                {status === 'running' ? (
                  <><Wifi size={14} /> API Server Running · All engines operational</>
                ) : (
                  <><WifiOff size={14} /> API Server Offline · Start backend: scripts/run_backend.ps1</>
                )}
              </div>
            </div>

            <div className="dashboard-grid">
              {DASHBOARD_CARDS.map(card => (
                <div
                  key={card.id}
                  className="dashboard-card"
                  onClick={() => setActiveTab(card.id as TabId)}
                  style={{ '--card-color': card.color } as React.CSSProperties}
                >
                  <div className="card-icon">{card.icon}</div>
                  <div className="card-body">
                    <h3 className="card-title">{card.title}</h3>
                    <p className="card-desc">{card.desc}</p>
                  </div>
                  <div className="card-arrow">→</div>
                </div>
              ))}
            </div>

            <div className="dashboard-stats">
              <div className="stat-item"><span className="stat-value">9M+</span><span className="stat-label">Lines of Code</span></div>
              <div className="stat-item"><span className="stat-value">9</span><span className="stat-label">Math Engines</span></div>
              <div className="stat-item"><span className="stat-value">200+</span><span className="stat-label">API Endpoints</span></div>
              <div className="stat-item"><span className="stat-value">∞</span><span className="stat-label">Offline · Always Fast</span></div>
            </div>
          </div>
        )}

        {activeTab === 'symbolic'      && <div className="feature-wrapper"><SymbolicCalculator /></div>}
        {activeTab === 'equation'      && <div className="feature-wrapper"><EquationSolver /></div>}
        {activeTab === 'calculus'      && <div className="feature-wrapper"><CalculusLab /></div>}
        {activeTab === 'matrix'        && <div className="feature-wrapper"><MatrixLab /></div>}
        {activeTab === 'notebook'      && <div className="feature-wrapper feature-tall"><NotebookLab /></div>}
        {activeTab === 'plotting'      && <div className="feature-wrapper feature-tall"><PlottingStudio /></div>}
        {activeTab === 'projects'      && <div className="feature-wrapper feature-tall"><ProjectManager /></div>}
        {activeTab === 'number_theory' && <NumberTheoryLab />}
        {activeTab === 'physics'       && <PhysicsSandbox />}
      </main>
    </div>
  )
}

export default App
