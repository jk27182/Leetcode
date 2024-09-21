


visited_nodes = set()
isConnected = [
    [1,1,0],
    [1,1,0],
    [0,0,1],
]

def count_connections(city: int, connections: int):
    print('current city is ', city)
    print('visited_nodes is', visited_nodes)
    if city in visited_nodes:
        return connections

    visited_nodes.add(city)
    conn_next_city = count_connections(city+1, connections+1) 

    return conn_next_city



count_connections(0, 0)







