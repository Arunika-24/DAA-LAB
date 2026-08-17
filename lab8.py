from itertools import permutations

INF = float('inf')


def tsp_brute_force(cost, n):
    """Brute force solution for TSP"""

    cities = list(range(1, n))

    best_cost = INF
    best_path = None

    for perm in permutations(cities):

        path = [0] + list(perm) + [0]

        current_cost = sum(
            cost[path[i]][path[i + 1]]
            for i in range(n)
        )

        if current_cost < best_cost:
            best_cost = current_cost
            best_path = path

    return best_path, best_cost


# 4-city cost matrix
cost = [
    [INF, 12, 10, 19],
    [12, INF, 3, 7],
    [10, 3, INF, 6],
    [19, 7, 6, INF]
]

n = 4

cities = ['P', 'Q', 'R', 'S']


# Find optimal tour
best_path, best_cost = tsp_brute_force(cost, n)


# Display cost matrix
print("4-City TSP - Cost Matrix:")

print(f"{'':>4}", ' '.join(f'{c:>5}' for c in cities))

for i, row in enumerate(cost):

    r = [
        'INF' if x == INF else str(x)
        for x in row
    ]

    print(
        f'{cities[i]:>4}',
        ' '.join(f'{v:>5}' for v in r)
    )


# Display optimal tour
print(
    f'\nOptimal Tour: '
    f'{" -> ".join(cities[i] for i in best_path)}'
)

print(f'Minimum Cost: {best_cost}')


# Verify each path
print('\nPath Verification:')

for i in range(n):

    u = best_path[i]
    v = best_path[i + 1]

    print(
        f' {cities[u]} -> {cities[v]}: '
        f'cost = {cost[u][v]}'
    )
