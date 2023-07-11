# Crop Allocation Backtracking Approach

This project implements a backtracking search algorithm to solve the crop allocation problem in Belagavi district, Karnataka, under the One-Taluk One-Crop Scheme. The goal is to assign four crop seeds (Jowar, Cotton, Maize, Paddy) to each Taluk in a way that ensures neighboring Taluks do not have the same crops to grow. This scheme is similar to the One District One Crop scheme of the state government of Karnataka.

## Problem Statement

The problem is to find an appropriate solution by implementing a backtracking search to distribute crop seeds to each Taluk in Belagavi district. The objective is to assign crops to each Taluk while satisfying the following conditions:

- Each Taluk should be assigned one crop seed.
- No neighboring Taluks should have the same crop assigned.

## Getting Started

To get started with this project, follow the instructions below.

### Prerequisites

Make sure you have the following prerequisites installed:

- Python (version 3.7 or higher)
- pip (package installer for Python)

### Installation

1. Clone the repository using the following command:

   ```shell
   git clone https://github.com/MohammedZuhairAhmed/Crop-Allocation-Backtracking-approach.git
   ```

2. Navigate to the project directory:

   ```shell
   cd Crop-Allocation-Backtracking-approach
   ```

3. Install the required dependencies by running:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

To use the backtracking approach for crop allocation, follow these steps:

1. Make sure you have the necessary input files for the farm and crop data. These files should be in a specific format (see `data/farm_data.csv` and `data/crop_data.csv` for examples).

2. Adjust the parameters in the `backtracking_search.py` file according to your requirements.

3. Run the `backtracking_search.py` script using the following command:

   ```shell
   python backtracking_search.py
   ```

4. The script will output the optimized crop allocation for the given Taluks in Belagavi district, considering the constraints of no neighboring Taluks having the same crop assigned.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

The backtracking algorithm implemented in this project was inspired by various resources and prior work in the field. We acknowledge the contributions of the open-source community and researchers in developing this approach.
