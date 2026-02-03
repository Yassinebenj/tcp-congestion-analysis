import csv
import matplotlib.pyplot as plt
import os

# Get directory of this Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build paths to CSV files
h1_path = os.path.join(BASE_DIR, "data", "h1.csv")
h3_path = os.path.join(BASE_DIR, "data", "h3.csv")


# -------- Read H1 data --------
times_h1 = []
values_h1 = []

with open(h1_path, "r", newline="") as f:
    reader = csv.reader(f)
    next(reader)  # skip header if needed

    for row in reader:
        times_h1.append(float(row[0]))
        values_h1.append(float(row[1]))


# -------- Read H3 data --------
times_h3 = []
values_h3 = []

with open(h3_path, "r", newline="") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        times_h3.append(float(row[0]))
        values_h3.append(float(row[1]))


# -------- Plot both --------
plt.plot(times_h1, values_h1, label="H1")
plt.plot(times_h3, values_h3, label="H3")

plt.xlabel("Time (s)")
plt.ylabel("Congestion Window")
plt.title("TCP Congestion Window: H1 vs H3")
plt.legend()
plt.grid(True)

plt.show()
