import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)

    mean_matrix = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), float(np.mean(matrix))]
    variance_matrix = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), float(np.var(matrix))]
    std_matrix = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), float(np.std(matrix))]
    max_matrix = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), float(np.max(matrix))]
    min_matrix = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), float(np.min(matrix))]
    sum_matrix = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), float(np.sum(matrix))]

    calculations = {
        'mean' : mean_matrix,
        'variance' : variance_matrix,
        'standard deviation': std_matrix,
        'max': max_matrix,
        'min': min_matrix,
        'sum': sum_matrix 
    }

    return calculations