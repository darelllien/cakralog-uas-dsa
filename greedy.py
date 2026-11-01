from data import DOCK_REQUESTS_D5

def solve_dock_scheduling_greedy(requests):
    """
    Menyelesaikan masalah Interval Scheduling dengan strategi Greedy.
    
    Greedy Rule: Pilih aktivitas yang selesai paling awal (Earliest Finish Time)
    yang kompatibel dengan jadwal yang sudah terpilih sebelumnya.
    """

    sorted_requests = sorted(requests, key=lambda x: x[2])

    selected_schedule = []
    last_finish_time = float("-inf")

    for req_id, start, end in sorted_requests:
        if start >= last_finish_time:
            selected_schedule.append((req_id, start, end))
            last_finish_time = end

    return selected_schedule


def run_task_2():
    print("=" * 65)
    print("TASK 2: LOADING DOCK SCHEDULING (GREEDY INTERVAL SCHEDULING)")
    print("=" * 65)

    print(f"Total Permintaan Masuk (D5) : {len(DOCK_REQUESTS_D5)} Permintaan")

    selected = solve_dock_scheduling_greedy(DOCK_REQUESTS_D5)

    print(f"Jumlah Permintaan Dilayani  : {len(selected)} Permintaan (Maksimal)")
    print("\nJadwal Loading Dock Terpilih (Urutan Earliest Finish Time):")
    for req_id, start, end in selected:
        print(f"  - {req_id}: Jam {start:02d}:00 - {end:02d}:00 (Durasi: {end - start} jam)")

    print("\n" + "-" * 50)
    print("ANALISIS VALIDITAS & KETERBATASAN GREEDY (TASK 2)")
    print("-" * 50)
    print("1. Justifikasi Validitas (Exchange Argument):")
    print("   Memilih aktivitas yang selesai paling awal menyisakan ruang waktu")
    print("   terluas untuk aktivitas berikutnya, sehingga dijamin optimal")
    print("   dalam memaksimalkan JUMLAH (count) aktivitas.")
    print("\n2. Kondisi Di Mana Greedy Bisa Gagal:")
    print("   Jika setiap permintaan memiliki bobot/prioritas bernilai beda")
    print("   (Weighted Interval Scheduling), aturan Earliest Finish Time akan gagal")
    print("   dan memerlukan pendekatan Dynamic Programming.")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    run_task_2()