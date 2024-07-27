import numpy as np
import pandas as pd

data = pd.read_csv('./data/info.csv', index_col=0,
                   dtype={'latitude': float, 'longitude': float, 'address': str})
num_nodes = len(data)

result = np.zeros((num_nodes, num_nodes))
for i in range(num_nodes):
    file_name = "./result/result"+str(i)+".csv"
    df = pd.read_csv(file_name).to_numpy()
    result[i] = df

for i in range(num_nodes):
    for j in range(num_nodes):
        if result[i][j] == 0:
            result[i][j] = result[j][i]

output = pd.DataFrame(result)
output.to_csv("./result/distance_matrix.csv")