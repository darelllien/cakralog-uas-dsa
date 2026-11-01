from data import BUDGET_D4, UPGRADE_OPTIONS_D4


def solve_knapsack_dp(budget, items):
    """
    Menyelesaikan 0/1 Knapsack dengan Bottom-Up Dynamic Programming.
    
    State: dp[i][w] = nilai maksimum dari i item pertama dengan kapasitas budget w
    """
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Mengisi tabel DP
    for i in range(1, n + 1):
        item_id, name, cost, value = items[i - 1]
        for w in range(budget + 1):
            if cost > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(
                    dp[i - 1][w],
                    value + dp[i - 1][w - cost]
                )

    max_value = dp[n][budget]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_id, name, cost, value = items[i - 1]
            selected_items.append(items[i - 1])
            w -= cost

    selected_items.reverse() 
    total_cost = sum(item[2] for item in selected_items)

    return max_value, total_cost, selected_items, dp


def solve_knapsack_greedy(budget, items):
    """
    Simulasi pendekatan Greedy berbasis rasio (Value / Cost) tertinggi.
    Digunakan untuk perbandingan pada laporan teknis.
    """
   
    sorted_items = sorted(items, key=lambda x: x[3] / x[2], reverse=True)

    selected_items = []
    total_cost = 0
    total_value = 0

    for item in sorted_items:
        item_id, name, cost, value = item
        if total_cost + cost <= budget:
            selected_items.append(item)
            total_cost += cost
            total_value += value

    return total_value, total_cost, selected_items


def run_task_1():
    print("=" * 65)
    print("TASK 1: BUDGET ALLOCATION WITH DYNAMIC PROGRAMMING (0/1 KNAPSACK)")
    print("=" * 65)

    dp_val, dp_cost, dp_selected, dp_table = solve_knapsack_dp(BUDGET_D4, UPGRADE_OPTIONS_D4)

    print(f"Target Budget           : Rp{BUDGET_D4} Juta")
    print(f"Total Cost Terpakai (DP): Rp{dp_cost} Juta")
    print(f"Total Value Skor (DP)   : {dp_val}")
    print("\nOpsi Upgrade Terpilih (DP Optimal):")
    for item in dp_selected:
        print(f"  - Opsi #{item[0]}: {item[1]} (Cost: Rp{item[2]}M, Value: {item[3]})")

    gr_val, gr_cost, gr_selected = solve_knapsack_greedy(BUDGET_D4, UPGRADE_OPTIONS_D4)
    print("\n" + "-" * 50)
    print("ANALISIS PERBANDINGAN: GREEDY (VALUE PER COST RULE)")
    print("-" * 50)
    print(f"Total Cost (Greedy)     : Rp{gr_cost} Juta")
    print(f"Total Value (Greedy)    : {gr_val}")
    print("Opsi Upgrade Terpilih (Greedy):")
    for item in gr_selected:
        ratio = item[3] / item[2]
        print(f"  - Opsi #{item[0]}: {item[1]} (Cost: Rp{item[2]}M, Value: {item[3]}, Ratio: {ratio:.2f})")

    print("\n--> EVALUASI HASIL:")
    if dp_val > gr_val:
        print(f"    Strategi Greedy GAGAL mencapai hasil optimal! (DP = {dp_val} vs Greedy = {gr_val})")
    elif dp_val == gr_val:
        print(f"    Pada D4, Greedy kebetulan menghasilkan nilai sama, namun secara teori 0/1 Knapsack tidak dijamin optimal oleh Greedy.")

    print("=" * 65 + "\n")


if __name__ == "__main__":
    run_task_1()