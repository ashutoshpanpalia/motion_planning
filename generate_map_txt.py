import numpy as np
import random

def generate_map(
    n=500,
    m=500,
    num_obstacles=20,
    max_obstacle_size=30,
    filename="map.txt"
):
    # Initialize empty map
    grid = np.zeros((n, m), dtype=int)

    for _ in range(num_obstacles):
        # Random rectangle size
        h = random.randint(1, max_obstacle_size)
        w = random.randint(1, max_obstacle_size)

        # Random top-left corner (ensure it fits)
        x = random.randint(0, n - h)
        y = random.randint(0, m - w)

        # Place obstacle
        grid[x:x+h, y:y+w] = 1

    # Save to txt file
    np.savetxt(filename, grid, fmt="%d")

    return grid


if __name__ == "__main__":
    generate_map(
        n=1000,
        m=800,
        num_obstacles=50,
        max_obstacle_size=50,
        filename="rrt_map2.txt"
    )
