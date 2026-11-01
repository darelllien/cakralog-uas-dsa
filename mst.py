import heapq
from data import LOCATIONS_D1, ROADS_D1

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
            return True
        return False


def kruskal_mst(vertices, edges):
    """
    Algoritma Kruskal menggunakan Disjoint Set Union (DSU).
    Kompleksitas Waktu: O(E log E)
    """
    sorted_edges = sorted(edges, key=lambda x: x[2])
    dsu = DisjointSet(vertices)

    mst_edges = []
    total_cost = 0

    for u, v, weight in sorted_edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_cost += weight

    is_connected = len(mst_edges) == len(vertices) - 1
    return mst_edges, total_cost, is_connected

def prim_mst(vertices, edges, start_vertex="W"):
    """
    Algoritma Prim menggunakan Priority Queue (Min-Heap).
    Kompleksitas Waktu: O(E log V)
    """
    if not vertices:
        return [], 0, False

    adj = {v: [] for v in vertices}
    for u, v, weight in edges:
        adj[u].append((v, weight))
        adj[v].append((u, weight))

    visited = set()
    mst_edges = []
    total_cost = 0

    min_heap = []

    def visit(node):
        visited.add(node)
        for neighbor, weight in adj[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, node, neighbor))

    visit(start_vertex)

    while min_heap and len(visited) < len(vertices):
        weight, u, v = heapq.heappop(min_heap)
        if v not in visited:
            mst_edges.append((u, v, weight))
            total_cost += weight
            visit(v)

    is_connected = len(visited) == len(vertices)
    return mst_edges, total_cost, is_connected


def run_task_3():
    print("=" * 65)
    print("TASK 3: INFRASTRUCTURE AT MINIMUM COST (MINIMUM SPANNING TREE)")
    print("=" * 65)

    print(f"Total Lokasi (Vertices) : {len(LOCATIONS_D1)} (W, N, S, H, X, Y)")
    print(f"Total Opsi Jalan (Edges): {len(ROADS_D1)} Jalan Tak Berarah")

    kruskal_edges, kruskal_cost, k_valid = kruskal_mst(LOCATIONS_D1, ROADS_D1)

    print("\n[HASIL ALGORITMA KRUSKAL]")
    print(f"Total Biaya Upgrade Jalan : Rp{kruskal_cost} Juta")
    print(f"Jumlah Edge Digunakan     : {len(kruskal_edges)} (Syarat V-1 = {len(LOCATIONS_D1)-1})")
    print("Daftar Jalan Terpilih (Kruskal):")
    for u, v, w in kruskal_edges:
        print(f"  - Jalan {u} <---> {v} (Biaya: Rp{w}M)")

    prim_edges, prim_cost, p_valid = prim_mst(LOCATIONS_D1, ROADS_D1, start_vertex="W")

    print("\n[HASIL ALGORITMA PRIM (Start: W)]")
    print(f"Total Biaya Upgrade Jalan : Rp{prim_cost} Juta")
    print("Daftar Jalan Terpilih (Prim):")
    for u, v, w in prim_edges:
        print(f"  - Jalan {u} <---> {v} (Biaya: Rp{w}M)")

    print("\n" + "-" * 50)
    print("PENGUJIAN EDGE CASE: DISCONNECTED GRAPH (GRAF TERPUTUS)")
    print("-" * 50)
    disc_vertices = ["A", "B", "C", "D"]
    disc_edges = [("A", "B", 1), ("C", "D", 2)]
    _, disc_cost, disc_valid = kruskal_mst(disc_vertices, disc_edges)

    print(f"Menguji Graf Terputus : Vertices {disc_vertices}, Edges {disc_edges}")
    print(f"Apakah MST Terbentuk? : {disc_valid} (Sesuai Ekspektasi: Terdeteksi Terputus)")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    run_task_3()