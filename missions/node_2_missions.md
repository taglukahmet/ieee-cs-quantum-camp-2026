# MISSION DETAILS: NODE 2 (Mine Çetinkaya)

### (#N2-01) D-Wave Physics: The Quantum Annealing Landscape
**Description:** You must understand the physical hardware before you write code for it. How does the system settle from an initial superposition state into a final problem Hamiltonian?
**Sources:**
- D-Wave Documentation: "What is Quantum Annealing?"
**Acceptance Criteria:**
- You can visually and verbally explain the concept of an "energy landscape" and how quantum tunneling helps the system escape local minima.

### (#N2-02) Formulating QUBOS for Optimization
**Description:** You need to understand how constraints are mapped into a matrix format.
**Sources:**
- YouTube: D-Wave Systems - "Formulating QUBOS for Optimization Problems"
**Acceptance Criteria:**
- You can explain how a linear dependency between two nodes becomes a quadratic mathematical term in a QUBO.

### (#N2-03) Mixed-Integer to QUBO Mapping & Integer Bounds
**Description:** Real physical networks contain continuous flow rates, not just binary switches. You must learn how the SDK handles integer variables within the constraints.
**Sources:**
- D-Wave Ocean SDK Documentation: "Integer Variable Representations".
**Acceptance Criteria:**
- Read the documentation to find out how `dimod.Integer()` bounds are defined and converted under the hood.
- Write out the syntax to define a variable constrained between `V_min` and `V_max`.

### (#N2-04) Map Mathematical Formulation into `dimod` Objects
**Description:** Take the pure equations created by Node 1 and map them into the `dimod` structure.
**Sources:**
- Node 1's Mathematical Markdown payload.
**Acceptance Criteria:**
- Without running cloud compute, instantiate a local `BinaryQuadraticModel` (BQM) representing a simple 2-pump penalty equation.

### (#N2-05) Build `ConstrainedQuadraticModel` (CQM) Logic
**Description:** The Leap Hybrid solver requires the use of CQMs to handle complex bounded constraints automatically.
**Sources:**
- D-Wave GitHub Examples: "Resource-Constrained Scheduling".
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N2-05-cqm-build`.
- Write `challenges/quruntu/cqm_builder.py`.
- Instantiate a `ConstrainedQuadraticModel` and successfully use `.add_constraint()` for a simulated reservoir limit.
- Commit, push, open a Pull Request, and have Node 1 review it.

### (#N2-06) Cloud Deployment API via `LeapHybridCQMSolver`
**Description:** You must authenticate and submit your CQM object to the hybrid cloud solver using the `.env` architecture we established.
**Sources:**
- D-Wave Ocean SDK: Hybrid Solvers Documentation.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N2-06-hybrid-solver`.
- Write a script that loads `DWAVE_API_TOKEN` via our `Config` class, submits the CQM, and returns the response.
- Commit, push, open a Pull Request, and have Node 5 review it.

### (#N2-07) Parse `SampleSet` for Constraint Violations
**Description:** The solver will return multiple possible network configurations. You must isolate the lowest-energy solution and check if any physical boundaries (like reservoir overflow) were broken due to hardware noise.
**Sources:**
- Ocean SDK Documentation: Handling `SampleSet` Objects.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N2-07-sampleset-parser`.
- Write a parsing function that flags any bit configuration that violates the problem's hard constraints.
- Commit, push, open a PR, and have Node 4 review it.

### (#N2-08) Integrate Node 4's Tabu Search "Repair" Script
**Description:** When the quantum hardware returns an invalid configuration, we rely on classical heuristics to fix it. Node 4 will write the heuristic; you must link it to the Quantum output.
**Sources:**
- Node 4's Local Search codebase.
**Acceptance Criteria:**
- Check out Node 4's branch.
- Write the connective logic: If the `SampleSet` is flagged as invalid, automatically pass that binary array into Node 4's Tabu Search function for repair.

### (#N2-09) Review Node 1's Mathematical Constraint Equations
**Description:** Before you can write the `dimod` logic, you must ensure Node 1's math translates cleanly to the SDK.
**Sources:**
- Node 1's open Pull Request for the Constraint Payload.
**Acceptance Criteria:**
- Review the math. Verify that there are no continuous variables left unmapped or unpenalized before approving Node 1's Pull Request.
