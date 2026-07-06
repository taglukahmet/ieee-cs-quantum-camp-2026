# IEEE CS Quantum Camp 2026: Master Curriculum

## TEAM: Quruntu

### Node 1: Formulation Architect (Ahmet Tağluk)
**Theory & Mathematics**
- [ ] `[1h]` Complete: 3Blue1Brown - Vectors & Linear Combinations
- [ ] `[1h]` Complete: 3Blue1Brown - Matrix Multiplication & Eigenvectors
- [ ] `[2h]` Master: Dirac (Bra-Ket) notation & Superposition algebra
- [ ] `[3h]` Master: Penalty Methods (Lagrange multipliers for inequality constraints)
- [ ] `[3h]` Master: Quadratic terms mapping for dependent node constraints
**Execution & Output**
- [ ] `[2h]` Draft: Algebraic objective function for energy cost minimization
- [ ] `[2h]` Draft: Penalty equation for reservoir capacity boundaries (Min/Max)
- [ ] `[4h]` Code PR: Submit Mathematical markdown `[challenges/02_qubo/penalty_model.md]`
- [ ] `[2h]` Report Draft: Write the "Mathematical Optimization Strategy" section (Max 2 pages).

### Node 2: Annealing & Repair Engineer (Mine Çetinkaya)
**Theory & Hardware**
- [ ] `[1h]` Read: D-Wave Docs - "What is Quantum Annealing?"
- [ ] `[2h]` Watch: D-Wave Webinar - "Formulating QUBOs for Optimization"
- [ ] `[2h]` Study: Local search heuristics (Tabu Search/Simulated Annealing concepts)
**SDK Mastery (Ocean)**
- [ ] `[2h]` Master: `dimod` module & `BinaryQuadraticModel` (BQM) instantiation
- [ ] `[3h]` Master: `ConstrainedQuadraticModel` (CQM) & `.add_constraint()` syntax
- [ ] `[1h]` Master: Configuring `num_reads` and `annealing_time` parameters
- [ ] `[2h]` Master: Cloud deployment via `LeapHybridCQMSolver`
**Execution & Output**
- [ ] `[3h]` Code PR: Extract lowest-energy configurations from a `SampleSet` object
- [ ] `[4h]` Code PR: Submit Ocean CQM script `[challenges/03_ocean/sampler.py]`
- [ ] `[2h]` Report Draft: Write the "Hybrid Annealing Hardware Execution" section (Max 2 pages).

### Node 3: Gate-Based Architect (Zeynep Dilay Çelik)
**Theory & Hardware**
- [ ] `[2h]` Complete: IBM Quantum Learning - "Basics of Quantum Information"
- [ ] `[1h]` Master: Qubit state mapping on the Bloch Sphere
- [ ] `[2h]` Master: The Measurement Problem & statevector collapse probabilities
- [ ] `[3h]` Watch: Qiskit YouTube - "Quantum Optimization" (VQE & QAOA mechanics)
**SDK Mastery (Qiskit)**
- [ ] `[2h]` Master: `QuantumCircuit` instantiation & register mapping
- [ ] `[2h]` Master: Gate application (H, X, CNOT, Rz)
- [ ] `[2h]` Master: Execution via `AerSimulator` and histogram plotting
- [ ] `[3h]` Master: Qiskit Optimization Module (`QuadraticProgram` class)
**Execution & Output**
- [ ] `[3h]` Code PR: Build alternating cost/mixer layers for a QAOA ansatz
- [ ] `[4h]` Code PR: Submit Qiskit benchmark script `[challenges/04_qaoa/circuit.ipynb]`
- [ ] `[2h]` Report Draft: Write the "Gate-Based Combinatorial Comparison" section (Max 2 pages).

### Node 4: Classical Data Engineer (İrem Saniye Baran)
**Theory & Mathematics**
- [ ] `[2h]` Master: Linear Programming (LP) boundaries & equality constraints
- [ ] `[3h]` Master: Mixed-Integer Linear Programming (MILP) logic for binary hardware
- [ ] `[2h]` Read: Google OR-Tools Documentation (Routing & MIP)
**SDK Mastery**
- [ ] `[2h]` Master: Python JSON/CSV ingestion and payload cleaning
- [ ] `[2h]` Master: `scipy.optimize.linprog` execution
- [ ] `[3h]` Master: Google OR-Tools environment setup
**Execution & Output**
- [ ] `[2h]` Code PR: Calculate baseline electrical costs for a dummy 3-pump flow
- [ ] `[4h]` Code PR: Submit classical baseline script `[challenges/01_baseline/linprog.py]`
- [ ] `[2h]` Report Draft: Write the "Dataset Pre-Processing & Classical Baselines" section (Max 2 pages).

### Node 5: Systems Integrator (Ekin Ağardan)
**Theory & Algorithms**
- [ ] `[2h]` Read: NetworkX Documentation (Graph theory mapping)
- [ ] `[3h]` Study: Graph Partitioning algorithms (METIS concepts)
- [ ] `[3h]` Study: Multi-Objective Pareto Optimization logic
**SDK Mastery & Pipeline**
- [ ] `[1h]` Master: Setting up Python Virtual Environments (`venv`)
- [ ] `[2h]` Master: `NetworkX` graph instantiation from JSON payloads
- [ ] `[2h]` Master: Formatting CLI outputs for execution time & cost comparisons
**Execution & Output**
- [ ] `[3h]` Code PR: Write script partitioning a 10-node JSON graph into sub-graphs
- [ ] `[5h]` Code PR: Submit integrated pipeline `[challenges/05_pipeline/main.py]`
- [ ] `[2h]` Report Draft: Compile all sections into the final constraint-checked PDF (Max 15 pages).

