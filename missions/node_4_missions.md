# MISSION DETAILS: NODE 4 (İrem Saniye Baran)

### (#N4-01) Mixed-Integer Linear Programming (MILP) Logic
**Description:** Classical linear programming can handle fluid flow, but you cannot have 0.5 of a pump turned on. You must understand how integer constraints alter the mathematical landscape.
**Sources:**
- Google OR-Tools Documentation: "Mixed-Integer Programming".
**Acceptance Criteria:**
- Explain the computational complexity shift from P to NP-hard when binary constraints are added to a linear model.
- Write down a basic mathematical constraint that forces a decision variable to be either exactly 0 or exactly 1.

### (#N4-02) Google OR-Tools CP-SAT Solver Mechanics
**Description:** We are completely skipping `scipy.linprog`[cite: 1]. The Google CP-SAT engine is specifically optimized for complex, time-based scheduling constraints and logical state transitions[cite: 1].
**Sources:**
- Google OR-Tools Documentation: "CP-SAT Solver".
**Acceptance Criteria:**
- Read the documentation to understand how CP-SAT handles boolean logic and transition matrices differently than standard GLOP solvers.

### (#N4-03) Local Search Heuristics & Tabu Search Theory
**Description:** Quantum hardware will return broken constraints due to physical noise[cite: 1]. You are responsible for providing the algorithmic safety net that repairs these errors[cite: 1].
**Sources:**
- Academic papers / Textbooks: "Tabu Search algorithm fundamentals".
**Acceptance Criteria:**
- Define what a "Tabu List" is and explain how it prevents a classical search algorithm from getting stuck in an endless loop at a local minimum.

### (#N4-04) Standardize JSON/CSV Data Ingestion Classes
**Description:** You must establish strict formatting structures for the JSON/CSV inputs on day one[cite: 1]. Node 2 and Node 3 will build their mathematical arrays from your baseline[cite: 1].
**Sources:**
- Python `json` and `pandas` documentation.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N4-04-data-ingestion`.
- Write `challenges/quruntu/data_loader.py`. Build a script that parses a simulated water network JSON into structured Python dictionaries.
- Commit, push, open a Pull Request, and have Node 5 review the data structures.

### (#N4-05) Build CP-SAT MILP Baseline (Pump Wear-and-Tear)
**Description:** Write the classical baseline solver that accurately calculates pump wear-and-tear costs[cite: 1]. This is the benchmark that Node 3 will measure their quantum circuits against.
**Sources:**
- Node 1's Multi-Period mathematical formulations.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N4-05-cpsat-baseline`.
- Write `challenges/quruntu/classical_baseline.py`. Implement a 3-pump dynamic cost calculation using `cp_model.CpModel()`.
- Commit, push, open a PR, and have Node 1 verify the math.

### (#N4-06) Build Tabu Search "Repair" Framework
**Description:** Write the standalone classical heuristic script that takes a slightly broken binary array and searches local neighboring states to find a valid configuration.
**Sources:**
- Local search algorithm design patterns.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N4-06-tabu-repair`.
- Write `challenges/quruntu/tabu_repair.py`. The function must accept an invalid bitstring, apply a bit-flip neighborhood search, and return a valid bitstring.
- Commit, push, open a PR, and have Node 2 review it.

### (#N4-07) Collaborate with Node 2 on Quantum Output Filtering
**Description:** Your Tabu Search repair framework must be wired directly into Node 2's D-Wave execution pipeline.
**Sources:**
- Node 2's D-Wave Ocean codebase.
**Acceptance Criteria:**
- Review Node 2's `SampleSet` parser logic.
- Ensure that the variables extracted from the quantum hardware seamlessly pass into your `tabu_repair.py` script without type errors or dimension mismatches.

### (#N4-08) Review Node 5's NetworkX Topological Baselines
**Description:** Node 5 is building the graph structures. You must ensure their output can be easily digested by your CP-SAT solver.
**Sources:**
- Node 5's open Pull Request for NetworkX generation.
**Acceptance Criteria:**
- Check out Node 5's branch locally. Verify that the nodes and edges mapped in their graph contain the correct cost coefficient variables required by your baseline solver.
