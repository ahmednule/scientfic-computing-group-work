import numpy as np


adjacency = np.array([
    [0.0, 1.0, 1.0, 0.0],
    [1.0, 0.0, 1.0, 1.0],
    [1.0, 1.0, 0.0, 1.0],
    [0.0, 1.0, 1.0, 0.0],
])
eigenvalues, eigenvectors = np.linalg.eig(adjacency)
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
centrality = dominant_vector / dominant_vector.sum()

print("Dominant eigenvalue:", dominant_value)
print("Eigenvector-based importance:")
for node, score in zip(["A", "B", "C", "D"], centrality):
    print(f"{node}: {score:.4f}")

vector = np.real(eigenvectors[:, index])
print(
    "Verification error:",
    np.linalg.norm(adjacency @ vector - dominant_value * vector),
)
