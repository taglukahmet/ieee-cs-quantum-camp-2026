# MISSION DETAILS: NODE 1 (Ahmet Tağluk)

### (#N1-01) 3Blue1Brown: Vectors & Linear Combinations
**Description:** Quantum computing does not use boolean logic; it uses vector spaces. You must visually understand how a state vector is defined by its basis states.
**Sources:**
- YouTube: 3Blue1Brown "Essence of Linear Algebra" (Chapters 1 & 2).
**Acceptance Criteria:**
- You can explain the geometric difference between a scalar and a vector.
- You understand what a linear combination of two basis vectors looks like in 2D space.

### (#N1-02) 3Blue1Brown: Matrix Multiplication & Eigenvectors
**Description:** Quantum logic gates are just unitary matrices. Applying a gate to a qubit is mathematically just multiplying a matrix by a column vector.
**Sources:**
- YouTube: 3Blue1Brown "Essence of Linear Algebra" (Chapters 3 & 14).
**Acceptance Criteria:**
- You can manually multiply a $2 \times 2$ matrix by a $2 \times 1$ column vector on paper.
- You understand that eigenvectors represent axes of rotation that remain unchanged during a transformation.

### (#N1-03) Calculate Bra-Ket probabilities
**Description:** The AI interview and the electronic exam will test your ability to read Dirac notation. You must calculate measurement probabilities manually.
**Sources:**
- IBM Quantum Learning: "Basics of Quantum Information" (Multiple Qubits section).
**Acceptance Criteria:**
- On a physical whiteboard, write a 2-qubit superposition state equation.
- Calculate the probability amplitude of measuring the $|11\rangle$ state.

### (#N1-04) Penalty Methods & Lagrange Multipliers
**Description:** Quantum annealers only minimize energy; they do not understand "limits." You must translate constraints into algebraic penalties that spike the energy landscape if violated.
**Sources:**
- D-Wave Ocean SDK Documentation: "Formulating QUBOS".
**Acceptance Criteria:**
- Write an algebraic equation that equals 0 if $x + y = 1$, but returns a massive positive integer if $x + y = 0$ or $x + y = 2$.

### (#N1-05) Multi-Period Indexing & Dynamic Stock-Balance
**Description:** Water networks operate across time. The storage at hour $t$ depends on hour $t-1$. You must master dynamic state-space modeling.
**Sources:**
- Google OR-Tools Documentation: "Inventory Management / Multi-Period Models".
**Acceptance Criteria:**
- Define the mathematical notation to index variables across multiple time steps (e.g., $x_{i,t}$ representing Pump $i$ at hour $t$).

### (#N1-06) Draft Multi-Period Reservoir Constraint Equation
**Description:** Create the actual formula for the hackathon's core physical constraint: maintaining water levels within safe operational limits over time.
**Sources:**
- Review generic mass balance equations in fluid dynamics.
**Acceptance Criteria:**
- Write a formal mathematical constraint on paper for a single reservoir: $S_t = S_{t-1} + I_t - O_t$.
- Map out how you will apply the penalty method to ensure $V_{\min} \le S_t \le V_{\max}$.

### (#N1-07) Draft Pump Transition Penalty Matrix
**Description:** The system penalizes excessive on-off switching of pumps to preserve asset lifespans. You must write a quadratic term mapping this logic.
**Sources:**
- D-Wave Examples: "Job-Shop Scheduling" (specifically transition penalties).
**Acceptance Criteria:**
- Write a quadratic matrix term that outputs a cost penalty only when $x_{t-1} = 0$ and $x_t = 1$.

### (#N1-08) Build Mathematical Markdown Payload
**Description:** Time to digitize your math. You must document the penalty models so Node 2 and Node 3 can build their code off a single source of truth.
**Sources:**
- Your whiteboard notes from N1-06 and N1-07.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N1-08-math-payload`.
- Write `challenges/quruntu/penalty_model.md` using formal LaTeX syntax.
- Commit, push, and open a Pull Request. Have Node 2 review and merge it.

### (#N1-09) Architect Base Pipeline Data Classes
**Description:** You are the systems orchestrator. You must build the Python `dataclass` structures that Node 4 will use to load data, and Node 2/3 will use to read it.
**Sources:**
- Python 3.11 `dataclasses` standard library documentation.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N1-09-data-classes`.
- Write `challenges/quruntu/pipeline_router.py`. Define classes for `Pump`, `Reservoir`, and `TimePeriod`.
- Commit, push, and open a PR. Have Node 5 review and merge it.

### (#N1-10) Review Node 4's CP-SAT Baseline
**Description:** Ensure Node 4's classical Google OR-Tools setup correctly implements your multi-period constraints.
**Sources:**
- Node 4's open Pull Request.
**Acceptance Criteria:**
- Check out Node 4's branch locally. Execute their code. Ensure the mathematical logic matches your penalty models before approving the PR.

### (#N1-11) Review Node 2's D-Wave Ocean Architecture
**Description:** Ensure Node 2 is correctly translating your equations into `dimod` BQM objects.
**Sources:**
- Node 2's open Pull Request.
**Acceptance Criteria:**
- Check out Node 2's branch locally. Verify that the continuous/integer bounds mapping aligns with your reservoir constraint logic before approving the PR.
