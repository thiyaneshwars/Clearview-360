import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull

# Function to read LiDAR data from a file
def read_lidar_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

# Replace the sample data with a call to read_lidar_data
file_path = '/home/Thiyanesh/Desktop/live_op.txt' # Update this path to your actual file
data = read_lidar_data(file_path)

# Data Parsing (same as before)
theta = []
dist = []
for line in data.strip().split('\n'):
    parts = line.split()
    try:
        t = float(parts[1])
        d = float(parts[3])
        theta.append(t)
        dist.append(d)
    except (ValueError, IndexError) as e:
        print(f"Error parsing line: {line}")
        print(f"Error: {e}")

theta = np.array(theta)
dist = np.array(dist)

# Convert polar coordinates to Cartesian coordinates for top view
x = dist * np.cos(np.radians(theta))
y = dist * np.sin(np.radians(theta))

# Ensure there are points before creating the ConvexHull
if len(x) > 0 and len(y) > 0:
    points = np.vstack((x, y)).T
    hull = ConvexHull(points)
    x_hull = points[hull.vertices, 0]
    y_hull = points[hull.vertices, 1]

    # --- Outer Shell Representation ---
    plt.figure(figsize=(8, 8))
    plt.plot(x_hull, y_hull, marker='.', linestyle='-')
    plt.fill(x_hull, y_hull, 'b', alpha=0.3)  # Fill the outer shell with a light blue color
    plt.title("LiDAR Data (Outer Shell)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()
else:
    print("No points to plot.")