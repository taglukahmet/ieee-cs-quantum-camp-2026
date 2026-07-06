# METU IEEE CS: Quantum Camp 2026

Welcome to the central incubator and training repository for the 2026 Teknofest Water Distribution Network Optimization Hackathon.

This environment is shared by two independent teams (Quruntu and Kararsızlıq). We operate on a strict 5-Node decoupled architecture, combining classical mixed-integer programming with D-Wave Quantum Annealing and IBM Qiskit gate-based hardware.

## The 5-Node Architecture
Both teams must strictly adhere to this division of labor.
1. **Formulation Architect:** Owns the pure mathematical physics and QUBO matrices.
2. **Annealing & Repair Engineer:** Owns the D-Wave Ocean SDK and local search repair algorithms.
3. **Gate-Based Architect:** Owns the IBM Qiskit QAOA / VQE execution.
4. **Classical Data Engineer:** Owns the JSON/CSV parsing and SciPy/OR-Tools baseline models.
5. **Systems Integrator:** Owns graph partitioning (NetworkX) and the final data pipeline.

## Environment Setup (Strict Protocol)

We are standardizing on Python 3.11.x. Do not use Python 3.12 or 3.13, as they lack stable pre-compiled wheels for the required quantum C++/Rust binaries. Do not use Conda; we enforce the native venv module for absolute cross-platform parity.

1. ### Create and Activate the Virtual Environment

Navigate to the root of the cloned repository:
```bash
python3.11 -m venv .venv
```

Activate it:

- **Mac/Linux:** `source .venv/bin/activate`
- **Windows (Cmd):** `.venv\Scripts\activate.bat`
- **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`

2. ### Install the Infrastructure

```bash
pip install --upgrade pip
pip install -r requirements.txt
pre-commit install
```

_Note:_ The `pre-commit install` command activates our automated repository defense. You cannot commit code that violates our file size constraints or contains syntax errors.

## Secrets & Telemetry (`.env`)

You must never hardcode API tokens into your Python scripts. This repository is protected by a fail-fast `config.py` gatekeeper.

1. Duplicate the `.env.example` file and rename the copy to strictly `.env`.
2. Add your personal tokens to the `.env` file.

```plaintext
# .env
GITHUB_TOKEN=your_personal_access_token
DWAVE_API_TOKEN=your_leap_token
IBM_QUANTUM_TOKEN=your_ibm_token
```

The `.env` file is already in our `.gitignore`. It will never be pushed to GitHub.

## The Command Center CLI (`quruntu_tracker.py`)

Do not manually read the curriculum markdown files. Use the built-in CLI routing engine to track your execution velocity, locate your next immediate bottleneck, and fetch live network blockers.

**Default Execution (Entire Quruntu Team):**
```bash
python quruntu_tracker.py
```

**Targeted Execution (Specific Team or Engineer):**
```bash
python quruntu_tracker.py kararsızlıq
python quruntu_tracker.py ahmet #any name or surname works as long as its in the CURRICULUM.md
```

**System Diagnostics (The Smoke Test):** Run this immediately after setting up your environment to verify that your C++ and Rust quantum bindings compiled correctly.
```bash
python quruntu_tracker.py --diagnose
```

“Code is read much more often than it is written.”
