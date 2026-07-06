### Team Environment Setup (Strict Protocol)

We are standardizing on **Python 3.11**. Do not use Python 3.12. Do not use Conda for this repository. We are using the native `venv` module to ensure absolute parity across Mac, Linux, and Windows.

**Step 1: Create the Virtual Environment**
Open your terminal, navigate to the root of our cloned repository, and run:
`python3.11 -m venv .venv` 
*(Note: On Windows, you may just need to type `python -m venv .venv`)*

**Step 2: Activate the Environment**
You must do this every time you open a new terminal to work on this code.
* **Mac/Linux:** `source .venv/bin/activate`
* **Windows (Command Prompt):** `.venv\Scripts\activate.bat`
* **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
*(You will know it worked when your terminal prompt is prefixed with `(.venv)`).*

**Step 3: Install the Stack**
With the environment active, install our exact architecture:
`pip install --upgrade pip`
`pip install -r requirements.txt`

**Step 4: Verify the Ignore Rule**
Before you commit any code, run `git status`. If you see `.venv/` listed as an untracked file, **stop**. Add `.venv/` to the `.gitignore` file immediately. Never commit a virtual environment to GitHub.