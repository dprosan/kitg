from collections import deque

class Dinic:
    def __init__(self, n):
        self.n = n  # Количество вершин
        self.graph = [[] for _ in range(n)]  # Список смежности для графа
        self.level = [-1] * n  # Уровни вершин для поиска в ширину
        self.ptr = [0] * n  # Указатели на рёбра для поиска в глубину

    def add_edge(self, u, v, capacity):
        """Добавление ребра в граф с пропускной способностью"""
        self.graph[u].append([v, capacity, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def bfs(self, source, sink):
        """Поиск увеличивающих путей с помощью поиска в ширину"""
        self.level = [-1] * self.n
        queue = deque([source])
        self.level[source] = 0
        while queue:
            u = queue.popleft()
            for v, cap, rev in self.graph[u]:
                if self.level[v] == -1 and cap > 0:  # Если вершина не посещена и ребро имеет пропускную способность
                    self.level[v] = self.level[u] + 1
                    if v == sink:
                        return True
                    queue.append(v)
        return False

    def dfs(self, u, sink, flow):
        """Поиск увеличивающего пути с помощью поиска в глубину"""
        if u == sink:
            return flow
        while self.ptr[u] < len(self.graph[u]):
            v, cap, rev = self.graph[u][self.ptr[u]]
            if self.level[v] == self.level[u] + 1 and cap > 0:  # Если вершина на следующем уровне и есть пропускная способность
                curr_flow = min(flow, cap)
                pushed_flow = self.dfs(v, sink, curr_flow)
                if pushed_flow > 0:
                    # Обновляем остаточную сеть
                    self.graph[u][self.ptr[u]][1] -= pushed_flow
                    self.graph[v][rev][1] += pushed_flow
                    return pushed_flow
            self.ptr[u] += 1
        return 0

    def max_flow(self, source, sink):
        """Вычисление максимального потока"""
        total_flow = 0
        while self.bfs(source, sink):
            self.ptr = [0] * self.n
            while True:
                flow = self.dfs(source, sink, float('Inf'))
                if flow == 0:
                    break
                total_flow += flow
        return total_flow


# Пример использования
if __name__ == "__main__":
    # Количество вершин в графе
    n = 6  
    dinic = Dinic(n)

    # Добавление рёбер с пропускными способностями
    dinic.add_edge(0, 1, 16)
    dinic.add_edge(0, 2, 13)
    dinic.add_edge(1, 2, 10)
    dinic.add_edge(1, 3, 12)
    dinic.add_edge(2, 1, 4)
    dinic.add_edge(2, 4, 14)
    dinic.add_edge(3, 2, 9)
    dinic.add_edge(3, 5, 20)
    dinic.add_edge(4, 3, 7)
    dinic.add_edge(4, 5, 4)

    # Поиск максимального потока от источника 0 до стока 5
    source = 0
    sink = 5
    max_flow = dinic.max_flow(source, sink)
    print(f"Максимальный поток: {max_flow}")
