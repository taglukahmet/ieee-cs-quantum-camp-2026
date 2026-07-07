import re
import sys
import os
import argparse
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
from dotenv import load_dotenv
from config import Config
from rich.markdown import Markdown

# Graceful degradation if PyGithub is missing
try:
    from github import Github, Auth
    GITHUB_AVAILABLE = True
except ImportError:
    GITHUB_AVAILABLE = False

REPO_NAME = "taglukahmet/ieee-cs-quantum-camp-2026"

def fetch_live_telemetry():
    """Fetches open PRs and Issues from the GitHub API using an environment token."""
    if not GITHUB_AVAILABLE:
        return None, "PyGithub not installed."

    token = Config.GITHUB_TOKEN
    if not token:
        return None, "GITHUB_TOKEN environment variable not set."

    try:
        auth = Auth.Token(token)
        g = Github(auth=auth)
        repo = g.get_repo(REPO_NAME)

        pulls = repo.get_pulls(state='open')
        issues = repo.get_issues(state='open')

        real_issues = [i for i in issues if i.pull_request is None]

        return {"prs": list(pulls), "issues": list(real_issues)}, None
    except Exception as e:
        return None, str(e)

def parse_curriculum(file_path: str, target: str) -> dict:
    """Parses markdown dynamically based on team name or member name."""
    content = Path(file_path).read_text(encoding="utf-8")
    pattern = re.compile(r"- \[( |x|X)\](?:\s*\`?\[(\d+)[hH]\]\`?)?\s*(.*)")

    stats = {}
    current_node = None
    target_upper = target.upper()
    in_target_team = False
    tracking_mode = None

    for line in content.splitlines():
        # Check if the target matches a Team header
        if line.upper().startswith("## TEAM:"):
            team_name = line.split(":")[-1].strip().upper()
            if target_upper in team_name:
                in_target_team = True
                tracking_mode = "TEAM"
            else:
                in_target_team = False
            continue

        if line.upper().startswith("### NODE") or line.upper().startswith("### MEMBER"):
            node_name = line.split("(")[-1].replace(")", "").strip()

            # Dynamic Routing: If target matches a specific user, isolate them.
            if target_upper in node_name.upper():
                current_node = node_name
                tracking_mode = "USER"
            # Otherwise, if we are in the target team block, track everyone in it.
            elif tracking_mode == "TEAM" and in_target_team:
                current_node = node_name
            else:
                current_node = None
                continue

            stats[current_node] = {
                "hours_completed": 0,
                "hours_total": 0,
                "next_action": None
            }
            continue

        if current_node:
            match = pattern.search(line)
            if match:
                is_checked = match.group(1).lower() == "x"
                hours = int(match.group(2)) if match.group(2) else 1
                task_text = match.group(3)

                stats[current_node]["hours_total"] += hours

                if is_checked:
                    stats[current_node]["hours_completed"] += hours
                elif stats[current_node]["next_action"] is None:
                    stats[current_node]["next_action"] = f"[{hours}h] {task_text}"

    return stats

