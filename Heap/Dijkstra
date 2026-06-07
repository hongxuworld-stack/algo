from collections import defaultdict
import heapq


# Method 1: finalize a node the first time it is popped.
def dijkstra_finalize_on_pop(edges, start):
    graph = defaultdict(list)

    for u, v, weight in edges:
        graph[u].append((weight, v))

    # (distance_from_start, node)
    heap = [(0, start)]
    distances = {}

    while heap:
        current_distance, node = heapq.heappop(heap)

        # The first pop gives this node's shortest distance.
        if node in distances:
            continue

        distances[node] = current_distance

        for weight, neighbor in graph[node]:
            if neighbor not in distances:
                new_distance = current_distance + weight
                heapq.heappush(heap, (new_distance, neighbor))

    return distances


# Method 2: update distances whenever a shorter path is found.
def dijkstra_relaxation(edges, start):
    graph = defaultdict(list)
    nodes = {start}

    for u, v, weight in edges:
        graph[u].append((weight, v))
        nodes.add(u)
        nodes.add(v)

    distances = {node: float("inf") for node in nodes}
    distances[start] = 0

    # (distance_from_start, node)
    heap = [(0, start)]

    while heap:
        current_distance, node = heapq.heappop(heap)

        # Ignore an outdated path left in the heap.
        if current_distance > distances[node]:
            continue

        for weight, neighbor in graph[node]:
            new_distance = current_distance + weight

            # Relaxation: update only when this path is shorter.
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return distances


# Both methods require non-negative edge weights.
# Time complexity: O((V + E) log V)
# Space complexity: O(V + E)
