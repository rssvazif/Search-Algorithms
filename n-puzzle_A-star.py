
def heuristic(state, goal_state, n):
    distance = 0
    for num in range(1, n*n):  
        current_index = state.index(num)
        goal_index = goal_state.index(num)
        current_row, current_col = divmod(current_index, n)
        goal_row, goal_col = divmod(goal_index, n)
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance


def find_zero(state):
    return state.index(0)


def get_neighbors(state, n):
    zero_idx = find_zero(state)
    row, col = divmod(zero_idx, n)
    neighbors = []
    

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < n and 0 <= new_col < n:
            new_idx = new_row * n + new_col
            new_state = state[:]
            new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
            neighbors.append(new_state)
    return neighbors


def a_star(initial_state, goal_state, n):
    open_set = [(0, initial_state, [])]  
    visited = set() 

    while open_set:

        open_set.sort(key=lambda x: x[0])
        _, current_state, path = open_set.pop(0)  

        if current_state == goal_state:
            return path + [current_state]


        if tuple(current_state) not in visited:
            visited.add(tuple(current_state))


            for neighbor in get_neighbors(current_state, n):
                g = len(path) + 1  
                h = heuristic(neighbor, goal_state, n)  
                f = g + h  
                open_set.append((f, neighbor, path + [current_state]))

    return None  


def get_user_input():
    n = int(input("Enter the size of the grid (n) (e.g., 3 for a 3x3 grid): "))
    print(f"Enter the initial state ({n}x{n}) as a list:")
    initial_state = list(map(int, input().strip().split()))
    print(f"Enter the goal state ({n}x{n}) as a list:")
    goal_state = list(map(int, input().strip().split()))
    
    if len(initial_state) != n * n or len(goal_state) != n * n:
        raise ValueError("The number of elements does not match the grid size!")
    
    return n, initial_state, goal_state


if __name__ == "__main__":
    try:

        n, initial_state, goal_state = get_user_input()
        

        solution = a_star(initial_state, goal_state, n)
        if solution:
            print("Solution found:")
            for step in solution:
                for i in range(n):
                    print(step[i*n:(i+1)*n])
                print("-" * 10)
        else:
            print("The puzzle is unsolvable.")
    except ValueError as e:
        print(f"Error: {e}")