def render_dashboard(stats: dict, target: str, telemetry: dict, telemetry_error: str):
    console = Console()

    if not stats:
        console.print(f"[bold red]Error: No data found for target '{target}'. Check spelling.[/]")
        return

    # 1. Local Velocity Table
    table = Table(title=f"[bold blue]{target.upper()} : EXECUTION VELOCITY[/]", box=box.MINIMAL_DOUBLE_HEAD)
    table.add_column("Engineer", style="cyan", no_wrap=True)
    table.add_column("Burnup", justify="right", style="magenta")
    table.add_column("Progress", style="green")

    for node, data in stats.items():
        total = data["hours_total"]
        if total == 0: continue
        completed = data["hours_completed"]
        percentage = (completed / total) * 100

        bar_length = 20
        filled = int((percentage / 100) * bar_length)
        bar = f"[{'█' * filled}{'░' * (bar_length - filled)}]"
        table.add_row(node, f"{completed}h / {total}h", f"{bar} {percentage:.1f}%")

    console.print()
    console.print(table)
    console.print()

    # 2. Live GitHub Telemetry
    if telemetry:
        prs = telemetry["prs"]
        issues = telemetry["issues"]
        if prs or issues:
            telemetry_table = Table(title="[blink bold red]LIVE NETWORK BLOCKERS[/]", box=box.SIMPLE_HEAVY)
            telemetry_table.add_column("Type", style="red")
            telemetry_table.add_column("Title", style="white")
            telemetry_table.add_column("Author", style="cyan")

            for pr in prs:
                telemetry_table.add_row("PULL REQUEST", pr.title, pr.user.login)
            for issue in issues:
                telemetry_table.add_row("ISSUE", issue.title, issue.user.login)

            console.print(telemetry_table)
            console.print()
    elif telemetry_error:
        console.print(f"[dim italic]Live telemetry offline: {telemetry_error}[/]")
        console.print()

    # 3. Active Missions
    console.print("[bold yellow]ACTIVE MISSIONS (NEXT IMMEDIATE BOTTLENECK)[/]")
    for node, data in stats.items():
        if data["next_action"]:
            action_text = data["next_action"]
            if "[" in action_text and "]" in action_text and "h]" not in action_text.split()[0]:
                action_text = re.sub(r"\[(.*?)\]", r"[bold red][\1][/]", action_text)

            panel = Panel(
                Text.from_markup(action_text),
                title=f"[bold cyan]{node}[/]", title_align="left", border_style="cyan", padding=(1, 2)
            )
            console.print(panel)


def test_numpy():
    import numpy as np
    # Verifies core C-extensions are operational
    matrix = np.array([[1, 0], [0, 1]])
    np.linalg.eigvals(matrix)

def test_dwave():
    import dimod
    # Verifies the Ocean SDK binary quadratic modeler compiles
    bqm = dimod.BinaryQuadraticModel({'x': 1}, {}, 0, 'BINARY')

def test_qiskit():
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    # Verifies Qiskit Rust bindings and local simulation mechanics
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.measure_all()
    sim = AerSimulator()
    sim.run(qc).result()

def test_ortools():
    from ortools.linear_solver import pywraplp
    # Verifies Google's C++ solver wrappers
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        raise RuntimeError("GLOP solver failed to initialize.")

def run_diagnostics():
    """Executes all isolated smoke tests and catches compilation errors."""
    console = Console()
    console.print(Panel("[bold cyan]SYSTEM DIAGNOSTICS: LOCAL ENVIRONMENT VALIDATION[/]", style="cyan"))
    console.print()

    tests = [
        ("Core Mathematics (NumPy)", test_numpy),
        ("Quantum Annealing (D-Wave Ocean)", test_dwave),
        ("Gate-Based Quantum (Qiskit & Aer)", test_qiskit),
        ("Classical Optimization (OR-Tools)", test_ortools)
    ]

    all_passed = True
    for name, test_func in tests:
        try:
            test_func()
            console.print(f"[bold green]✓ PASS[/] {name}")
        except ImportError as e:
            console.print(f"[bold red]✗ FAIL[/] {name} [dim](Missing Library: {e})[/]")
            all_passed = False
        except Exception as e:
            console.print(f"[bold red]✗ FAIL[/] {name}")
            console.print(f"  [dim red]Runtime/Binary Error: {str(e)}[/]")
            all_passed = False

    console.print()
    if all_passed:
        console.print("[bold green]ALL SYSTEMS OPTIMAL. Hardware dependencies are securely linked.[/]")
    else:
        console.print("[bold red]ENVIRONMENT FAULT DETECTED. Check your virtual environment and requirements.txt.[/]")
        sys.exit(1)

