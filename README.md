# CakraLog - Smart Logistics & Distribution Optimization System
**Final Project: Data Structures & Algorithms (IK306)**  
*Universitas Cakrawala - Semester Ganjil 2026/2027*

---

## 📌 Deskripsi Proyek
CakraLog merupakan sistem pendukung keputusan (Decision Support Engine) berbasis algoritma pemodelan graf dan optimasi diskret untuk memecahkan 5 tantangan operasional logistik:
1. **Task 1: Budget Allocation** – Pemanfaatan anggaran modal Rp10 Juta menggunakan *0/1 Knapsack Dynamic Programming*.
2. **Task 2: Dock Scheduling** – Penjadwalan antrean truk *loading dock* tunggal menggunakan *Greedy Interval Scheduling (Earliest Finish Time)*.
3. **Task 3: Infrastructure Upgrade** – Rancangan perbaikan jalur jalan fisik minimal menggunakan *Minimum Spanning Tree (Kruskal & Prim)*.
4. **Task 4: Route Analysis** – Penentuan rute transit tercepat dan deteksi siklus negatif menggunakan *Floyd-Warshall* dan *Bellman-Ford*.
5. **Task 5: Maximum Throughput** – Maksimasi debit kargo harian dari Gudang Utama ke Terminal Kawasan Industri menggunakan *Edmonds-Karp Network Flow*.

---

## 📁 Struktur Repositori
```text
.
├── data.py                 # Dataset resmi (D1 - D5) dan graf pengujian sintetis (T1, T2)
├── dynamic_programming.py  # Modul Task 1: 0/1 Knapsack DP & perbandingan Greedy
├── greedy.py               # Modul Task 2: Greedy Interval Scheduling
├── mst.py                  # Modul Task 3: Kruskal (DSU) & Prim MST
├── shortest_path.py        # Modul Task 4: Floyd-Warshall & Bellman-Ford
├── network_flow.py         # Modul Task 5: Edmonds-Karp Max Flow (BFS Augmenting Path)
├── main.py                 # Runner utama & penggabung laporan eksekutif
├── .gitignore              # Konfigurasi pengabaian file Git
└── README.md               # Dokumentasi proyek