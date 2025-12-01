import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("C:/Users/BizovaV/ci2/A06/graph.csv")

# Extract columns
x = df["x"]
y = df["y"]

# Plot
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x^2")
plt.grid(True)

# Save figure
plt.savefig("C:/Users/BizovaV/ci2/A06/graph.png", dpi=300)
plt.show()
