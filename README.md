# Read Me

## Overview:
This Python script processes atom data from a given configuration file (`config.custom`) and calculates various properties such as center of mass (COM) and tangents for atom clusters. The script uses vector mathematics to compute unit vectors and dot products, and it visualizes the results using a logarithmic plot.

## Dependencies:
- **Python 3.x**
- **Libraries:**
  - `sys`: Standard library used for system-specific parameters and functions.
  - `operator`: Provides efficient functions corresponding to basic operations.
  - `pdb`: Python debugger (not currently used in the script).
  - `numpy`: For numerical operations and logarithmic calculations.
  - `math`: For mathematical operations like square root.
  - `matplotlib.pyplot`: For plotting graphs.

## Data Structure:
- **`atom` dictionary**: A template for storing individual atom properties (e.g., `id`, `type`, `mol`, coordinates `x`, `y`, `z`, and periodic image flags `ix`, `iy`, `iz`).
  
## Functions:

### 1. `unit_vector(vector)`
- **Purpose**: Converts a 3D vector into a unit vector by normalizing it.
- **Input**: A vector in 3D space.
- **Output**: The normalized vector.

### 2. `dot_product(vector1, vector2)`
- **Purpose**: Calculates the dot product of two 3D vectors.
- **Input**: Two vectors (must both be of length 3).
- **Output**: The scalar result of the dot product.

### 3. `get_sorted_batch(file_name)`
- **Purpose**: Reads the atom data from the configuration file and returns a sorted list of atoms by their `id`.
- **Input**: The name of the file containing atom information.
- **Output**: A sorted list of atom dictionaries.

### 4. `com_56(batch)`
- **Purpose**: Calculates the center of mass for a batch of 56 atoms.
- **Input**: A list of 56 atoms.
- **Output**: A list of coordinates representing the center of mass.

### 5. `populate_coms(whole_batch)`
- **Purpose**: Placeholder function (currently incomplete) intended to populate a list of center of mass data for the entire batch of atoms.

### 6. `com_trimer(whole_batch, start)`
- **Purpose**: Calculates the center of mass for a cluster of three consecutive batches of 56 atoms.
- **Input**: A list of atoms and the starting index for the first batch.
- **Output**: The equivalent center of mass for the three batches.

### 7. `populate_tangents(whole_batch)`
- **Purpose**: Populates a global list of tangent vectors calculated between clusters of atoms. Uses the COM of three batches at a time and calculates a unit tangent vector.
- **Input**: The entire batch of atoms.
- **Output**: Populates the `tangents` global list.

## Main Flow:
- **File Input**: Reads and sorts atom data from `config.custom`.
- **COM Calculation**: Calculates the center of mass for the clusters.
- **Tangent Calculation**: Calculates and stores the tangents between consecutive atom clusters.
- **Logarithmic Plot**: Calculates the logarithm of the dot product between the tangent vectors and generates a plot showing this relationship.

## How to Run:
1. Ensure all dependencies are installed (e.g., `numpy`, `matplotlib`).
2. Place the atom configuration file (`config.custom`) in the same directory as the script.
3. Run the script:
   ```bash
   python script_name.py
   ```
4. The script will output the length of the tangent vectors list and display a plot of the log-scaled dot products between vectors.

