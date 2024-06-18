import unittest
from pathfinder import *
from mazeGenerator import generate_maze


class TestAStarSearch(unittest.TestCase):
    def setUp(self):
        """Создаем матрицы для тестов"""
        self.matrix1 = [[0 for _ in range(10)] for _ in range(10)]
        self.matrix1[0][0] = 1
        self.matrix1[9][9] = 2

        self.matrix2 = [[0 for _ in range(10)] for _ in range(10)]
        self.matrix2[0][0] = 1
        self.matrix2[9][9] = 2
        for x, y in [(3, 4), (3, 5), (3, 6), (2, 6)]:
            self.matrix2[x][y] = 3

        self.matrix3 = [[0 for _ in range(10)] for _ in range(10)]
        self.matrix3[0][0] = 1
        self.matrix3[9][9] = 2
        for x, y in [(2, 8), (2, 9), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (2, 2), (2, 3), (1, 3), (0, 3), (1, 0), (9, 6), (8, 6), (7, 6), (5, 7), (5, 6)]:
            self.matrix3[x][y] = 3

    def test_path_exists_simple(self):
        """Проверка, что путь существует в простой матрице без препятствий"""
        start = (0, 0)
        goal = (9, 9)
        path = a_star_search(self.matrix1, start, goal)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], goal)

    def test_random_maze_path(self):
        matrix, goal = generate_maze(10, 10)
        start = (0, 0)
        path = a_star_search(matrix, start, goal)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], goal)

    def test_path_exists_with_obstacles(self):
        """Проверка, что путь существует в матрице с препятствиями"""
        start = (0, 0)
        goal = (9, 9)
        path = a_star_search(self.matrix2, start, goal)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], goal)

    def test_path_not_exists(self):
        """Проверка, что путь не существует, если старт или цель заблокированы"""
        start = (0, 0)
        goal = (9, 9)
        path = a_star_search(self.matrix3, start, goal)
        self.assertIsNone(path)

    def test_optimal_path(self):
        """Проверка, что найденный путь является оптимальным"""
        start = (0, 0)
        goal = (9, 9)
        print_matrix(self.matrix2)
        path = a_star_search(self.matrix2, start, goal)
        self.assertEqual(len(path), 19)  # Оптимальная длина пути с учетом препятствий


if __name__ == '__main__':
    unittest.main()
