from time import perf_counter

import numpy as np
from numpy.typing import NDArray

from src.plotting import plot_points


def invalid_orientation(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> bool:
    val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    if val >= 0:
        return True
    return False

def convex_bucket(points: NDArray) -> NDArray:
    """Complexity: O(n log n)"""
    clockwise_sorted_ch = []

    sorted_points = sorted(points, key=lambda p: (p[0], p[1]))  # Sort all points by X, then by Y if x1 = x2

    clockwise_sorted_ch.append(sorted_points[0])
    clockwise_sorted_ch.append(sorted_points[1])

    for point in sorted_points[2:]:
        # Checking if orientation is incorrect:
        while len(clockwise_sorted_ch) > 1 and invalid_orientation(clockwise_sorted_ch[-2], clockwise_sorted_ch[-1], point):
            clockwise_sorted_ch.pop()

        clockwise_sorted_ch.append(point)

    clockwise_sorted_ch += clockwise_sorted_ch[-2::-1]  # To avoid connecting first and last point

    return np.array(clockwise_sorted_ch)


if __name__ == "__main__":
    for i in range(1, 11):
        txtpath = f"../points_{i}.txt"
        curr_points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(curr_points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec")
        plot_points(curr_points, convex_hull=ch, markersize=20)
        print()
