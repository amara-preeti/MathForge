[feature/symbolic-engine-core] feat(symbolic): add expression parser and tokenizer
[feature/symbolic-engine-core] feat(symbolic): implement AST node hierarchy
[feature/symbolic-engine-core] feat(symbolic): add algebraic simplification rules
[feature/symbolic-engine-core] feat(symbolic): implement symbolic differentiation
[feature/symbolic-engine-core] feat(symbolic): add pattern matching for expressions
[feature/symbolic-engine-core] test(symbolic): add unit tests for parser
[feature/symbolic-engine-core] fix(symbolic): fix operator precedence in parser
[feature/symbolic-engine-core] docs(symbolic): add API documentation for symbolic engine
[feature/symbolic-engine-integration] feat(symbolic): add LaTeX output formatter
[feature/symbolic-engine-integration] feat(symbolic): add MathML output support
[feature/symbolic-engine-integration] feat(symbolic): implement symbolic integration via parts
[feature/symbolic-engine-integration] fix(symbolic): handle edge case in trigonometric simplification
[feature/symbolic-engine-integration] refactor(symbolic): extract common subexpression elimination
[feature/matrix-engine-core] feat(matrix): implement dense matrix operations
[feature/matrix-engine-core] feat(matrix): add sparse matrix support with CSR format
[feature/matrix-engine-core] feat(matrix): implement LU decomposition
[feature/matrix-engine-core] feat(matrix): add QR decomposition with Householder reflections
[feature/matrix-engine-core] feat(matrix): implement eigenvalue computation (QR algorithm)
[feature/matrix-engine-core] test(matrix): add comprehensive matrix operation tests
[feature/matrix-engine-core] perf(matrix): optimize matrix multiplication with BLAS-style blocking
[feature/matrix-advanced] feat(matrix): add SVD decomposition
[feature/matrix-advanced] feat(matrix): implement Cholesky decomposition
[feature/matrix-advanced] feat(matrix): add matrix norm computations
[feature/matrix-advanced] feat(matrix): implement pseudoinverse via SVD
[feature/matrix-advanced] fix(matrix): fix numerical stability in LU with partial pivoting
[feature/calculus-engine] feat(calculus): implement numerical differentiation (finite differences)
[feature/calculus-engine] feat(calculus): add adaptive Gaussian quadrature
[feature/calculus-engine] feat(calculus): implement Romberg integration
[feature/calculus-engine] feat(calculus): add ODE solvers (RK4, RK45)
[feature/calculus-engine] feat(calculus): implement symbolic limit computation
[feature/calculus-engine] test(calculus): add integration accuracy benchmarks
[feature/calculus-engine] docs(calculus): document numerical methods and error bounds
[feature/calculus-multivariable] feat(calculus): add partial derivative computation
[feature/calculus-multivariable] feat(calculus): implement gradient and Hessian
[feature/calculus-multivariable] feat(calculus): add double and triple integral support
[feature/calculus-multivariable] feat(calculus): implement divergence and curl operators
[feature/calculus-multivariable] fix(calculus): fix singularity handling in adaptive quadrature
[feature/numerical-engine] feat(numerical): implement Newton-Raphson root finding
[feature/numerical-engine] feat(numerical): add bisection and secant methods
[feature/numerical-engine] feat(numerical): implement Brent's method for robust root finding
[feature/numerical-engine] feat(numerical): add polynomial root finding (companion matrix)
[feature/numerical-engine] test(numerical): add root finding convergence tests
[feature/numerical-interpolation] feat(numerical): add Lagrange interpolation
[feature/numerical-interpolation] feat(numerical): implement cubic spline interpolation
[feature/numerical-interpolation] feat(numerical): add Chebyshev interpolation nodes
[feature/numerical-interpolation] feat(numerical): implement barycentric rational interpolation
[feature/numerical-interpolation] docs(numerical): document interpolation accuracy and stability
[feature/statistics-engine] feat(stats): implement descriptive statistics (mean, variance, skewness, kurtosis)
[feature/statistics-engine] feat(stats): add probability distributions (normal, binomial, Poisson)
[feature/statistics-engine] feat(stats): implement hypothesis testing (t-test, chi-squared, ANOVA)
[feature/statistics-engine] feat(stats): add linear regression with OLS and WLS
[feature/statistics-engine] feat(stats): implement bootstrap confidence intervals
[feature/statistics-engine] test(stats): add statistical correctness tests against known datasets
[feature/statistics-engine] docs(stats): add statistical methods documentation
[feature/statistics-advanced] feat(stats): add Bayesian inference engine
[feature/statistics-advanced] feat(stats): implement MCMC sampling (Metropolis-Hastings)
[feature/statistics-advanced] feat(stats): add time series analysis (ARIMA)
[feature/statistics-advanced] feat(stats): implement PCA and factor analysis
[feature/statistics-advanced] fix(stats): fix numerical issue in log-likelihood computation
[feature/probability-engine] feat(prob): implement continuous distribution framework
[feature/probability-engine] feat(prob): add discrete distribution framework
[feature/probability-engine] feat(prob): implement joint and conditional distributions
[feature/probability-engine] feat(prob): add Monte Carlo simulation engine
[feature/probability-engine] feat(prob): implement Markov chain analysis
[feature/probability-engine] test(prob): add distribution moment verification tests
[feature/probability-advanced] feat(prob): add stochastic process simulation
[feature/probability-advanced] feat(prob): implement Brownian motion and diffusion
[feature/probability-advanced] feat(prob): add copula functions for dependency modeling
[feature/probability-advanced] fix(prob): fix CDF inversion for heavy-tailed distributions
[feature/geometry-engine] feat(geo): implement 2D geometric primitives
[feature/geometry-engine] feat(geo): add 3D geometric objects
[feature/geometry-engine] feat(geo): implement computational geometry algorithms
[feature/geometry-engine] feat(geo): add convex hull computation (QuickHull)
[feature/geometry-engine] feat(geo): implement Voronoi diagram generation
[feature/geometry-engine] test(geo): add geometric algorithm correctness tests
[feature/geometry-transformations] feat(geo): add affine transformations (rotation, scaling, shear)
[feature/geometry-transformations] feat(geo): implement projective transformations
[feature/geometry-transformations] feat(geo): add coordinate system conversions
[feature/geometry-transformations] feat(geo): implement geodesic computations on sphere
[feature/geometry-transformations] docs(geo): document geometry engine API
[feature/graph-engine] feat(graph): implement adjacency list and matrix representations
[feature/graph-engine] feat(graph): add BFS and DFS traversal algorithms
[feature/graph-engine] feat(graph): implement Dijkstra's shortest path algorithm
[feature/graph-engine] feat(graph): add A* pathfinding algorithm
[feature/graph-engine] feat(graph): implement minimum spanning tree (Kruskal, Prim)
[feature/graph-engine] test(graph): add graph algorithm tests on benchmark graphs
[feature/graph-advanced] feat(graph): add topological sort
[feature/graph-advanced] feat(graph): implement strongly connected components (Tarjan)
[feature/graph-advanced] feat(graph): add max flow (Ford-Fulkerson, Dinic)
[feature/graph-advanced] feat(graph): implement graph coloring algorithms
[feature/graph-advanced] feat(graph): add spectral graph theory computations
[feature/optimization-engine] feat(opt): implement gradient descent variants (SGD, Adam, RMSProp)
[feature/optimization-engine] feat(opt): add conjugate gradient method
[feature/optimization-engine] feat(opt): implement L-BFGS quasi-Newton method
[feature/optimization-engine] feat(opt): add linear programming solver (simplex method)
[feature/optimization-engine] feat(opt): implement interior point method for LP
[feature/optimization-engine] test(opt): add optimization convergence tests
[feature/optimization-advanced] feat(opt): add convex programming (CVXPY-style)
[feature/optimization-advanced] feat(opt): implement genetic algorithm optimizer
[feature/optimization-advanced] feat(opt): add simulated annealing
[feature/optimization-advanced] feat(opt): implement particle swarm optimization
[feature/optimization-advanced] docs(opt): document optimization algorithms and use cases
[feature/equation-engine] feat(eq): implement linear system solver (Gaussian elimination)
[feature/equation-engine] feat(eq): add iterative solvers (Jacobi, Gauss-Seidel, SOR)
[feature/equation-engine] feat(eq): implement polynomial arithmetic and GCD
[feature/equation-engine] feat(eq): add Diophantine equation solver
[feature/equation-engine] feat(eq): implement differential equation classifier
[feature/equation-symbolic] feat(eq): add symbolic equation solver
[feature/equation-symbolic] feat(eq): implement system of equations solver
[feature/equation-symbolic] feat(eq): add inequality solver
[feature/equation-symbolic] fix(eq): fix rational root theorem implementation
[feature/plotting-engine] feat(plot): implement SVG-based 2D plotting engine
[feature/plotting-engine] feat(plot): add line, scatter, bar, and histogram plots
[feature/plotting-engine] feat(plot): implement 3D surface and wireframe plots
[feature/plotting-engine] feat(plot): add contour and heatmap visualization
[feature/plotting-engine] feat(plot): implement interactive plot controls
[feature/plotting-engine] test(plot): add visual regression tests for plots
[feature/plotting-advanced] feat(plot): add animated plot support
[feature/plotting-advanced] feat(plot): implement polar and complex plane plots
[feature/plotting-advanced] feat(plot): add parametric curve plotting
[feature/plotting-advanced] feat(plot): implement vector field visualization
[feature/plotting-advanced] fix(plot): fix axis label overlap in dense plots
[feature/notebook-engine] feat(notebook): implement cell-based execution model
[feature/notebook-engine] feat(notebook): add Python kernel integration
[feature/notebook-engine] feat(notebook): implement Markdown cell rendering
[feature/notebook-engine] feat(notebook): add cell output caching
[feature/notebook-engine] feat(notebook): implement notebook export (HTML, PDF, LaTeX)
[feature/notebook-engine] test(notebook): add notebook execution tests
[feature/notebook-collaboration] feat(notebook): add real-time collaboration via WebSockets
[feature/notebook-collaboration] feat(notebook): implement conflict resolution for concurrent edits
[feature/notebook-collaboration] feat(notebook): add version history for notebooks
[feature/notebook-collaboration] fix(notebook): fix race condition in cell execution order
[feature/dataset-engine] feat(dataset): implement CSV and JSON data loading
[feature/dataset-engine] feat(dataset): add Parquet and Arrow format support
[feature/dataset-engine] feat(dataset): implement data cleaning pipeline
[feature/dataset-engine] feat(dataset): add data transformation DSL
[feature/dataset-engine] feat(dataset): implement lazy evaluation for large datasets
[feature/dataset-engine] test(dataset): add data pipeline integration tests
[feature/dataset-advanced] feat(dataset): add SQL query interface over datasets
[feature/dataset-advanced] feat(dataset): implement data profiling and summary stats
[feature/dataset-advanced] feat(dataset): add missing value imputation strategies
[feature/dataset-advanced] fix(dataset): fix memory leak in large dataset streaming
[feature/export-engine] feat(export): implement PDF export via LaTeX backend
[feature/export-engine] feat(export): add HTML export with embedded plots
[feature/export-engine] feat(export): implement Jupyter notebook export
[feature/export-engine] feat(export): add Word/DOCX export
[feature/export-engine] feat(export): implement MATLAB .m file export
[feature/plugin-engine] feat(plugin): implement plugin discovery and loading
[feature/plugin-engine] feat(plugin): add plugin sandboxing with restricted execution
[feature/plugin-engine] feat(plugin): implement plugin API versioning
[feature/plugin-engine] feat(plugin): add plugin marketplace integration
[feature/plugin-engine] test(plugin): add plugin lifecycle tests
[feature/number-theory] feat(numth): implement prime number generation (Sieve of Eratosthenes)
[feature/number-theory] feat(numth): add primality testing (Miller-Rabin)
[feature/number-theory] feat(numth): implement integer factorization (Pollard rho)
[feature/number-theory] feat(numth): add modular arithmetic operations
[feature/number-theory] feat(numth): implement RSA key generation for cryptography module
[feature/number-theory] feat(numth): add continued fraction expansion
[feature/number-theory] test(numth): add number theory algorithm tests
[feature/number-theory-advanced] feat(numth): add Euler's totient function
[feature/number-theory-advanced] feat(numth): implement Mobius function and inversion
[feature/number-theory-advanced] feat(numth): add quadratic sieve for large factorization
[feature/number-theory-advanced] feat(numth): implement elliptic curve point operations
[feature/number-theory-advanced] docs(numth): document number theory module
[feature/signal-processing] feat(signal): implement FFT (Cooley-Tukey algorithm)
[feature/signal-processing] feat(signal): add windowing functions (Hamming, Hann, Blackman)
[feature/signal-processing] feat(signal): implement FIR and IIR filter design
[feature/signal-processing] feat(signal): add spectrogram computation
[feature/signal-processing] feat(signal): implement wavelet transform (DWT, CWT)
[feature/signal-processing] test(signal): add signal processing accuracy tests
[feature/signal-advanced] feat(signal): add noise reduction algorithms
[feature/signal-advanced] feat(signal): implement Hilbert transform
[feature/signal-advanced] feat(signal): add convolution and correlation
[feature/signal-advanced] feat(signal): implement Z-transform computation
[feature/signal-advanced] fix(signal): fix aliasing artifact in downsampling
[feature/ml-engine] feat(ml): implement linear and logistic regression
[feature/ml-engine] feat(ml): add decision tree with pruning
[feature/ml-engine] feat(ml): implement Random Forest classifier and regressor
[feature/ml-engine] feat(ml): add Support Vector Machine (SVM) with kernel trick
[feature/ml-engine] feat(ml): implement K-Means and DBSCAN clustering
[feature/ml-engine] feat(ml): add neural network layers (Dense, Conv, RNN)
[feature/ml-engine] test(ml): add ML model accuracy tests on standard datasets
[feature/ml-deep-learning] feat(ml): implement backpropagation with automatic differentiation
[feature/ml-deep-learning] feat(ml): add Adam, SGD, and RMSProp optimizers
[feature/ml-deep-learning] feat(ml): implement batch normalization
[feature/ml-deep-learning] feat(ml): add dropout regularization
[feature/ml-deep-learning] feat(ml): implement convolutional neural network training
[feature/physics-engine] feat(physics): implement classical mechanics simulation
[feature/physics-engine] feat(physics): add rigid body dynamics
[feature/physics-engine] feat(physics): implement electromagnetic field simulation
[feature/physics-engine] feat(physics): add quantum mechanics operators
[feature/physics-engine] feat(physics): implement thermodynamics computations
[feature/physics-engine] test(physics): add physics simulation validation tests
[feature/physics-quantum] feat(physics): add Schrodinger equation solver
[feature/physics-quantum] feat(physics): implement quantum gate simulation
[feature/physics-quantum] feat(physics): add quantum circuit visualization
[feature/physics-quantum] fix(physics): fix normalization in wavefunction computation
[feature/frontend-dashboard] feat(ui): implement main dashboard layout
[feature/frontend-dashboard] feat(ui): add engine selector sidebar
[feature/frontend-dashboard] feat(ui): implement recent computations panel
[feature/frontend-dashboard] feat(ui): add quick action buttons
[feature/frontend-dashboard] fix(ui): fix responsive layout on mobile viewports
[feature/frontend-symbolic-ui] feat(ui): add symbolic math input editor
[feature/frontend-symbolic-ui] feat(ui): implement LaTeX preview for expressions
[feature/frontend-symbolic-ui] feat(ui): add expression tree visualizer
[feature/frontend-symbolic-ui] feat(ui): implement step-by-step solution display
[feature/frontend-matrix-ui] feat(ui): implement matrix input grid component
[feature/frontend-matrix-ui] feat(ui): add matrix operation palette
[feature/frontend-matrix-ui] feat(ui): implement matrix visualization (heatmap)
[feature/frontend-matrix-ui] feat(ui): add eigenvalue/eigenvector display
[feature/frontend-calculus-ui] feat(ui): implement function input with LaTeX preview
[feature/frontend-calculus-ui] feat(ui): add integral bounds UI
[feature/frontend-calculus-ui] feat(ui): implement ODE initial conditions form
[feature/frontend-calculus-ui] feat(ui): add calculus result visualization
[feature/frontend-stats-ui] feat(ui): implement data input table
[feature/frontend-stats-ui] feat(ui): add statistical test selector
[feature/frontend-stats-ui] feat(ui): implement results dashboard with charts
[feature/frontend-stats-ui] feat(ui): add hypothesis test interpretation panel
[feature/frontend-plot-ui] feat(ui): implement interactive plot canvas
[feature/frontend-plot-ui] feat(ui): add plot customization panel
[feature/frontend-plot-ui] feat(ui): implement zoom and pan controls
[feature/frontend-plot-ui] feat(ui): add data export for plot data
[feature/frontend-notebook-ui] feat(ui): implement notebook cell editor (CodeMirror)
[feature/frontend-notebook-ui] feat(ui): add cell execution controls
[feature/frontend-notebook-ui] feat(ui): implement output rendering for plots and tables
[feature/frontend-notebook-ui] feat(ui): add notebook toolbar and menu
[feature/frontend-settings] feat(ui): implement user preferences panel
[feature/frontend-settings] feat(ui): add theme switcher (light/dark/high-contrast)
[feature/frontend-settings] feat(ui): implement engine configuration settings
[feature/frontend-settings] feat(ui): add keyboard shortcut customization
[feature/backend-api-symbolic] feat(api): wire symbolic engine to /api/symbolic router
[feature/backend-api-symbolic] feat(api): add expression simplification endpoint
[feature/backend-api-symbolic] feat(api): add symbolic differentiation endpoint
[feature/backend-api-symbolic] feat(api): add symbolic integration endpoint
[feature/backend-api-symbolic] test(api): add API integration tests for symbolic routes
[feature/backend-api-matrix] feat(api): wire matrix engine to /api/matrix router
[feature/backend-api-matrix] feat(api): add matrix decomposition endpoints
[feature/backend-api-matrix] feat(api): add eigenvalue endpoint
[feature/backend-api-matrix] test(api): add API integration tests for matrix routes
[feature/backend-api-calculus] feat(api): wire calculus engine to /api/calculus router
[feature/backend-api-calculus] feat(api): add numerical integration endpoint
[feature/backend-api-calculus] feat(api): add ODE solver endpoint
[feature/backend-api-calculus] test(api): add calculus API tests
[feature/backend-api-stats] feat(api): wire statistics engine to /api/stats router
[feature/backend-api-stats] feat(api): add hypothesis testing endpoint
[feature/backend-api-stats] feat(api): add regression endpoint
[feature/backend-api-stats] test(api): add statistics API tests
[feature/backend-api-ml] feat(api): wire ML engine to /api/ml router
[feature/backend-api-ml] feat(api): add model training endpoint
[feature/backend-api-ml] feat(api): add model inference endpoint
[feature/backend-api-ml] feat(api): add model evaluation metrics endpoint
[feature/backend-api-ml] test(api): add ML API integration tests
[feature/backend-auth] feat(auth): implement JWT authentication
[feature/backend-auth] feat(auth): add OAuth2 provider support
[feature/backend-auth] feat(auth): implement role-based access control
[feature/backend-auth] feat(auth): add API key management
[feature/backend-auth] test(auth): add authentication flow tests
[feature/backend-caching] feat(cache): implement Redis-based result caching
[feature/backend-caching] feat(cache): add cache invalidation strategies
[feature/backend-caching] feat(cache): implement computation memoization
[feature/backend-caching] perf(cache): optimize cache key generation
[feature/backend-workers] feat(worker): implement Celery task queue for heavy computations
[feature/backend-workers] feat(worker): add computation progress tracking
[feature/backend-workers] feat(worker): implement worker auto-scaling
[feature/backend-workers] ops(worker): add worker health monitoring
[feature/ci-cd-pipeline] ci: add GitHub Actions workflow for Python backend
[feature/ci-cd-pipeline] ci: add frontend build and test workflow
[feature/ci-cd-pipeline] ci: implement automated integration testing
[feature/ci-cd-pipeline] ci: add code coverage reporting
[feature/ci-cd-pipeline] ci: implement semantic versioning with release automation
[feature/documentation] docs: add comprehensive README with installation guide
[feature/documentation] docs: add API reference documentation
[feature/documentation] docs: add developer contributing guide
[feature/documentation] docs: add mathematical algorithm documentation
[feature/documentation] docs: add architecture decision records (ADRs)
[feature/performance-profiling] perf: profile and optimize symbolic engine hot paths
[feature/performance-profiling] perf: optimize matrix operations with NumPy vectorization
[feature/performance-profiling] perf: implement lazy evaluation for symbolic expressions
[feature/performance-profiling] perf: add computation time budgeting
[feature/performance-profiling] benchmark: add performance benchmarks for all engines
[feature/security-hardening] security: implement input sanitization for all endpoints
[feature/security-hardening] security: add rate limiting middleware
[feature/security-hardening] security: implement CORS policy
[feature/security-hardening] security: add SQL injection prevention
[feature/security-hardening] security: implement CSP headers
[feature/testing-infrastructure] test: set up pytest with fixtures and conftest
[feature/testing-infrastructure] test: add property-based testing with Hypothesis
[feature/testing-infrastructure] test: implement visual regression tests
[feature/testing-infrastructure] test: add load testing with Locust
[feature/testing-infrastructure] test: set up test coverage requirements
[feature/monitoring-observability] ops: add Prometheus metrics endpoint
[feature/monitoring-observability] ops: implement structured logging with structlog
[feature/monitoring-observability] ops: add distributed tracing with OpenTelemetry
[feature/monitoring-observability] ops: implement health check endpoints
[feature/monitoring-observability] ops: add Grafana dashboard configuration
[feature/database-layer] feat(db): implement SQLAlchemy models for computation history
[feature/database-layer] feat(db): add Alembic migration setup
[feature/database-layer] feat(db): implement user session storage
[feature/database-layer] feat(db): add dataset metadata persistence
[feature/database-layer] test(db): add database integration tests
[feature/websocket-realtime] feat(ws): implement WebSocket connection manager
[feature/websocket-realtime] feat(ws): add real-time computation progress streaming
[feature/websocket-realtime] feat(ws): implement collaborative session protocol
[feature/websocket-realtime] fix(ws): fix WebSocket reconnection handling
[feature/internationalization] i18n: add i18n framework setup
[feature/internationalization] i18n: add English locale strings
[feature/internationalization] i18n: add Spanish locale translations
[feature/internationalization] i18n: add French locale translations
[feature/internationalization] i18n: add right-to-left layout support
[feature/accessibility] a11y: add ARIA labels to all interactive elements
[feature/accessibility] a11y: implement keyboard navigation throughout UI
[feature/accessibility] a11y: add screen reader support for math output
[feature/accessibility] a11y: implement high-contrast color mode
[feature/accessibility] a11y: add focus management for modal dialogs
[feature/mobile-responsive] feat(ui): implement responsive grid layout
[feature/mobile-responsive] feat(ui): add touch-friendly controls
[feature/mobile-responsive] feat(ui): implement mobile navigation drawer
[feature/mobile-responsive] feat(ui): optimize plot rendering for small screens
[feature/pwa-support] feat(pwa): add Service Worker for offline support
[feature/pwa-support] feat(pwa): implement progressive web app manifest
[feature/pwa-support] feat(pwa): add offline computation caching
[feature/pwa-support] feat(pwa): implement background sync for queued computations
[feature/docker-deployment] ops: add multi-stage Docker build for backend
[feature/docker-deployment] ops: add nginx-based frontend Docker image
[feature/docker-deployment] ops: implement docker-compose for local development
[feature/docker-deployment] ops: add Kubernetes deployment manifests
[feature/docker-deployment] ops: add Helm chart for production deployment
[feature/cloud-storage] feat(storage): add S3-compatible storage backend
[feature/cloud-storage] feat(storage): implement dataset upload/download
[feature/cloud-storage] feat(storage): add notebook cloud sync
[feature/cloud-storage] feat(storage): implement large file chunked upload
[feature/sharing-collaboration] feat(share): implement shareable computation links
[feature/sharing-collaboration] feat(share): add notebook sharing with access control
[feature/sharing-collaboration] feat(share): implement public gallery for computations
[feature/sharing-collaboration] feat(share): add embed mode for iframes
[feature/expression-editor] feat(editor): implement math expression editor
[feature/expression-editor] feat(editor): add autocomplete for math functions
[feature/expression-editor] feat(editor): implement syntax highlighting for MathForge DSL
[feature/expression-editor] feat(editor): add bracket matching and auto-close
[feature/expression-editor] fix(editor): fix cursor position after auto-complete insertion
[feature/computation-history] feat(history): implement computation history storage
[feature/computation-history] feat(history): add history search and filter
[feature/computation-history] feat(history): implement favorites/bookmarks
[feature/computation-history] feat(history): add computation replay functionality
[feature/error-handling] feat(error): implement structured error response format
[feature/error-handling] feat(error): add user-friendly error messages
[feature/error-handling] feat(error): implement error boundary components in React
[feature/error-handling] feat(error): add computation timeout handling
[feature/async-computation] feat(async): implement async computation queue
[feature/async-computation] feat(async): add computation status polling
[feature/async-computation] feat(async): implement cancellation for long-running jobs
[feature/async-computation] feat(async): add computation result expiry policy
[feature/benchmarking-suite] bench: implement computation speed benchmarks
[feature/benchmarking-suite] bench: add memory usage benchmarks
[feature/benchmarking-suite] bench: implement accuracy benchmarks against known results
[feature/benchmarking-suite] bench: add competitive analysis vs Wolfram Alpha API
[feature/code-generation] feat(codegen): implement Python code generation from computations
[feature/code-generation] feat(codegen): add NumPy code export
[feature/code-generation] feat(codegen): implement MATLAB code export
[feature/code-generation] feat(codegen): add Julia code generation
[feature/latex-engine] feat(latex): implement LaTeX input parsing
[feature/latex-engine] feat(latex): add LaTeX to AST conversion
[feature/latex-engine] feat(latex): implement bidirectional LaTeX/MathForge DSL conversion
[feature/latex-engine] fix(latex): fix nested fraction rendering in LaTeX output
[feature/wolfram-compat] feat(compat): implement Wolfram Language subset interpreter
[feature/wolfram-compat] feat(compat): add Mathematica notebook import
[feature/wolfram-compat] feat(compat): implement common Wolfram functions
[feature/wolfram-compat] docs(compat): document Wolfram compatibility layer
[feature/jupyter-integration] feat(jupyter): implement Jupyter kernel protocol
[feature/jupyter-integration] feat(jupyter): add MathForge as Jupyter kernel
[feature/jupyter-integration] feat(jupyter): implement magic commands for MathForge DSL
[feature/jupyter-integration] docs(jupyter): add Jupyter integration guide
[feature/api-client-sdk] feat(sdk): implement Python client SDK
[feature/api-client-sdk] feat(sdk): add JavaScript/TypeScript client SDK
[feature/api-client-sdk] feat(sdk): implement R client library
[feature/api-client-sdk] docs(sdk): add SDK usage examples and tutorials
[feature/plugin-marketplace] feat(marketplace): implement plugin marketplace backend
[feature/plugin-marketplace] feat(marketplace): add plugin submission workflow
[feature/plugin-marketplace] feat(marketplace): implement plugin rating and reviews
[feature/plugin-marketplace] feat(marketplace): add curated plugin collections
[feature/workspace-management] feat(workspace): implement project workspace model
[feature/workspace-management] feat(workspace): add workspace file browser
[feature/workspace-management] feat(workspace): implement workspace templates
[feature/workspace-management] feat(workspace): add workspace sharing
[feature/theme-system] feat(theme): implement CSS custom properties theme system
[feature/theme-system] feat(theme): add dark mode with system preference detection
[feature/theme-system] feat(theme): add solarized and monokai themes
[feature/theme-system] feat(theme): implement custom theme creator
[feature/keyboard-shortcuts] feat(shortcuts): implement global keyboard shortcut system
[feature/keyboard-shortcuts] feat(shortcuts): add shortcut hints overlay
[feature/keyboard-shortcuts] feat(shortcuts): implement vim-mode for expression editor
[feature/keyboard-shortcuts] fix(shortcuts): fix shortcut conflicts with browser defaults
[feature/onboarding] feat(onboarding): implement interactive tutorial
[feature/onboarding] feat(onboarding): add sample computations gallery
[feature/onboarding] feat(onboarding): implement feature discovery tooltips
[feature/onboarding] feat(onboarding): add welcome wizard for new users
[feature/search] feat(search): implement full-text search for computation history
[feature/search] feat(search): add function and constant search
[feature/search] feat(search): implement fuzzy matching for math expressions
[feature/search] feat(search): add search result preview
[bugfix/parser-edge-cases] fix(parser): handle empty expression input gracefully
[bugfix/parser-edge-cases] fix(parser): fix parsing of nested parentheses
[bugfix/parser-edge-cases] fix(parser): handle Unicode math symbols correctly
[bugfix/parser-edge-cases] fix(parser): fix operator priority for unary minus
[bugfix/numerical-stability] fix(numerical): improve condition number estimation
[bugfix/numerical-stability] fix(numerical): handle near-singular matrices gracefully
[bugfix/numerical-stability] fix(numerical): fix catastrophic cancellation in float subtraction
[bugfix/numerical-stability] fix(numerical): improve convergence detection in iterative solvers
[bugfix/ui-rendering] fix(ui): fix plot re-render on window resize
[bugfix/ui-rendering] fix(ui): fix matrix input overflow on small screens
[bugfix/ui-rendering] fix(ui): correct LaTeX rendering for complex fractions
[bugfix/ui-rendering] fix(ui): fix dark mode color contrast for code blocks
[bugfix/api-errors] fix(api): return proper 422 for malformed JSON input
[bugfix/api-errors] fix(api): handle computation timeout with proper error response
[bugfix/api-errors] fix(api): fix CORS preflight handling for auth endpoints
[bugfix/api-errors] fix(api): correct pagination in history list endpoint
[refactor/engine-interfaces] refactor: define common Engine base interface
[refactor/engine-interfaces] refactor: migrate all engines to use unified interface
[refactor/engine-interfaces] refactor: extract shared computation context
[refactor/engine-interfaces] refactor: centralize error handling in engine layer
[refactor/frontend-components] refactor(ui): extract common form components
[refactor/frontend-components] refactor(ui): create design system component library
[refactor/frontend-components] refactor(ui): centralize API client configuration
[refactor/frontend-components] refactor(ui): extract shared hooks for computation state
[chore/dependency-updates] chore: update Python dependencies to latest stable
[chore/dependency-updates] chore: update React and frontend dependencies
[chore/dependency-updates] chore: pin dependency versions for reproducible builds
[chore/dependency-updates] chore: add dependency vulnerability scanning
[chore/code-quality] chore: add ruff and mypy for Python linting
[chore/code-quality] chore: add ESLint and Prettier for TypeScript
[chore/code-quality] chore: configure pre-commit hooks
[chore/code-quality] chore: add code complexity metrics reporting
[release/v1.1.0] chore(release): bump version to v1.1.0
[release/v1.1.0] chore(release): update CHANGELOG for v1.1.0
[release/v1.1.0] chore(release): generate release notes
[release/v1.2.0] chore(release): bump version to v1.2.0
[release/v1.2.0] chore(release): update CHANGELOG for v1.2.0 with ML engine release
[release/v1.2.0] chore(release): generate API migration guide
[release/v1.3.0] chore(release): bump version to v1.3.0
[release/v1.3.0] chore(release): update CHANGELOG for v1.3.0 with physics engine
[release/v1.3.0] chore(release): update documentation site
[release/v2.0.0-beta] chore(release): prepare v2.0.0 beta release
[release/v2.0.0-beta] chore(release): update CHANGELOG for v2.0.0-beta
[release/v2.0.0-beta] chore(release): add upgrade guide from v1.x to v2.0
[release/v2.0.0-beta] chore(release): freeze v2.0.0-beta API surface
[pr/fix-symbolic-parser-edge-cases] fix(symbolic): handle empty input in parser
[pr/fix-symbolic-parser-edge-cases] fix(symbolic): fix operator precedence for nested exprs
[pr/feat-matrix-sparse-ops] feat(matrix): add sparse matrix element-wise ops
[pr/feat-matrix-sparse-ops] test(matrix): add sparse ops unit tests
[pr/feat-calculus-romberg] feat(calculus): implement Romberg integration
[pr/feat-calculus-romberg] test(calculus): verify Romberg accuracy on polynomials
[pr/fix-stats-variance-edge-case] fix(stats): handle n=1 case in variance computation
[pr/feat-prob-copula-frank] feat(prob): add Frank copula implementation
[pr/feat-prob-copula-frank] docs(prob): document Frank copula parameters
[pr/perf-matrix-multiply-cache] perf(matrix): cache-friendly matrix multiply layout
[pr/perf-matrix-multiply-cache] bench(matrix): add multiply benchmark
[pr/fix-numerical-bisection-nan] fix(numerical): guard against NaN in bisection method
[pr/feat-geometry-kd-tree] feat(geo): implement KD-tree for point queries
[pr/feat-geometry-kd-tree] test(geo): add KD-tree nearest-neighbor tests
[pr/feat-graph-floyd-warshall] feat(graph): implement Floyd-Warshall all-pairs shortest path
[pr/feat-graph-floyd-warshall] test(graph): verify Floyd-Warshall on dense graph
[pr/fix-equation-polynomial-gcd] fix(eq): fix GCD computation for polynomials with leading zeros
[pr/feat-signal-wavelet-haar] feat(signal): add Haar wavelet transform
[pr/feat-signal-wavelet-haar] test(signal): verify Haar perfect reconstruction
[pr/feat-ml-gradient-boosting] feat(ml): implement gradient boosting with shrinkage
[pr/feat-ml-gradient-boosting] test(ml): add gradient boosting accuracy test
[pr/fix-numth-miller-rabin-edge] fix(numth): fix Miller-Rabin for n=2 and n=3 edge cases
[pr/feat-physics-rk4-pendulum] feat(physics): simulate double pendulum with RK4
[pr/feat-physics-rk4-pendulum] docs(physics): add pendulum simulation example
[pr/feat-plot-annotation] feat(plot): add text annotation support
[pr/feat-plot-annotation] feat(plot): add arrow annotation to plots
[pr/feat-dataset-sql-group] feat(dataset): implement SQL GROUP BY semantics
[pr/feat-dataset-sql-group] test(dataset): add groupby aggregation tests
[pr/feat-export-svg-batch] feat(export): add batch SVG export
[pr/feat-export-svg-batch] perf(export): parallelize SVG rendering
[pr/feat-plugin-hot-reload] feat(plugin): implement plugin hot-reload
[pr/feat-plugin-hot-reload] test(plugin): add plugin reload lifecycle test
[pr/fix-api-timeout-handling] fix(api): return 408 on computation timeout
[pr/fix-api-timeout-handling] test(api): add timeout integration test
[pr/feat-auth-refresh-token] feat(auth): implement JWT refresh token rotation
[pr/feat-auth-refresh-token] test(auth): add refresh token expiry test
[pr/fix-ws-reconnect-backoff] fix(ws): implement exponential backoff on reconnect
[pr/fix-ws-reconnect-backoff] test(ws): add reconnect simulation test
[pr/feat-cache-lru-eviction] feat(cache): implement LRU eviction policy
[pr/feat-cache-lru-eviction] test(cache): verify LRU behavior under load
[pr/perf-symbolic-cse] perf(symbolic): common subexpression elimination pass
[pr/perf-symbolic-cse] bench(symbolic): CSE benchmark on large expressions
[pr/feat-notebook-git-history] feat(notebook): track notebook version history
[pr/feat-notebook-git-history] test(notebook): add version diff test
[pr/fix-plot-axis-labels] fix(plot): prevent axis label overlap with auto-rotation
[pr/fix-plot-axis-labels] fix(plot): fix label truncation on small viewports
[pr/feat-stats-kernel-density] feat(stats): implement kernel density estimation
[pr/feat-stats-kernel-density] test(stats): verify KDE on Gaussian samples
[pr/feat-prob-beta-distribution] feat(prob): add Beta distribution support
[pr/feat-prob-beta-distribution] test(prob): verify Beta moments
[pr/feat-numerical-hermite-interp] feat(numerical): add Hermite interpolation
[pr/feat-numerical-hermite-interp] test(numerical): verify Hermite with derivative data
[pr/fix-opt-adam-bias-correction] fix(opt): apply bias correction in Adam first iteration
[pr/feat-geo-convex-hull-3d] feat(geo): implement 3D convex hull (QuickHull3D)
[pr/feat-geo-convex-hull-3d] test(geo): verify 3D convex hull volume
[pr/feat-graph-community-detection] feat(graph): implement Louvain community detection
[pr/feat-graph-community-detection] test(graph): verify modularity improvement
[pr/fix-eq-linear-system-singular] fix(eq): detect and report singular systems gracefully
[pr/feat-signal-stft] feat(signal): implement Short-Time Fourier Transform
[pr/feat-signal-stft] test(signal): verify STFT invertibility
[pr/feat-ml-attention-mechanism] feat(ml): implement scaled dot-product attention
[pr/feat-ml-attention-mechanism] test(ml): verify attention output shape
[pr/fix-numth-pollard-cycle] fix(numth): fix cycle detection in Pollard rho
[pr/feat-physics-em-simulation] feat(physics): simulate EM field on 2D grid
[pr/feat-physics-em-simulation] test(physics): verify Gauss law on point charge
[pr/feat-dataset-parquet-streaming] feat(dataset): stream large Parquet files in chunks
[pr/feat-dataset-parquet-streaming] test(dataset): add streaming integrity test
[pr/feat-export-jupyter-widgets] feat(export): embed interactive widgets in Jupyter export
[pr/fix-plugin-sandbox-escape] security(plugin): patch sandbox escape via __builtins__
[pr/fix-plugin-sandbox-escape] test(plugin): add sandbox security test
[pr/feat-ui-expression-history] feat(ui): add expression history dropdown
[pr/feat-ui-expression-history] fix(ui): persist history across sessions
[pr/fix-api-cors-preflight] fix(api): correctly handle OPTIONS preflight for all routes
[pr/perf-graph-bfs-queue] perf(graph): replace list with deque for BFS O(1) popleft
[pr/perf-graph-bfs-queue] bench(graph): show 3x speedup on large graphs
[pr/feat-symbolic-groebner] feat(symbolic): implement Buchberger algorithm for Groebner basis
[pr/feat-symbolic-groebner] test(symbolic): verify ideal membership
[pr/feat-calculus-adaptive-simpson] feat(calculus): add adaptive Simpson quadrature
[pr/feat-calculus-adaptive-simpson] test(calculus): verify on oscillatory functions
[pr/fix-stats-t-test-welch] fix(stats): use Welch correction for unequal variances in t-test
[pr/feat-prob-mcmc-hmc] feat(prob): implement Hamiltonian Monte Carlo sampler
[pr/feat-prob-mcmc-hmc] test(prob): verify HMC on bivariate Gaussian
[pr/perf-matrix-svd-lanczos] perf(matrix): use Lanczos iteration for large sparse SVD
[pr/perf-matrix-svd-lanczos] bench(matrix): 10x speedup on sparse matrices
[pr/feat-geo-polygon-clip] feat(geo): implement Sutherland-Hodgman polygon clipping
[pr/feat-geo-polygon-clip] test(geo): verify clip preserves area
[pr/feat-graph-max-clique] feat(graph): implement Bron-Kerbosch max clique
[pr/feat-graph-max-clique] test(graph): verify on known clique instances
[pr/fix-eq-diophantine-negative] fix(eq): handle negative coefficients in linear Diophantine solver
[pr/feat-signal-phase-vocoder] feat(signal): implement phase vocoder for time-stretching
[pr/feat-signal-phase-vocoder] test(signal): verify pitch preservation
[pr/feat-ml-vae-encoder] feat(ml): implement VAE encoder with reparameterization
[pr/feat-ml-vae-encoder] test(ml): verify latent space distribution
[pr/feat-numth-elliptic-add] feat(numth): implement elliptic curve point addition
[pr/feat-numth-elliptic-add] test(numth): verify associativity of EC addition
[pr/feat-physics-quantum-gates] feat(physics): add Hadamard, CNOT, Toffoli gates
[pr/feat-physics-quantum-gates] test(physics): verify quantum gate unitarity
[pr/feat-plot-3d-interactive] feat(plot): add trackball rotation for 3D plots
[pr/feat-plot-3d-interactive] feat(plot): add pinch-to-zoom on touch devices
[pr/feat-dataset-missing-knn] feat(dataset): implement KNN imputation for missing values
[pr/feat-dataset-missing-knn] test(dataset): verify KNN imputation RMSE
[pr/feat-export-latex-template] feat(export): add customizable LaTeX document templates
[pr/feat-export-latex-template] docs(export): document template variables
[pr/fix-plugin-version-conflict] fix(plugin): resolve version conflict between plugin deps
[pr/feat-ui-dark-mode-toggle] feat(ui): add animated dark/light mode toggle
[pr/feat-ui-dark-mode-toggle] fix(ui): persist theme preference in localStorage
[pr/perf-api-response-compression] perf(api): enable gzip response compression
[pr/perf-api-response-compression] bench(api): 60% payload reduction on large responses
[pr/feat-symbolic-limit-lhopital] feat(symbolic): apply L'Hopital rule in limit evaluation
[pr/feat-symbolic-limit-lhopital] test(symbolic): verify limits of indeterminate forms
[pr/feat-calculus-ode-stiff] feat(calculus): add BDF solver for stiff ODEs
[pr/feat-calculus-ode-stiff] test(calculus): verify on Van der Pol oscillator
[pr/fix-stats-chi-squared-df] fix(stats): correct degrees of freedom in chi-squared test
[pr/feat-prob-poisson-process] feat(prob): simulate inhomogeneous Poisson process
[pr/feat-prob-poisson-process] test(prob): verify intensity estimation
[pr/perf-numerical-fft-radix4] perf(numerical): add radix-4 FFT for power-of-4 sizes
[pr/perf-numerical-fft-radix4] bench(numerical): 25% speedup over radix-2
[pr/feat-geo-voronoi-incremental] feat(geo): implement incremental Voronoi construction
[pr/feat-geo-voronoi-incremental] test(geo): verify Fortune's and incremental agree
[pr/feat-graph-spectral-clustering] feat(graph): implement spectral clustering via graph Laplacian
[pr/feat-graph-spectral-clustering] test(graph): verify cluster assignment on SBM graph
[pr/fix-eq-polynomial-sturm] fix(eq): implement Sturm sequence for real root isolation
[pr/feat-signal-mel-spectrogram] feat(signal): compute Mel spectrogram for audio
[pr/feat-signal-mel-spectrogram] test(signal): verify filterbank energy sums
[pr/feat-ml-transformer-block] feat(ml): implement Transformer encoder block
[pr/feat-ml-transformer-block] test(ml): verify residual connection shapes
[pr/feat-numth-quadratic-sieve] feat(numth): implement basic quadratic sieve factorization
[pr/feat-numth-quadratic-sieve] test(numth): factor semiprime with quadratic sieve
[pr/feat-physics-navier-stokes-2d] feat(physics): solve 2D Navier-Stokes with finite diff
[pr/feat-physics-navier-stokes-2d] test(physics): verify lid-driven cavity solution
[pr/feat-plot-contour-labels] feat(plot): add auto-placed contour line labels
[pr/feat-plot-contour-labels] fix(plot): fix label collision near plot edges
[pr/feat-dataset-join-hash] feat(dataset): implement hash join for large datasets
[pr/feat-dataset-join-hash] bench(dataset): 5x speedup over nested loop join
[pr/fix-export-pdf-unicode] fix(export): handle Unicode characters in PDF export
[pr/feat-plugin-marketplace-ratings] feat(plugin): display star ratings in marketplace
[pr/feat-plugin-marketplace-ratings] fix(plugin): fix rating average for < 5 reviews
[pr/feat-ui-mobile-swipe] feat(ui): add swipe gesture for mobile navigation
[pr/feat-ui-mobile-swipe] test(ui): add Playwright swipe gesture test
[pr/fix-auth-jwt-expiry-clock] fix(auth): add clock skew tolerance in JWT validation
[pr/feat-cache-distributed-redis] feat(cache): implement distributed cache via Redis
[pr/feat-cache-distributed-redis] test(cache): verify cross-instance cache hit
[pr/perf-symbolic-pattern-index] perf(symbolic): index patterns by root node type
[pr/perf-symbolic-pattern-index] bench(symbolic): 4x faster simplification dispatch
[pr/feat-notebook-auto-save] feat(notebook): auto-save every 60s with conflict detection
[pr/feat-notebook-auto-save] test(notebook): simulate concurrent save conflict
[pr/feat-calculus-pde-heat] feat(calculus): solve heat equation with Crank-Nicolson
[pr/feat-calculus-pde-heat] test(calculus): verify conservation of energy
[pr/feat-stats-bootstrap-bca] feat(stats): implement BCa bootstrap confidence intervals
[pr/feat-stats-bootstrap-bca] test(stats): verify BCa vs percentile intervals
[pr/fix-prob-inverse-cdf-beta] fix(prob): fix numerical instability in Beta CDF inversion
