class Arc:
    """
    Класс для представления дуги.
    """
    def __init__(self, start, end, weight=None):
        self.start = start  # Начальная вершина
        self.end = end      # Конечная вершина
        self.weight = weight  # Вес дуги (необязательно)

    def __repr__(self):
        return f"Arc({self.start} -> {self.end}, weight={self.weight})"

class Network:
    """
    Класс для представления сети, содержащей дуги.
    """
    def __init__(self):
        self.arcs = []

    def add_arc(self, start, end, weight=None):
        """Добавляет дугу в сеть."""
        self.arcs.append(Arc(start, end, weight))

    def sort_arcs_by_start(self):
        """Упорядочивает дуги по начальной вершине."""
        self.arcs.sort(key=lambda arc: arc.start)

    def __repr__(self):
        return "\n".join(map(str, self.arcs))

# Пример использования
if __name__ == "__main__":
    network = Network()

    # Добавляем дуги
    network.add_arc(3, 4, 5)
    network.add_arc(1, 2, 2)
    network.add_arc(2, 3, 4)
    network.add_arc(1, 3, 3)

    print("До сортировки:")
    print(network)

    # Упорядочиваем дуги по начальной вершине
    network.sort_arcs_by_start()

    print("\nПосле сортировки:")
    print(network)