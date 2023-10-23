import json
from scipy.io import loadmat
import numpy as np

# Load the .mat file
mat_file_path = 'test.mat'
mat_data = loadmat(mat_file_path)
mat_data = {key: mat_data[key] for key in mat_data if not key.startswith('__') and not isinstance(mat_data[key], type)}

# Convert to JSON
json_data = json.dumps(mat_data, default=lambda x: x.tolist() if isinstance(x, np.ndarray) else x)

# Save to a .json file
json_file_path = 'test.json'
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)
