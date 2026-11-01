from collections import deque
from data import NODES_D3, SOURCE_D3, SINK_D3, CAPACITY_MATRIX_D3


def bfs_augmenting_path(residual_capacity, source, sink, parent):
    """
    Mencari Augmenting Path dari Source ke Sink di Residual Graph menggunakan BFS (Edmonds-Karp).
    """
    visited = set([source])
    queue = deque([source])

    while queue:
        curr = queue.popleft()

        if curr == sink:
            return True

        for neighbor in residual_capacity[curr]:
            cap = residual_capacity[curr][neighbor]
            if neighbor not in visited and cap > 0:
                visited.add(neighbor)
                parent[neighbor] = curr
                queue.append(neighbor)

    return False


def edmonds_karp_max_flow(nodes, source, sink, capacity_matrix):
    """
    Algoritma Edmonds-Karp (Ford-Fulkerson berbasis BFS).
    Kompleksitas Waktu: O(V * E^2)
    """
    residual = {u: {v: 0 for v in nodes} for u in nodes}
    for u in nodes:
        for v in nodes:
            residual[u][v] = capacity_matrix[u][v]

    max_flow = 0
    augmenting_paths = []
    parent = {}

    iteration = 1
    while bfs_augmenting_path(residual, source, sink, parent):
        path = []
        curr = sink
        bottleneck = float("inf")

        while curr != source:
            prev = parent[curr]
            path.append(curr)
            bottleneck = min(bottleneck, residual[prev][curr])
            curr = prev

        path.append(source)
        path.reverse()

        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            residual[u][v] -= bottleneck
            residual[v][u] += bottleneck

        max_flow += bottleneck
        augmenting_paths.append((iteration, path, bottleneck))
        iteration += 1
        parent = {}

    return max_flow, augmenting_paths, residual


def run_task_5():
    print("=" * 65)
    print("TASK 5: MAXIMUM DAILY THROUGHPUT (NETWORK FLOW / EDMONDS-KARP)")
    print("=" * 65)

    print(f"Source (Titik Asal) : {SOURCE_D3} (Central Warehouse)")
    print(f"Sink (Titik Tujuan) : {SINK_D3} (Industrial Park)")

    max_flow_val, paths, final_residual = edmonds_karp_max_flow(
        NODES_D3, SOURCE_D3, SINK_D3, CAPACITY_MATRIX_D3
    )

    print("\n[JEJAK AUGMENTING PATHS & BOTTLENECK CAPACITY]")
    for iter_num, path, bottleneck in paths:
        path_str = " -> ".join(path)
        print(f" Iterasi #{iter_num}: Jalur [{path_str}] | Bottleneck Flow: {bottleneck} Ton/hari")

    print(f"\n=================================================")
    print(f" TOTAL MAXIMUM FLOW (W -> Y) : {max_flow_val} Ton / Hari")
    print(f"=================================================")

    print("\n" + "-" * 50)
    print("ANALISIS RESIDUAL NETWORK & MINIMUM CUT")
    print("-" * 50)
    print("Edge Kapasitas Utama Terpakai Penuh (Bottleneck Lanes):")
    for u in NODES_D3:
        for v in NODES_D3:
            orig_cap = CAPACITY_MATRIX_D3[u][v]
            if orig_cap > 0 and final_residual[u][v] == 0:
                print(f"  - Lane {u} -> {v}: Kapasitas {orig_cap} Ton/hari (Terguna Sempurna / Saturated)")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    run_task_5()