---

## TEAM: kararsızlıQ

**Note:** We prepared like this, you can change it according to your division of labour


## Node 1: Formulation Architect (Name)
**Theory & Mathematics**
- [ ] `[1h]` Complete: 3Blue1Brown - Vectors & Linear Combinations
- [ ] `[1h]` Complete: 3Blue1Brown - Matrix Multiplication & Eigenvectors
- [ ] `[2h]` Master: Dirac (Bra-Ket) notation & Superposition algebra
- [ ] `[3h]` Master: Penalty Methods (Lagrange multipliers for inequality constraints)
- [ ] `[3h]` Master: Quadratic terms mapping for dependent node constraints
**Execution & Output**
- [ ] `[2h]` Draft: Algebraic objective function for energy cost minimization
- [ ] `[2h]` Draft: Penalty equation for reservoir capacity boundaries (Min/Max)
- [ ] `[4h]` Code PR: Submit Mathematical markdown `[challenges/02_qubo/penalty_model.md]`
- [ ] `[2h]` Report Draft: Write the "Mathematical Optimization Strategy" section (Max 2 pages).

### Node 2: Annealing & Repair Engineer (Name)
**Theory & Hardware**
- [ ] `[1h]` Read: D-Wave Docs - "What is Quantum Annealing?"
- [ ] `[2h]` Watch: D-Wave Webinar - "Formulating QUBOs for Optimization"
- [ ] `[2h]` Study: Local search heuristics (Tabu Search/Simulated Annealing concepts)
**SDK Mastery (Ocean)**
- [ ] `[2h]` Master: `dimod` module & `BinaryQuadraticModel` (BQM) instantiation
- [ ] `[3h]` Master: `ConstrainedQuadraticModel` (CQM) & `.add_constraint()` syntax
- [ ] `[1h]` Master: Configuring `num_reads` and `annealing_time` parameters
- [ ] `[2h]` Master: Cloud deployment via `LeapHybridCQMSolver`
**Execution & Output**
- [ ] `[3h]` Code PR: Extract lowest-energy configurations from a `SampleSet` object
- [ ] `[4h]` Code PR: Submit Ocean CQM script `[challenges/03_ocean/sampler.py]`
- [ ] `[2h]` Report Draft: Write the "Hybrid Annealing Hardware Execution" section (Max 2 pages).

### Node 3: Gate-Based Architect (Name)
**Theory & Hardware**
- [ ] `[2h]` Complete: IBM Quantum Learning - "Basics of Quantum Information"
- [ ] `[1h]` Master: Qubit state mapping on the Bloch Sphere
- [ ] `[2h]` Master: The Measurement Problem & statevector collapse probabilities
- [ ] `[3h]` Watch: Qiskit YouTube - "Quantum Optimization" (VQE & QAOA mechanics)
**SDK Mastery (Qiskit)**
- [ ] `[2h]` Master: `QuantumCircuit` instantiation & register mapping
- [ ] `[2h]` Master: Gate application (H, X, CNOT, Rz)
- [ ] `[2h]` Master: Execution via `AerSimulator` and histogram plotting
- [ ] `[3h]` Master: Qiskit Optimization Module (`QuadraticProgram` class)
**Execution & Output**
- [ ] `[3h]` Code PR: Build alternating cost/mixer layers for a QAOA ansatz
- [ ] `[4h]` Code PR: Submit Qiskit benchmark script `[challenges/04_qaoa/circuit.ipynb]`
- [ ] `[2h]` Report Draft: Write the "Gate-Based Combinatorial Comparison" section (Max 2 pages).

### Node 4: Classical Data Engineer (Name)
**Theory & Mathematics**
- [ ] `[2h]` Master: Linear Programming (LP) boundaries & equality constraints
- [ ] `[3h]` Master: Mixed-Integer Linear Programming (MILP) logic for binary hardware
- [ ] `[2h]` Read: Google OR-Tools Documentation (Routing & MIP)
**SDK Mastery**
- [ ] `[2h]` Master: Python JSON/CSV ingestion and payload cleaning
- [ ] `[2h]` Master: `scipy.optimize.linprog` execution
- [ ] `[3h]` Master: Google OR-Tools environment setup
**Execution & Output**
- [ ] `[2h]` Code PR: Calculate baseline electrical costs for a dummy 3-pump flow
- [ ] `[4h]` Code PR: Submit classical baseline script `[challenges/01_baseline/linprog.py]`
- [ ] `[2h]` Report Draft: Write the "Dataset Pre-Processing & Classical Baselines" section (Max 2 pages).

### Node 5: Systems Integrator (Name)
**Theory & Algorithms**
- [ ] `[2h]` Read: NetworkX Documentation (Graph theory mapping)
- [ ] `[3h]` Study: Graph Partitioning algorithms (METIS concepts)
- [ ] `[3h]` Study: Multi-Objective Pareto Optimization logic
**SDK Mastery & Pipeline**
- [ ] `[1h]` Master: Setting up Python Virtual Environments (`venv`)
- [ ] `[2h]` Master: `NetworkX` graph instantiation from JSON payloads
- [ ] `[2h]` Master: Formatting CLI outputs for execution time & cost comparisons
**Execution & Output**
- [ ] `[3h]` Code PR: Write script partitioning a 10-node JSON graph into sub-graphs
- [ ] `[5h]` Code PR: Submit integrated pipeline `[challenges/05_pipeline/main.py]`
- [ ] `[2h]` Report Draft: Compile all sections into the final constraint-checked PDF (Max 15 pages).