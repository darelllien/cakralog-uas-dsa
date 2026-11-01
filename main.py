from dynamic_programming import run_task_1
from greedy import run_task_2
from mst import run_task_3
from shortest_path import run_task_4
from network_flow import run_task_5

def print_header():
    print("=" * 70)
    print("   CAKRALOG SMART LOGISTICS AND DISTRIBUTION OPTIMIZATION SYSTEM")
    print("   Final Project - Data Structures & Algorithms (IK306)")
    print("=" * 70)
    print("Executing all 5 optimization modules sequentially...\n")


def print_summary_integration():
    print("=" * 70)
    print("              INTEGRATED SYSTEM SUMMARY & EXECUTIVE REPORT")
    print("=" * 70)
    print("1. Infrastructure Upgrade Plan (Task 3 - MST):")
    print("   - Strategy: Kruskal / Prim Algorithm")
    print("   - Result  : Total cost Rp27 Million to connect all 6 locations (5 edges).")
    
    print("\n2. Fastest Transport Routes (Task 4 - Shortest Path):")
    print("   - Strategy: Floyd-Warshall & Bellman-Ford")
    print("   - Result  : Full time-matrix generated. Fastest W -> Y path takes 33 mins.")

    print("\n3. Budget Allocation (Task 1 - Dynamic Programming):")
    print("   - Strategy: 0/1 Knapsack DP")
    print("   - Result  : Allocated Rp10M budget to Option #3 & #4 achieving Max Value = 8.")

    print("\n4. Maximum Daily Throughput (Task 5 - Network Flow):")
    print("   - Strategy: Edmonds-Karp (Ford-Fulkerson + BFS)")
    print("   - Result  : Max daily throughput from W to Y is 14 Tons/day.")

    print("\n5. Loading Dock Schedule (Task 2 - Greedy Algorithm):")
    print("   - Strategy: Greedy Interval Scheduling (Earliest Finish Time)")
    print("   - Result  : Maximize 5 truck loading requests served out of 8 requests.")
    
    print("\n" + "-" * 70)
    print("IMPORTANT SYSTEM NOTE (INTEGRATION ASSUMPTIONS):")
    print("Each module optimizes a DIFFERENT objective based on its own dataset.")
    print("The algorithms function as complementary decision-support tools for management.")
    print("=" * 70 + "\n")


def main():
    print_header()
    
    run_task_1()
    run_task_2()
    run_task_3()
    run_task_4()
    run_task_5()
    
    print_summary_integration()


if __name__ == "__main__":
    main()