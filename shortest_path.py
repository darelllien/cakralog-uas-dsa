from data import LOCATIONS_D2, ROUTES_D2, NODES_T1_T2, GRAPH_T1, GRAPH_T2

def floyd_warshall(vertices, edges):
    """
    Algoritma Floyd-Warshall untuk mencari rute terpendek antar semua pasangan.
    Kompleksitas Waktu: O(V^3), Ruang: O(V^2)
    """
    INF = float("inf")
    dist = {u: {v: INF for v in vertices} for u in vertices}
    next_node = {u: {v: None for v in vertices} for u in vertices}

    for u in vertices:
        dist[u][u] = 0

    for u, v, weight in edges:
        dist[u][v] = weight
        next_node[u][v] = v

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node


def reconstruct_path(u, v, next_node):
    """Memulihkan jalur rute tercepat dari u ke v."""
    if next_node[u][v] is None:
        return []
    path = [u]
    curr = u
    while curr != v:
        curr = next_node[curr][v]
        path.append(curr)
    return path

def bellman_ford(vertices, edges, source):
    """
    Algoritma Bellman-Ford dengan deteksi Negative Cycle.
    Kompleksitas Waktu: O(V * E)
    """
    INF = float("inf")
    dist = {v: INF for v in vertices}
    predecessor = {v: None for v in vertices}
    dist[source] = 0
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if dist[u] != INF and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                predecessor[v] = u

    has_negative_cycle = False
    for u, v, weight in edges:
        if dist[u] != INF and dist[u] + weight < dist[v]:
            has_negative_cycle = True
            break

    return dist, predecessor, has_negative_cycle


def run_task_4():
    print("=" * 65)
    print("TASK 4: ROUTE ANALYSIS (SHORTEST PATH ALGORITHMS)")
    print("=" * 65)

    print("[1. HASIL FLOYD-WARSHALL (ALL-PAIRS SHORTEST PATHS)]")
    dist_matrix, next_matrix = floyd_warshall(LOCATIONS_D2, ROUTES_D2)

    print("\nTabel Waktu Tempuh Tercepat (dalam Menit):")
    header = f"{'From/To':<8}" + "".join([f"{v:>8}" for v in LOCATIONS_D2])
    print(header)
    print("-" * len(header))

    for u in LOCATIONS_D2:
        row_str = f"{u:<8}"
        for v in LOCATIONS_D2:
            val = dist_matrix[u][v]
            if val == float("inf"):
                row_str += f"{'INF':>8}"
            else:
                row_str += f"{val:>8}"
        print(row_str)

    sample_src, sample_dest = "W", "Y"
    sample_path = reconstruct_path(sample_src, sample_dest, next_matrix)
    print(f"\nContoh Rute Tercepat {sample_src} -> {sample_dest}:")
    print(f"  - Jalur  : {' -> '.join(sample_path)}")
    print(f"  - Waktu  : {dist_matrix[sample_src][sample_dest]} Menit")

    print("\n" + "-" * 50)
    print("PENGUJIAN EDGE CASE: UNREACHABLE PAIR (RUTE TAK TERJANGKAU)")
    print("-" * 50)
    unreachable_src, unreachable_dest = "X", "W"
    unreachable_dist = dist_matrix[unreachable_src][unreachable_dest]
    print(f"Rute dari {unreachable_src} ke {unreachable_dest} (Toko ke Gudang Utama):")
    print(f"  - Status Waktu Tempuh : {unreachable_dist} (Terdeteksi Tidak Ada Akses Balik)")

    print("\n" + "-" * 50)
    print("DEMONSTRASI BELLMAN-FORD: NEGATIVE EDGE & CYCLE DETECTION")
    print("-" * 50)

    dist_t1, _, cycle_t1 = bellman_ford(NODES_T1_T2, GRAPH_T1, source="A")
    print(f"Graf T1 (Dengan Negative Edge -3):")
    print(f"  - Jarak Terpendek dari A : {dist_t1}")
    print(f"  - Terdeteksi Negative Cycle? : {cycle_t1} (Sesuai Ekspektasi: Aman)")

    dist_t2, _, cycle_t2 = bellman_ford(NODES_T1_T2, GRAPH_T2, source="A")
    print(f"\nGraf T2 (T1 + Edge D -> B (-1) -> Membentuk Negative Cycle):")
    print(f"  - Terdeteksi Negative Cycle? : {cycle_t2} (Sesuai Ekspektasi: Terdeteksi Siklus Negatif!)")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    run_task_4()