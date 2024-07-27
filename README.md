# Food Company Customer Distance Matrix
 
## Introduction
Generate a distance matrix between all customers based on the locations provided by the order

## Features
- Find the coordinates based on the location provided by excel
- Load real-world road information and find the shortest distance between customer nodes

## Requirements
- Python
    - Numpy
    - Pandas
    - OpenPyXL
    - Google Maps API
    - OSMnx
    - Scikit-learn
    - TaxiCab

## Usage

1. **Install Dependencies**
    - Install basic dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. **Find map coordinates using Google Map API**
    - Modify data reading and text processing code based on the data characteristics:
    ```python
    # Data Processing
    import pandas as pd

    DATA_PATH = './data/2月9日(上午)送貨單.xlsx'
    df = pd.read_excel(DATA_PATH, usecols=['市', '區', '地址'], dtype=str)
    df['address'] = df['市'] + df['區'] + df['地址']
    small_df = df['address']

    # String Manipulation
    for i in range(len(small_df)):
        # Remove the contents after the left parenthesis
        index = small_df.iloc[i].find('(')
        if index != -1:
            small_df.iloc[i] = small_df.iloc[i][:index]
    ```

    - Run the following command:
    ```bash
    python coordinate.py
    ```
    - **Note**: You need to register for a Google Maps API account to obtain an API key. For more information, please refer to: [Google Maps API](https://developers.google.com/maps).

3. **Generate Distance Matrix**
    - Run the following command to find the shortest distance from one node to each node:
    ```bash
    python distance.py
    ```

    - Run the following command to combine the results:
    ```bash
    python combine_result.py
    ```
