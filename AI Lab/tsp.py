import sys

def nearest_neighbor(graph):
    num_cities = len(graph)
    visited = [False] * num_cities
    tour = []
    
    # Start from a random city
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True
    
    for _ in range(num_cities - 1):
        nearest_city = None
        min_distance = sys.maxsize
        
        # Find the nearest unvisited city
        for city in range(num_cities):
            if not visited[city] and graph[current_city][city] < min_distance:
                nearest_city = city
                min_distance = graph[current_city][city]
        
        # Move to the nearest city
        tour.append(nearest_city)
        visited[nearest_city] = True
        current_city = nearest_city
    
    # Return to the starting city to complete the tour
    tour.append(tour[0])
    
    return tour

if __name__ == "__main__":
    print("Enter number of vertices:")
    n = int(input())
    graph = []
    
    for i in range(n):
        row = []
        for j in range(n):
            if i != j:
                print("Enter cost of", i, "to", j)
                e = int(input())
                row.append(e)
            else:
                row.append(0)
        graph.append(row)
    
    tour = nearest_neighbor(graph)
    min_cost = sum(graph[tour[i]][tour[i + 1]] for i in range(n))

    print("Shortest path:", tour)
    print("Min Cost:", min_cost)
