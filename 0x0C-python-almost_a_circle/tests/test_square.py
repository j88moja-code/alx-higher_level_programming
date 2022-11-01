#!/usr/bin/python3
"""Square Test Module"""
import sys
import io
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """TestSquare Class"""
    def test_square(self):
        """test_square method"""
        s1 = Square(5, id=1)
        CO = io.StringIO()
        sys.stdout = CO
        print(s1)
        self.assertEqual(CO.getvalue(), "[Square] (1) 0/0 - 5\n")
        self.assertEqual(s1.area(), 25)
        CO = io.StringIO()
        sys.stdout = CO
        s1.display()
        self.assertEqual(CO.getvalue(), "#####\n#####\n#####\n#####\n#####\n")
        s2 = Square(2, 2, id=2)
        CO = io.StringIO()
        sys.stdout = CO
        print(s2)
        self.assertEqual(CO.getvalue(), "[Square] (2) 2/0 - 2\n")
        self.assertEqual(s2.area(), 4)
        CO = io.StringIO()
        sys.stdout = CO
        s2.display()
        self.assertEqual(CO.getvalue(), "  ##\n  ##\n")
        s3 = Square(3, 1, 3, id=3)
        CO = io.StringIO()
        sys.stdout = CO
        print(s3)
        self.assertEqual(CO.getvalue(), "[Square] (3) 1/3 - 3\n")
        self.assertEqual(s3.area(), 9)
        CO = io.StringIO()
        sys.stdout = CO
        s3.display()
        self.assertEqual(CO.getvalue(), "\n\n\n ###\n ###\n ###\n")

    def test_square_size(self):
        """test_square_size method"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = "g"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = []
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = {}
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = 4.0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = True
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.x = "g"
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.x = []
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.x = {}
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.x = 4.0
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.x = True
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.y = "g"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.y = []
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.y = {}
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.y = 4.0
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.y = True

    def test_square_update(self):
        """test_square_update method"""
        s1 = Square(5, id=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(size="hi")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(x="hi")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(y="hi")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(size=[])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(x=[])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(y=[])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(size=())
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(x=())
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(y=())
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(size=1.0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(x=2.0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(y=3.0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(size=True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(x=False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(y=True)

    def test_square_to_dictionary(self):
        """test_square_to_dictionary"""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertTrue(type(s1_dictionary) == dict)
        s2.update(**s1_dictionary)
        self.assertTrue(s1.__str__() == s2.__str__())
