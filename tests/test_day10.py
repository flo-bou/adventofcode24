import unittest
from day10.utils import *


class TestDay10(unittest.TestCase):

    def test_get_position_value(self):
        topo_map = [["2", "4", "6", "2"], ["3", "3", "1", "2"]]
        self.assertEqual(get_position_value((0,3), topo_map), 2)
        with self.assertRaises(IndexError):
            get_position_value((2,3), topo_map)
        with self.assertRaises(IndexError):
            get_position_value((), topo_map)
            
    def test_get_incremental_paths(self):
        topo_map = [["0", "1", "4", "5"], ["1", "2", "3", "4"]]
        self.assertEqual(get_incremental_paths([(0,0)], topo_map), [[(0,0), (0,1)], [(0,0), (1,0)]])

