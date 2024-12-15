from collections import deque

def bfs_shortest_path(graph, source):
    """
    Алгоритм построения кратчайших путей на сети с единичными длинами.

    :param graph: Словарь, представляющий граф в виде списка смежности.
                  Ключи - вершины, значения - списки соседних вершин.
    :param source: Вершина-источник, от которой ищутся кратчайшие пути.
    :return: Словарь расстояний от источника до каждой достижимой вершины.
    """
    # Инициализация
    distance = {v: -1 for v in graph}  # -1 означает, что вершина не посещена
    distance[source] = 0
    queue = deque([source])

    # Поиск в ширину
    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if distance[neighbor] == -1:  # Если сосед ещё не посещён
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    return distance

# Пример использования
if __name__ == "__main__":
    # Задаём граф в виде списка смежности
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4],
        4: [3]
    }

    # Вершина-источник
    source = 0

    # Поиск кратчайших путей
    distances = bfs_shortest_path(graph, source)

    # Вывод результатов
    print("Расстояния от вершины", source, ":")
    for vertex, dist in distances.items():
        print(f"Вершина {vertex}: {dist}")