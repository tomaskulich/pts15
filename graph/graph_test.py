
import unittest
from graph import prob_grid, get_path, bfs, dfs

class TestGrid(unittest.TestCase):
                
    def setUp(self):
        self.full_graph = prob_grid(1)
        self.empty_graph = prob_grid(0)

    def test_full_straight(self):
        path = get_path(*bfs(self.full_graph, (0,0), lambda x: x==(10,10)))
        self.assertEqual(len(path) - 1, 20)

    def test_empty(self):
        visited, end = bfs(self.empty_graph, (0,0), lambda x: x==(10,10))
        self.assertEqual(len(visited), 1)
        self.assertEqual(end, None)


if __name__ == '__main__':
    unittest.main()
