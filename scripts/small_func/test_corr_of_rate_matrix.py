import numpy as np
from scipy.stats import pearsonr
from numpy.linalg import norm

# 1. Construct a substitution model
def construct_substitution_model(a):
    matrix = np.full((4, 4), a)
    np.fill_diagonal(matrix, -3*a)
    return matrix

# 2. Add noise to a substitution model
def add_noise(old_matrix, std_dev):
    noise = np.random.normal(0, std_dev, old_matrix.shape)
    new_matrix = old_matrix + noise
    # Ensure non-diagonal elements are not less than 0
    for i in range(new_matrix.shape[0]):
        for j in range(new_matrix.shape[1]):
            if i != j:
                new_matrix[i, j] = np.maximum(0, new_matrix[i, j])
    # Recalculate the diagonal elements
    for i in range(new_matrix.shape[0]):
        new_matrix[i, i] = -np.sum(new_matrix[i, [j for j in range(new_matrix.shape[1]) if j != i]])
    return new_matrix

def calculate_correlation(matrix1, matrix2):
    r, _ = pearsonr(matrix1.flatten(), matrix2.flatten())
    return r

# 4. Compare the correlation with two substitution matrices
def compare_correlation(a1, a2, std_dev):
    matrix1 = construct_substitution_model(a1)
    matrix2 = construct_substitution_model(a2)
    matrix1_noisy = add_noise(matrix1, std_dev)
    matrix2_noisy = add_noise(matrix2, std_dev)
    return calculate_correlation(matrix1_noisy, matrix2_noisy)

# calculate the norm of the difference between two matrices
def calculate_norm(matrix1, matrix2, ord=None):
    if ord == 0:
        # L0 norm for a matrix is not supported by numpy, calculate manually
        return np.count_nonzero(matrix1 - matrix2)
    else:
        return norm(matrix1 - matrix2, ord=ord)

# 5. Compare the norm of the difference between two substitution matrices
def compare_norm(a1, a2, std_dev, ord=None):
    matrix1 = construct_substitution_model(a1)
    matrix2 = construct_substitution_model(a2)
    matrix1_noisy = add_noise(matrix1, std_dev)
    matrix2_noisy = add_noise(matrix2, std_dev)
    return calculate_norm(matrix1_noisy, matrix2_noisy, ord)

# Test the functions
a1 = 4
a2 = 8

print("Tese perason correlation")
# coef with noise
print(compare_correlation(a1, a2, 1))
print(compare_correlation(a1, 2*a2, 2))
print(compare_correlation(2*a1, 4*a2, 2))
# coef without noise
print(compare_correlation(a1, a2, 0))

print("Test norm in same rate with noise")
# norm with noise
print(compare_norm(a1, a1, 1, ord=None))  # Frobenius norm
print(compare_norm(a1, a1, 1, ord=2))  # L2 norm
print(compare_norm(a1, a1, 1, ord=0))  # L0 norm

print("Test norm in different rate without noise")
# norm without noise
print(compare_norm(a1, a2, 0, ord=None))  # Frobenius norm
print(compare_norm(a1, a2, 0, ord=2))  # L2 norm
print(compare_norm(a1, a2, 0, ord=0))  # L0 norm

print("Other test")
print(compare_correlation(3, 3, 0.5))
print(compare_correlation(3, 3.2, 0.5))
print(compare_correlation(3, 3.4, 0.5))

print(compare_norm(3, 3, 0.2, ord = 2))