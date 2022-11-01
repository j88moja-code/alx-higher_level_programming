#!/usr/bin/python3
"""Base Class Test Module"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_a_noinput(self):
        """test_noinput"""
        b0 = Base(1)
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_b_wronginput(self):
        """test_wronginput"""
        b1 = Base()
        self.assertEqual(b1.id, 4)
        b2 = Base("wrong")
        self.assertEqual(b2.id, "wrong")
        with self.assertRaises(TypeError):
            b3 = Base(1, 2)

    def test_c_to_json_string(self):
        """test_to_json_string"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([r1_dictionary])
        self.assertTrue(type(r1_dictionary) == dict)
        self.assertTrue(type(json_dictionary) == str)
        json_dictionary = Base.to_json_string([])
        self.assertTrue(json_dictionary == "[]")
        json_dictionary = Base.to_json_string(None)
        self.assertTrue(json_dictionary == "[]")
        s1 = Square(10, 2, 8, 1)
        s1_dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([s1_dictionary])
        self.assertTrue(type(s1_dictionary) == dict)
        self.assertTrue(type(json_dictionary) == str)

    def test_d_string_to_file(self):
        """test_string_to_file method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, id=1)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "w+") as f:
            self.assertTrue(type(f.read()) == str)
            f.seek(0)
        s1 = Square(10, 2, 8, 1)
        s2 = Square(2, id=1)
        Square.save_to_file([s1, s2])
        with open("Square.json", "w+") as f:
            self.assertTrue(type(f.read()) == str)
            f.seek(0)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "w+") as f:
            strrd = f.read()
            self.assertTrue(type(strrd) == str)
            CO = io.StringIO()
            sys.stdout = CO
            print(strrd)
            self.assertEqual(CO.getvalue(), "\n")
            sys.stdout = sys.__stdout__
        Square.save_to_file(None)
        with open("Square.json", "w+") as f:
            strrd = f.read()
            self.assertTrue(type(strrd) == str)
            CO = io.StringIO()
            sys.stdout = CO
            print(strrd)
            self.assertEqual(CO.getvalue(), "\n")
            sys.stdout = sys.__stdout__

    def test_e_from_json_string(self):
        """test_from_json_string method test"""
        self.assertTrue(Base.from_json_string(None) == [])
        self.assertTrue(Base.from_json_string("") == [])
        json_list_input = Rectangle.to_json_string([{"hi": 5, "hey": 6}])
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_output) == list)
        json_list_input = Square.to_json_string([{"hi": 5, "hey": 6}])
        list_output = Square.from_json_string(json_list_input)
        self.assertTrue(type(list_output) == list)

    def test_f_create(self):
        """test_create test method"""
        self.assertTrue(type(Rectangle.create()) == Rectangle)
        r1 = Rectangle(3, 5, 1, id=1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
        s1 = Square(3, 5, 1, id=1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)
        r3 = Rectangle.create(**{})
        self.assertTrue(r3.width == 1)
        self.assertTrue(r3.height == 1)
        self.assertTrue(r3.x == 0)
        self.assertTrue(r3.y == 0)
        s3 = Square.create(**{})
        self.assertTrue(s3.size == 1)
        self.assertTrue(s3.x == 0)
        self.assertTrue(s3.y == 0)

    def test_g_load_from_file(self):
        """test_load_from_file test method"""
        self.assertTrue(Base.load_from_file() == [])
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue(type(list_rectangles_output) == list)

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()
        self.assertTrue(type(list_squares_output) == list)

    def test_h_save_to_load_from_file_csv(self):
        """test_save_to_file_csv"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)
        with open("Rectangle.json", "r") as f:
            self.assertTrue(type(f.read()) == str)

        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertTrue(type(list_rectangles_output) == list)
