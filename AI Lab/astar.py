import heapq

class State:
    def __init__(self, queens, heuristic):
        self.queens = queens
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.heuristic < other.heuristic

def is_safe(queens, row, col):
    for r, c in queens:
        if r == row or c == col or abs(r - row) == abs(c - col):
            return False
    return True

def calculate_heuristic(queens):
    conflicts = 0
    for i, (r1, c1) in enumerate(queens):
        for j, (r2, c2) in enumerate(queens):
            if i != j:
                if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                    conflicts += 1
    return conflicts // 2

def solve_n_queens(n):
    open_list = []
    initial_state = State([], 0)
    heapq.heappush(open_list, initial_state)

    while open_list:
        current_state = heapq.heappop(open_list)
        if len(current_state.queens) == n:
            return current_state.queens
        for col in range(n):
            if is_safe(current_state.queens, len(current_state.queens), col):
                new_queens = current_state.queens + [(len(current_state.queens), col)]
                heuristic = calculate_heuristic(new_queens)
                heapq.heappush(open_list, State(new_queens, heuristic))

    return None

if __name__ == "__main__":
    n = int(input("Enter the board size (N): "))
    solution = solve_n_queens(n)
    
    if solution:
        print("Solution found:")
        for row, col in solution:
            print("Q", end=" ")
            for c in range(n):
                if c != col:
                    print(".", end=" ")
                else:
                    print("Q", end=" ")
            print()
    else:
        print("No solution found.")
