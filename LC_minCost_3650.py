import heapq
def minCost(n, edges):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))       
        adj[v].append((u, 2 * w))  
    pq = [(0, 0)]
    dist = [float('inf')] * n
    dist[0] = 0

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return int(dist[n - 1]) if dist[n - 1] != float('inf') else -1

#main
n = 4
edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
print(minCost(n, edges))