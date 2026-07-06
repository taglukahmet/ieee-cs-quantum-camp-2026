import os
import sys
from dotenv import load_dotenv

# Load the .env file into the system's environment variables
load_dotenv()

class Config:
    """Centralized Configuration and Secrets Manager."""

    # Tracker Telemetry (Optional)
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

    # Quantum Hardware Tokens (Required for Execution)
    DWAVE_API_TOKEN = os.environ.get("DWAVE_API_TOKEN")
    IBM_QUANTUM_TOKEN = os.environ.get("IBM_QUANTUM_TOKEN")

    @classmethod
    def validate_tracker(cls):
        """Validates dependencies for the CLI Tracker."""
        if not cls.GITHUB_TOKEN:
            # We do not crash here; the tracker degrades gracefully.
            pass

    @classmethod
    def validate_dwave(cls):
        """Violently crashes if D-Wave tokens are missing before cloud execution."""
        if not cls.DWAVE_API_TOKEN:
            print("\n[FATAL ERROR] DWAVE_API_TOKEN is missing!")
            print("You cannot submit jobs to the LeapHybridCQMSolver without authentication.")
            print("Action required: Add your token to the local .env file.\n")
            sys.exit(1)

    @classmethod
    def validate_ibm(cls):
        """Violently crashes if IBM Quantum tokens are missing before cloud execution."""
        if not cls.IBM_QUANTUM_TOKEN:
            print("\n[FATAL ERROR] IBM_QUANTUM_TOKEN is missing!")
            print("You cannot execute Qiskit circuits on IBM hardware without authentication.")
            print("Action required: Add your token to the local .env file.\n")
            sys.exit(1)
