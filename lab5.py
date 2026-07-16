import random

# Global comparison counter
comparison_count = 0


# ---------- Divide and Conquer ----------

def min_max_dc(arr, low, high):

    global comparison_count

    # Base case: One element
    if low == high:
        return arr[low], arr[low]

    # Base case: Two elements
    if high == low + 1:

        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]

        return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)

    # Combine

    comparison_count += 1

    if lmin < rmin:
        overall_min = lmin
    else:
        overall_min = rmin

    comparison_count += 1

    if lmax > rmax:
        overall_max = lmax
    else:
        overall_max = rmax

    return overall_min, overall_max


# ---------- Naive Method ----------

def min_max_naive(arr):

    mn = arr[0]
    mx = arr[0]

    comps = 0

    for x in arr[1:]:

        comps += 1
        if x < mn:
            mn = x

        comps += 1
        if x > mx:
            mx = x

    return mn, mx, comps


# ---------- Demonstration ----------

arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

comparison_count = 0

mn, mx = min_max_dc(arr, 0, len(arr) - 1)

dc_comps = comparison_count

_, _, naive_comps = min_max_naive(arr)

print("Array:", arr)
print("Minimum:", mn)
print("Maximum:", mx)
print("Divide & Conquer Comparisons:", dc_comps)
print("Naive Comparisons:", naive_comps)


# ---------- Performance Analysis ----------

print()

print(f'{"Size":>8} {"DC Comps":>12} {"Naive Comps":>14} {"Formula 3n/2-2":>18}')

print("-" * 60)

for size in [10, 100, 1000, 10000]:

    arr = [random.randint(1, 10000) for _ in range(size)]

    comparison_count = 0

    mn, mx = min_max_dc(arr, 0, len(arr) - 1)

    dc = comparison_count

    _, _, naive = min_max_naive(arr)

    formula = 3 * size // 2 - 2

    print(f"{size:>8} {dc:>12} {naive:>14} {formula:>18}")