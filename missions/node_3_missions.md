# MISSION DETAILS: NODE 3 (Zeynep Dilay Çelik)

### (#N3-01) IBM Quantum Learning: Basics of Quantum Information
**Description:** You must understand the mathematical realities of qubits before defining circuits.
**Sources:**
- IBM Quantum Learning: "Basics of Quantum Information".
**Acceptance Criteria:**
- Verbally explain the measurement problem and how probability amplitudes dictate statevector collapse.
- Map the angles $\theta$ and $\phi$ of a single qubit state on the Bloch Sphere.

### (#N3-02) Programmatic Circuit Construction & Gate Application
**Description:** Move from pure theory to code. Learn how to map physical qubits to index positions in Qiskit and apply standard operations.
**Sources:**
- Qiskit Documentation: `QuantumCircuit` class.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N3-02-circuit-basics`.
- Write a script in `challenges/quruntu/circuit_test.py` that applies H, X, CNOT, and Rz gates across a 3-qubit register.
- Commit, push, open a Pull Request, and have Node 1 review the math.

### (#N3-03) Execution via `AerSimulator` & Noise Injection
**Description:** Physical quantum hardware is noisy and returns errors[cite: 1]. You must learn how to simulate hardware noise locally to see how constraints degrade.
**Sources:**
- Qiskit Aer Documentation: Building Noise Models.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N3-03-aer-noise`.
- Run your previous circuit using `AerSimulator` over 1000 shots.
- Inject a basic depolarizing error model and plot the resulting probability histogram.
- Commit, push, and merge via PR.

### (#N3-04) Qiskit Optimization: VQE & QAOA Mechanics
**Description:** The hackathon optimization relies on hybrid variational loops. You must understand how the classical optimizer updates the quantum parameters.
**Sources:**
- Qiskit YouTube Channel: "Quantum Optimization" seminar series.
**Acceptance Criteria:**
- Explain the division of labor between the quantum execution (cost evaluation) and the classical optimizer (like COBYLA/SPSA updating the ansatz parameters).

### (#N3-05) XY-Mixers & Constraint-Preserving Circuitry
**Description:** Standard QAOA uses a transverse-field X-mixer which explores the entire Hilbert space, completely ignoring physical constraints[cite: 1]. You must research how to build a mixer circuit that naturally restricts the quantum state within the valid constraint subspace[cite: 1].
**Sources:**
- Qiskit Advanced Seminars / Research papers on "Constrained Quantum Optimization using the XY Mixer"[cite: 1].
**Acceptance Criteria:**
- Formulate the theoretical difference between an X-mixer and an XY-mixer on a whiteboard.

### (#N3-06) Formulate Penalty-Loaded `QuadraticProgram`
**Description:** If custom XY-mixers become computationally expensive, you must know how to load Node 1's explicit penalty matrices into a standard Qiskit optimizer to avoid local minima[cite: 1].
**Sources:**
- Qiskit Optimization Module Documentation: `QuadraticProgram`.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N3-06-quad-program`.
- Write `challenges/quruntu/qiskit_formulation.py`. Load a simulated 3-pump constraint into the `QuadraticProgram` class.
- Commit, push, and merge via PR.

### (#N3-07) Build QAOA Ansatz (Cost & Mixer Layers)
**Description:** The ultimate benchmark. You must construct the alternating logic layers of the QAOA algorithm specifically tailored for our penalty formulation.
**Sources:**
- Qiskit Circuit Library: QAOAAnsatz.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N3-07-qaoa-ansatz`.
- Write the final test circuit: `challenges/quruntu/qaoa_benchmark.py`. Map the cost and mixer layers mathematically.
- Commit, push, open a Pull Request, and have Node 5 review the structural code.

### (#N3-08) Review Node 1's QUBO / Penalty Formulations
**Description:** Since your gate-based logic relies entirely on Node 1's formulation, you must verify the math before attempting to build a circuit for it.
**Sources:**
- Node 1's open Pull Request (Mathematical Payload).
**Acceptance Criteria:**
- Check out Node 1's branch. Review the mathematical logic of the constraint penalties. Verify that it maps cleanly to a `QuadraticProgram` before approving the PR.

### (#N3-09) Benchmark QAOA vs. Node 4's Classical Baseline
**Description:** A quantum solution is meaningless without a classical baseline to compare it against.
**Sources:**
- Node 4's LP/MILP classical solver output.
**Acceptance Criteria:**
- Execute Node 4's classical baseline script.
- Execute your QAOA script on the exact same dataset.
- Ensure your quantum circuit returns the identical optimal solution indices as the classical solver.
