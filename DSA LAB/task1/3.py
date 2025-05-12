import numpy as np
import matplotlib.pyplot as plt


complexities = {
    "O(1)": lambda n: np.ones_like(n),
    "O(log n)": lambda n: np.log2(n),
    "O(n)": lambda n: n,
    "O(n²)": lambda n: n**2
}

n_values = np.arange(1, 101)


plt.figure(figsize=(8, 6))
for label, func in complexities.items():
    plt.plot(n_values, func(n_values), label=label)

plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time')
plt.title('Comparison of Big-O Complexities')
plt.legend()
plt.grid(True)
plt.show()
