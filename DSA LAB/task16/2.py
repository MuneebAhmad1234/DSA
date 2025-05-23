import heapq

def dijkstra(graph, start):
    priority_queue = []
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0

    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > shortest_distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))
