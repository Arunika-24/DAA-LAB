def matrix_chain_order(dims):
    """
    Matrix Chain Multiplication using DP
    dims: list of dimensions
    Matrix i has dims[i-1] x dims[i]
    """

    n = len(dims) - 1

    # m[i][j] = minimum multiplication cost for matrices i..j
    m = [[0] * (n + 1) for _ in range(n + 1)]

    # s[i][j] = position where the optimal split occurs
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # l = chain length
    for l in range(2, n + 1):

        for i in range(1, n - l + 2):
            j = i + l - 1

            m[i][j] = float('inf')

            for k in range(i, j):

                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + dims[i - 1] * dims[k] * dims[j]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):

    if i == j:
        return f"A{i}"

    k = s[i][j]

    left = print_optimal_parens(s, i, k)
    right = print_optimal_parens(s, k + 1, j)

    return f"({left} x {right})"


def print_dp_table(m, n):

    print("\nDP Cost Table m[i][j]:")

    print(f"{'':>6}", end="")

    for j in range(1, n + 1):
        print(f"{'A' + str(j):>9}", end="")

    print()

    for i in range(1, n + 1):

        print(f"{'A' + str(i):<6}", end="")

        for j in range(1, n + 1):

            if j < i:
                print(f"{'---':>9}", end="")
            else:
                print(f"{m[i][j]:>9}", end="")

        print()


# Matrix dimensions
dims = [5, 10, 15, 20, 25]

n = len(dims) - 1

print("Matrix Dimensions:")

for i in range(n):
    print(f" A{i + 1}: {dims[i]} x {dims[i + 1]}")


# Calculate minimum cost
m, s = matrix_chain_order(dims)

print(f"\nMinimum scalar multiplications: {m[1][n]}")

print(
    f"Optimal parenthesization: "
    f"{print_optimal_parens(s, 1, n)}"
)

# Print DP table
print_dp_table(m, n)
