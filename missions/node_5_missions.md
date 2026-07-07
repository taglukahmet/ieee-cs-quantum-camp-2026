# MISSION DETAILS: NODE 5 (Ekin Ağardan)

### (#N5-01) NetworkX Fundamentals & Graph Instantiation
**Description:** You are the architect of the physical map. You must understand how to translate water sources, reservoirs, and transmission lines into mathematical nodes and edges.
**Sources:**
- NetworkX Documentation: "Basic Graph Types" and "Nodes & Edges".
**Acceptance Criteria:**
- Verbally explain the difference between a directed and undirected graph.
- Write a 5-line Python snippet in the terminal that creates a graph with 3 nodes and assigns a "weight" to the edges connecting them.

### (#N5-02) Graph Partitioning Algorithms (METIS Concepts)
**Description:** The quantum computers cannot process the entire city at once. You must cut the city-wide graph into smaller sub-graphs.
**Sources:**
- NetworkX Documentation: `networkx.algorithms.community`.
- Karypis Lab METIS algorithm documentation (Concepts only).
**Acceptance Criteria:**
- Explain how graph partitioning algorithms attempt to minimize the "edge cut" (the number of transmission lines severed to divide the graph).

### (#N5-03) Boundary Integrity & Overlapping Buffer Zones
**Description:** If you cut the network without overlapping the boundaries, Node 1's mathematics will fail at the border lines[cite: 1]. You must learn how to partition with overlapping buffer zones[cite: 1].
**Sources:**
- Network flow decomposition theory / Benders Decomposition concepts[cite: 1].
**Acceptance Criteria:**
- Diagram on a whiteboard how two sub-graphs can share a single "buffer reservoir" node, ensuring that both quantum models factor in the boundary pressure correctly.

### (#N5-04) Multi-Objective Pareto Optimization Logic
**Description:** The hackathon does not have a single "right" answer. You are balancing energy costs against demand risks[cite: 1]. You must map the trade-offs.
**Sources:**
- Optimization Literature: "Pareto Front" and "Multi-Objective Trade-offs".
**Acceptance Criteria:**
- Sketch a Pareto Front graph on a whiteboard.
- Explain why a solution resting *on* the Pareto curve is mathematically superior to a solution resting *inside* the curve.

### (#N5-05) Build Multi-Period Topological Maps (NetworkX)
**Description:** Time to digitize the physical layout. You will take the raw JSON data parsed by Node 4 and turn it into a multi-period graph structure[cite: 1].
**Sources:**
- Node 4's standardized data dictionaries.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N5-05-networkx-mapping`.
- Write `challenges/quruntu/graph_builder.py`. Instantiate a NetworkX graph containing labeled `Source`, `Reservoir`, and `Consumption Zone` nodes.
- Commit, push, open a Pull Request, and have Node 4 review it.

### (#N5-06) Build Overlapping Sub-Graph Partitioner
**Description:** Write the script that takes a massive NetworkX graph and slices it into computationally viable chunks for the D-Wave hardware.
**Sources:**
- Your theory notes from N5-03.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N5-06-graph-partitioner`.
- Write `challenges/quruntu/graph_cutter.py`. The function must take a 10-node graph and output two 6-node sub-graphs (with a 2-node overlapping boundary).
- Commit, push, open a Pull Request, and have Node 1 verify the math.

### (#N5-07) Build Pareto Evaluation Engine (Energy vs. Demand)
**Description:** This script will be the final step of the pipeline. It takes the quantum and classical answers and plots their efficiency.
**Sources:**
- Matplotlib / SciPy documentation.
**Acceptance Criteria:**
- Create branch: `git checkout -b task/N5-07-pareto-engine`.
- Write `challenges/quruntu/pareto_evaluator.py`. Map simulated energy costs against simulated demand failure risks on a 2D plot.
- Commit, push, and merge via PR.

### (#N5-08) Review Node 1's Base Pipeline Data Classes
**Description:** Node 1 is building the orchestrator logic. You must ensure the data classes they define map cleanly to your NetworkX node attributes.
**Sources:**
- Node 1's open Pull Request (`pipeline_router.py`).
**Acceptance Criteria:**
- Check out Node 1's branch. Review their `dataclass` structure. Verify that attributes like `max_capacity` and `current_volume` are accessible for your graph builder before approving the PR.

### (#N5-09) Review Node 4's JSON Data Ingestion Structures
**Description:** You are the consumer of Node 4's data. If they format it poorly, your NetworkX builder will crash.
**Sources:**
- Node 4's open Pull Request (`data_loader.py`).
**Acceptance Criteria:**
- Check out Node 4's branch. Print their dictionary outputs. Ensure you can seamlessly iterate through their keys to generate your graph edges before approving the PR.
