import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")


    matrix = np.array(input_list).reshape(3, 3)

 
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Axis 0 (Columns)
            matrix.mean(axis=1).tolist(),  # Axis 1 (Rows)
            matrix.mean().tolist()        # Flattened
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()
        ]
    }
    # FCC version (Rows first, then Columns)
    {
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}


    calculations_fcc = {
        'mean': [
            matrix.mean(axis=1).tolist(),  # Axis 1 (Rows)
            matrix.mean(axis=0).tolist(),  # Axis 0 (Columns)
            matrix.mean().tolist()         # Flattened
        ],
        'variance': [
            matrix.var(axis=1).tolist(),
            matrix.var(axis=0).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=1).tolist(),
            matrix.std(axis=0).tolist(),
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=1).tolist(),
            matrix.max(axis=0).tolist(),
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=1).tolist(),
            matrix.min(axis=0).tolist(),
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=1).tolist(),
            matrix.sum(axis=0).tolist(),
            matrix.sum().tolist()
        ]
    }

    return calculations_fcc

if __name__ == '__main__':
   
    test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    try:
        results = calculate(test_list)
        import pprint
        pprint.pprint(results)
    except ValueError as e:
        print(f"Error: {e}")