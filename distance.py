# pip install osmnx
# pip install scikit-learn
# pip install Taxicab
import os
import time
import numpy as np
import pandas as pd
import osmnx as ox
import taxicab as tc
import multiprocessing as mp

# Global variables
data = pd.read_csv('./data/info.csv', index_col=0,
                   dtype={'latitude': float, 'longitude': float, 'address': str})
num_nodes = len(data)

coordinate_list = list(zip(data['latitude'], data['longitude']))

graph = ox.graph_from_place(['Taipei', 
                             'New Taipei', 
                             'Keelung', 
                             'Taoyuan', 
                             'Hsinchu', 
                             'Hsinchu County'], network_type='drive')

# Find the shortest distance from origin to destination
def FindShortestPath(origin_id):
    start_time = time.process_time() # record the processing time for the node
    distance = np.zeros(shape=(1, num_nodes))
    
    for destination_id in range(num_nodes):
        if origin_id >= destination_id:
            distance[0][destination_id] = 0
        else:
            try:
                route = tc.distance.shortest_path(graph, coordinate_list[origin_id], coordinate_list[destination_id])
                distance[0][destination_id] = route[0]
            except:
                distance[0][destination_id] = -1
                print(f"ERROR: can't find path from {origin_id} to {destination_id}")

    finish_time = time.process_time()
    print(f"finish node {origin_id} with {finish_time-start_time} s")

    file_name = "./result/result"+str(origin_id)+".csv"
    output = pd.DataFrame(distance)
    output.to_csv(file_name, index=False)

# Make the list of nodes that already done
def DoneList():
    file_list = os.listdir("./result")

    todo_list = []
    for file_name in file_list:
        node_id = ""
        for char in file_name:
            if char.isdigit():
                node_id += char
        todo_list.append(int(node_id))

    return todo_list

if __name__ == '__main__':
    done_list = DoneList()
    id_list = [i for i in range(num_nodes) if not(i in done_list)]

    num_cores = mp.cpu_count()
    pool = mp.Pool(num_cores)
    pool.map(FindShortestPath, id_list)
    
    pool.close()
    pool.join()