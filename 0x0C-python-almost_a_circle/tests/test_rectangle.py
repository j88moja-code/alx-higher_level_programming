#!/usr/bin/python3
"""Rectangle Test Module"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle Test Class"""
    def test_main_2(self):
        """test_main_2 method"""
        with self.assertRaises(TypeError):
            r0_m = Rectangle()
        with self.assertRaises(TypeError):
            r0_m = Rectangle(1)
        self.assertTrue(issubclass(Rectangle, Base))
        r1_m = Rectangle(10, 2)
        self.assertEqual(r1_m.width, 10)
        self.assertEqual(r1_m.height, 2)
        self.assertEqual(r1_m.x, 0)
        self.assertEqual(r1_m.y, 0)
        r2_m = Rectangle(2, 10)
        self.assertEqual(r2_m.width, 2)
        self.assertEqual(r2_m.height, 10)
        r3_m = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3_m.width, 10)
        self.assertEqual(r3_m.height, 2)
        with self.assertRaises(TypeError):
            r4_m = Rectangle(6, 6, 6, 6, 6, 6)

    def test_exceptions(self):
        """test_exceptions method"""
        r1 = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r4 = Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r4 = Rectangle(10, [2])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r4 = Rectangle(10, (2,))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r4 = Rectangle(10, 2.0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle([10], 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle((10,), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle(10.0, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r4 = Rectangle(10, 2, "3")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r4 = Rectangle(10, 2, [3])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r4 = Rectangle(10, 2, (3,))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r4 = Rectangle(10, 2, 3.0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r4 = Rectangle(10, 2, 3, "4")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r4 = Rectangle(10, 2, 3, [4])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r4 = Rectangle(10, 2, 3, (4,))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r4 = Rectangle(10, 2, 3, 4.0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.width = -10
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.height = -10
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.x = -10
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.y = -10
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = {}
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = []
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = ()
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = "x"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = {}
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = []
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = ()
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = "y"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = {}
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = []
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = ()
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = "width"
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.height = {}
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.height = []
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.height = ()
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.height = "height"
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r4 = Rectangle(10, 2, 3, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r4 = Rectangle(10, 2, -3, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r4 = Rectangle(10, -2, 3, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r4 = Rectangle(-10, 2, 3, 1)

    def test_area(self):
        """test_area method"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """test_display method"""
        r1 = Rectangle(4, 6)
        CO = io.StringIO()
        sys.stdout = CO
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(CO.getvalue(), "####\n####\n####\n####\n####\n####\n")
        r1 = Rectangle(2, 2)
        CO = io.StringIO()
        sys.stdout = CO
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(CO.getvalue(), "##\n##\n")

    def test_dunder_str(self):
        """test_dunder_str"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        CO = io.StringIO()
        sys.stdout = CO
        print(r1)
        self.assertEqual(CO.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")
        sys.stdout = sys.__stdout__
        r2 = Rectangle(5, 5, 1, id=1)
        CO = io.StringIO()
        sys.stdout = CO
        print(r2)
        self.assertEqual(CO.getvalue(), "[Rectangle] (1) 1/0 - 5/5\n")
        sys.stdout = sys.__stdout__

    def test_display_1(self):
        """test_display_1 method"""
        r1 = Rectangle(2, 3, 2, 2)
        CO = io.StringIO()
        sys.stdout = CO
        r1.display()
        self.assertEqual(CO.getvalue(), "\n\n  ##\n  ##\n  ##\n")
        CO = io.StringIO()
        sys.stdout = CO
        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        self.assertEqual(CO.getvalue(), " ###\n ###\n")
        sys.stdout = sys.__stdout__

    def test_update(self, *args):
        """test_update test method"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        CO = io.StringIO()
        sys.stdout = CO
        print(r1)
        self.assertEqual(CO.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")
        r1.update(89)
        CO = io.StringIO()
        sys.stdout = CO
        print(r1)
        self.assertEqual(CO.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")
        r1.update(89, 2)
        CO = io.StringIO()
        sys.stdout = CO
        print(r1)
        self.assertEqual(CO.getvalue(), "[Rectangle] (89) 10/10 - 2/10\n")
        r1.update(89, 2, 3)
        CO = io.StringIO()
        sys.stdout = CO
        print(r1)
        self.assertEqual(CO.getvalue(), "[Rectangle] (89) 10/10 - 2/3\n")
        r1.update(89, 2, 3, 4)
        CO = io.StringIO()
        sys.stdout = CO
        print(r1)
        self.assertEqual(CO.getvalue(), "[Rectangle] (89) 4/10 - 2/3\n")
        r1.update(89, 2, 3, 4, 5)
        CO = io.StringIO()
        sys.stdout = CO
        print(r1)
        self.assertEqual(CO.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(1, "with")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(1, 2, "with")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(1, 2, 3, "with")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(1, 2, 3, 4, "with")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(1, ["with"])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(1, 2, ["with"])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(1, 2, 3, [])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(1, 2, 3, 4, [])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(1, ("with",))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(1, 2, ("with",))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(1, 2, 3, ("with",))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(1, 2, 3, 4, ("with",))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(1, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(1, 2, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(1, 2, 3, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(1, 2, 3, 4, True)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(1, 2.0)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(1, 2, 3.0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(1, 2, 3, 4.0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(1, 2, 3, 4, 5.0)

    def test_update_1(self):
        """test_update_1 method"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        CO = io.StringIO()
        sys.stdout = CO
        print(r1)
        self.assertEqual(CO.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")
        r1.update(height=1)
        CO = io.StringIO()
        sys.stdout = CO
        print(r1)
        self.assertEqual(CO.getvalue(), "[Rectangle] (1) 10/10 - 10/1\n")
        r1.update(width=1, x=2)
        CO = io.StringIO()
        sys.stdout = CO
        print(r1)
        self.assertEqual(CO.getvalue(), "[Rectangle] (1) 2/10 - 1/1\n")
        r1.update(y=1, width=2, x=3, id=89)
        CO = io.StringIO()
        sys.stdout = CO
        print(r1)
        self.assertEqual(CO.getvalue(), "[Rectangle] (89) 3/1 - 2/1\n")
        r1.update(x=1, height=2, y=3, width=4)
        CO = io.StringIO()
        sys.stdout = CO
        print(r1)
        self.assertEqual(CO.getvalue(), "[Rectangle] (89) 1/3 - 4/2\n")
        sys.stdout = sys.__stdout__
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(width=True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(height=True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=True)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(width=[])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(height=[])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=[])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=[])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(width=(True,))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(height=(True,))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=(True,))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=(True,))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(width={})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(height={})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x={})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y={})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(width=3.0)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(height=5.0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=10.0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=11.0)

    def test_rectangle_to_dict(self):
        """test_rectangle_to_dict"""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertTrue(type(r1_dictionary) == dict)
        r2.update(**r1_dictionary)
        self.assertTrue(r2.__str__() == r1.__str__())
