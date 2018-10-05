import unittest

from ..route_between_nodes import Node, Graph, find_route


class Test(unittest.TestCase):
    def test_basic(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')

        a.add_neighbor(b)
        b.add_neighbor(c)
        c.add_neighbor(b)

        graph = Graph([a, b, c, d])

        self.assertTrue(find_route(graph, a, b))
        self.assertTrue(find_route(graph, a, c))
        self.assertFalse(find_route(graph, a, d))
        self.assertFalse(find_route(graph, b, a))
        self.assertTrue(find_route(graph, b, c))
        self.assertFalse(find_route(graph, b, d))
        self.assertFalse(find_route(graph, c, a))
        self.assertTrue(find_route(graph, c, b))
        self.assertFalse(find_route(graph, c, d))
        self.assertFalse(find_route(graph, d, a))
        self.assertFalse(find_route(graph, d, b))
        self.assertFalse(find_route(graph, d, c))