def render_current_mission(task_string):
    """Parses a task tag and renders the highly detailed mission from the missions directory."""
    console = Console()

    # 1. Regex to extract the tag format: e.g., (#N1-01)
    match = re.search(r'\(#(N[1-5])-(\d+)\)', task_string)
    if not match:
        console.print("[red]Error: No valid mission tag found on the current task.[/]")
        return

    node_id = match.group(1)
    node_num = node_id[1]
    full_tag = match.group(0)

    # 2. Dynamic File Routing
    mission_file = Path(f"missions/node_{node_num}_missions.md")
    if not mission_file.exists():
        console.print(f"[red]Error: Mission file {mission_file} not found.[/]")
        return

    # 3. Block Extraction
    with open(mission_file, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        # Split the document at the specific tag header
        block_start = content.split(f"### {full_tag}")[1]
        mission_raw = block_start.split("### (#")[0].strip()

        # 4. Format the Markdown (Fixing the margin collapse)
        # We inject double newlines to force Rich to recognize them as distinct blocks
        mission_raw = mission_raw.replace("**Description:**", "\n\n**Description:**\n")
        mission_raw = mission_raw.replace("**Sources:**", "\n\n**Sources:**\n")
        mission_raw = mission_raw.replace("**Acceptance Criteria:**", "\n\n**Acceptance Criteria:**\n")

        # Isolate the title from the rest of the body
        lines = mission_raw.strip().split('\n')
        title = lines[0].strip()
        body = '\n'.join(lines[1:]).strip()

        # Reconstruct a clean markdown string
        final_markdown = f"## {title}\n{body}"

        # 5. Terminal Rendering (Added padding for better UI margins)
        header = f"[bold cyan]ACTIVE MISSION: {full_tag}[/]"
        console.print(Panel(Markdown(final_markdown), title=header, border_style="cyan", padding=(1, 2)))

    except IndexError:
        console.print(f"[red]Error: Tag {full_tag} not found in {mission_file}[/]")

def get_active_mission_string(filepath, target):
    """Isolates the target's markdown block and returns the first unchecked task string."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_target_block = False
    for line in lines:
        # Detect the start of the target's specific block
        if line.startswith("### Node ") and target.lower() in line.lower():
            in_target_block = True
            continue
        # Detect if we have bled into the next team member's block
        elif in_target_block and line.startswith("### Node "):
            break

        # Return the first uncompleted task
        if in_target_block and "- [ ]" in line:
            return line.strip()

    return None


if __name__ == "__main__":

    # The CLI Argument Parser
    parser = argparse.ArgumentParser(description="Quruntu Command Center")
    parser.add_argument("target", nargs="?", default="Quruntu", help="Team name or specific member name")
    parser.add_argument("--diagnose", action="store_true", help="Run local environment smoke tests")
    parser.add_argument("--current", action="store_true", help="Find the current task decription based on the name")
    args = parser.parse_args()

    # Route 1: Run Diagnostics and Exit
    if args.diagnose:
        run_diagnostics()
        sys.exit(0)

    file_path = "curriculum/CURRICULUM.md"
    if not Path(file_path).exists():
        print(f"Error: Could not find {file_path}")
        sys.exit(1)

    # Route 2: Render Current Mission Details and Exit
    if args.current:
        # Require a specific engineer to be targeted, not the whole team
        if args.target.lower() in ["quruntu", "kararsizlik", "kararsızlıq"]:
            print("Error: You must specify an individual engineer (e.g., 'Ahmet') to use the --current flag.")
            sys.exit(1)

        active_task_string = get_active_mission_string(file_path, args.target)
        if active_task_string:
            render_current_mission(active_task_string)
        else:
            print(f"No active missions found for {args.target}.")
        sys.exit(0)

    # Route 3: Standard Tracker Dashboard
    parsed_data = parse_curriculum(file_path, target=args.target)
    telemetry_data, error = fetch_live_telemetry()
    render_dashboard(parsed_data, args.target, telemetry_data, error)
