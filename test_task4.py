#!/usr/bin/env python

import unittest
import task4


class Test4(unittest.TestCase):
    def test4(self):
        self.assertEqual(task4.task4(100), '455')
        self.assertEqual(task4.task4(13), '-1')
        self.assertRaises(ValueError, task4.task4, -1)


if __name__ == '__main__':
    unittest.main()
