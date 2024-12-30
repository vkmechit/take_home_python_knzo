# Take Home Test Kenzo Security

This repository contains a Python script for processing security alerts and calculating risk scores.

## Prerequisites

- Python 3.7+
- pandas

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
git clone https://github.com/vkmechit/take_home_python_knzo.git


2. Navigate to the project directory:
cd take-home-test-kenzo-security


## Usage

To run the script, follow these steps:

1. Create a virtual environment:
```
python -m venv venv
```


3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```


4. Install dependencies:
```
pip install pandas
```


6. Run the main Python script:
```
python main.py
```


## Sample Input and Output Files

The script uses two sample files:
- `sample_input.csv`: This file contains the input data for processing security alerts. Users can modify the contents of this file, but should not change the headers.
- `sample_output.csv`: This file stores the processed results after running the script.

## Config File

The script uses a configuration file named `config.json`. Users can update this file according to their specific requirements. The default configuration is set up to handle various scenarios, but it can be modified to suit different needs.

## Supported Python Version

This project supports Python 3.7 and above. We recommend using Python 3.8 or 3.9 for optimal performance.

