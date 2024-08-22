from collections import deque


def solve(n, m, distances, mapping):
    """
    Finds the shortest route for the delivery driver.

    Args:
        n: The number of customers.
        m: The number of known distances between customers.
        distances: A 2D list representing distances between locations.
        mapping: A dictionary mapping customer IDs to their indices in the distances matrix.

    Returns:
        The shortest route distance, or -1 if no route is found.
    """

    # Initialize a matrix to store shortest distances for all combinations of visited customers
    f = [[None] * (n + 1) for _ in range(1 << n)]  # 2D list with size (2^n) x (n+1)

    # Queue to store possible states during exploration (current state, current location, current distance)
    queue = deque([(0, 0, 0)])  # (visited_state, current_customer, distance)

    # Set distance to depot (location 0) as 0 for the initial state
    f[0][0] = 0

    while queue:
        state, current_customer, current_distance = queue.popleft()

        # Explore all unvisited neighbors
        for next_customer in range(n + 1):
            if next_customer != current_customer and distances[current_customer][next_customer] is not None:
                next_state = state
                # Update visited state (set corresponding bit to 1)
                if next_customer != 0:
                    next_state |= 1 << (next_customer - 1)

                # Update distance and state if a shorter path is found
                if f[next_state][next_customer] is None or f[next_state][next_customer] > current_distance + \
                        distances[current_customer][next_customer]:
                    f[next_state][next_customer] = current_distance + distances[current_customer][next_customer]
                    queue.append((next_state, next_customer, f[next_state][next_customer]))

    # Check if all customers have been visited (final state)
    if f[(1 << n) - 1][0] is None:
        return -1

    # Return the shortest distance to reach all customers and return to depot
    return f[(1 << n) - 1][0]


# Read input
n, m = map(int, input().split())

distances = [[None] * (n + 1) for _ in range(n + 1)]  # Initialize distances matrix
mapping = {}  # Map customer IDs to their indices

for i in range(1, n + 1):
    uid,d = map(int, input().split())
    mapping[uid] = i
    distances[0][i] = distances[i][0] = d

for _ in range(m):
    x, y, d = map(int, input().split())
    x = mapping[x]
    y = mapping[y]
    distances[x][y] = distances[y][x] = d

# Find and print the shortest route distance
shortest_distance = solve(n, m, distances, mapping)
print(shortest_distance)
