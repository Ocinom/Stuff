import unittest

class Employee():

    def __init__(self, f, l, s):
        self.f = f
        self.l = l
        self.s = s

    def gr(self, r=5000):
        self.s += r

class te(unittest.TestCase):

    def setUp(self):
        self.em = Employee('j', 'd', 0)

    def test_gdr(self):
        self.em.gr()
        self.assertEqual(5000, self.em.s)

    def test_gcr(self):
        self.em.gr(10)
        self.assertEqual(10, self.em.s)


unittest.main()