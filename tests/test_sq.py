# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


class Num2WordsSQTest(TestCase):
    """Test cases for Albanian language (sq) num2words implementation"""
    
    def test_basic_numbers_0_to_10(self):
        """Test basic numbers 0-10 in Albanian"""
        self.assertEqual(num2words(0, lang='sq'), 'zero')
        self.assertEqual(num2words(1, lang='sq'), 'një')
        self.assertEqual(num2words(2, lang='sq'), 'dy')
        self.assertEqual(num2words(3, lang='sq'), 'tre')
        self.assertEqual(num2words(4, lang='sq'), 'katër')
        self.assertEqual(num2words(5, lang='sq'), 'pesë')
        self.assertEqual(num2words(6, lang='sq'), 'gjashtë')
        self.assertEqual(num2words(7, lang='sq'), 'shtatë')
        self.assertEqual(num2words(8, lang='sq'), 'tetë')
        self.assertEqual(num2words(9, lang='sq'), 'nëntë')
        self.assertEqual(num2words(10, lang='sq'), 'dhjetë')

    def test_teens_11_to_19(self):
        """Test teen numbers 11-19 in Albanian"""
        self.assertEqual(num2words(11, lang='sq'), 'njëmbëdhjetë')
        self.assertEqual(num2words(12, lang='sq'), 'dymbëdhjetë')
        self.assertEqual(num2words(13, lang='sq'), 'trembëdhjetë')
        self.assertEqual(num2words(14, lang='sq'), 'katërmbëdhjetë')
        self.assertEqual(num2words(15, lang='sq'), 'pesëmbëdhjetë')
        self.assertEqual(num2words(16, lang='sq'), 'gjashtëmbëdhjetë')
        self.assertEqual(num2words(17, lang='sq'), 'shtatëmbëdhjetë')
        self.assertEqual(num2words(18, lang='sq'), 'tetëmbëdhjetë')
        self.assertEqual(num2words(19, lang='sq'), 'nëntëmbëdhjetë')

    def test_tens_20_to_90(self):
        """Test tens (20, 30, 40, etc.) in Albanian"""
        self.assertEqual(num2words(20, lang='sq'), 'njëzet')
        self.assertEqual(num2words(30, lang='sq'), 'tridhjetë')
        self.assertEqual(num2words(40, lang='sq'), 'dyzet')
        self.assertEqual(num2words(50, lang='sq'), 'pesëdhjetë')
        self.assertEqual(num2words(60, lang='sq'), 'gjashtëdhjetë')
        self.assertEqual(num2words(70, lang='sq'), 'shtatëdhjetë')
        self.assertEqual(num2words(80, lang='sq'), 'tetëdhjetë')
        self.assertEqual(num2words(90, lang='sq'), 'nëntëdhjetë')

    def test_complex_tens(self):
        """Test complex tens with units in Albanian"""
        self.assertEqual(num2words(21, lang='sq'), 'njëzet e një')
        self.assertEqual(num2words(22, lang='sq'), 'njëzet e dy')
        self.assertEqual(num2words(23, lang='sq'), 'njëzet e tre')
        self.assertEqual(num2words(35, lang='sq'), 'tridhjetë e pesë')
        self.assertEqual(num2words(47, lang='sq'), 'dyzet e shtatë')
        self.assertEqual(num2words(56, lang='sq'), 'pesëdhjetë e gjashtë')
        self.assertEqual(num2words(68, lang='sq'), 'gjashtëdhjetë e tetë')
        self.assertEqual(num2words(79, lang='sq'), 'shtatëdhjetë e nëntë')
        self.assertEqual(num2words(84, lang='sq'), 'tetëdhjetë e katër')
        self.assertEqual(num2words(99, lang='sq'), 'nëntëdhjetë e nëntë')

    def test_hundreds(self):
        """Test hundreds in Albanian"""
        self.assertEqual(num2words(100, lang='sq'), 'njëqind')
        self.assertEqual(num2words(200, lang='sq'), 'dyqind')
        self.assertEqual(num2words(300, lang='sq'), 'treqind')
        self.assertEqual(num2words(400, lang='sq'), 'katërqind')
        self.assertEqual(num2words(500, lang='sq'), 'pesëqind')
        self.assertEqual(num2words(600, lang='sq'), 'gjashtëqind')
        self.assertEqual(num2words(700, lang='sq'), 'shtatëqind')
        self.assertEqual(num2words(800, lang='sq'), 'tetëqind')
        self.assertEqual(num2words(900, lang='sq'), 'nëntëqind')

    def test_complex_hundreds(self):
        """Test hundreds with tens and units in Albanian"""
        self.assertEqual(num2words(101, lang='sq'), 'njëqind e një')
        self.assertEqual(num2words(125, lang='sq'), 'njëqind njëzet e pesë')
        self.assertEqual(num2words(234, lang='sq'), 'dyqind tridhjetë e katër')
        self.assertEqual(num2words(345, lang='sq'), 'treqind dyzet e pesë')
        self.assertEqual(num2words(456, lang='sq'), 'katërqind pesëdhjetë e gjashtë')
        self.assertEqual(num2words(567, lang='sq'), 'pesëqind gjashtëdhjetë e shtatë')
        self.assertEqual(num2words(678, lang='sq'), 'gjashtëqind shtatëdhjetë e tetë')
        self.assertEqual(num2words(789, lang='sq'), 'shtatëqind tetëdhjetë e nëntë')
        self.assertEqual(num2words(890, lang='sq'), 'tetëqind nëntëdhjetë')
        self.assertEqual(num2words(999, lang='sq'), 'nëntëqind nëntëdhjetë e nëntë')

    def test_thousands(self):
        """Test thousands in Albanian"""
        self.assertEqual(num2words(1000, lang='sq'), 'një mijë')
        self.assertEqual(num2words(2000, lang='sq'), 'dy mijë')
        self.assertEqual(num2words(3000, lang='sq'), 'tre mijë')
        self.assertEqual(num2words(4000, lang='sq'), 'katër mijë')
        self.assertEqual(num2words(5000, lang='sq'), 'pesë mijë')
        self.assertEqual(num2words(10000, lang='sq'), 'dhjetë mijë')
        self.assertEqual(num2words(11000, lang='sq'), 'njëmbëdhjetë mijë')
        self.assertEqual(num2words(21000, lang='sq'), 'njëzet e një mijë')
        self.assertEqual(num2words(100000, lang='sq'), 'njëqind mijë')

    def test_complex_thousands(self):
        """Test complex thousands in Albanian"""
        self.assertEqual(num2words(1001, lang='sq'), 'një mijë e një')
        self.assertEqual(num2words(1234, lang='sq'), 'një mijë dyqind tridhjetë e katër')
        self.assertEqual(num2words(2345, lang='sq'), 'dy mijë treqind dyzet e pesë')
        self.assertEqual(num2words(12345, lang='sq'), 'dymbëdhjetë mijë treqind dyzet e pesë')
        self.assertEqual(num2words(23456, lang='sq'), 'njëzet e tre mijë katërqind pesëdhjetë e gjashtë')
        self.assertEqual(num2words(123456, lang='sq'), 'njëqind njëzet e tre mijë katërqind pesëdhjetë e gjashtë')

    def test_millions(self):
        """Test millions in Albanian"""
        self.assertEqual(num2words(1000000, lang='sq'), 'një milion')
        self.assertEqual(num2words(2000000, lang='sq'), 'dy milion')
        self.assertEqual(num2words(3000000, lang='sq'), 'tre milion')
        self.assertEqual(num2words(10000000, lang='sq'), 'dhjetë milion')
        self.assertEqual(num2words(100000000, lang='sq'), 'njëqind milion')

    def test_complex_millions(self):
        """Test complex millions in Albanian"""
        self.assertEqual(num2words(1000001, lang='sq'), 'një milion e një')
        self.assertEqual(num2words(1001000, lang='sq'), 'një milion e një mijë')
        self.assertEqual(num2words(1001001, lang='sq'), 'një milion e një mijë e një')
        self.assertEqual(num2words(1234567, lang='sq'), 'një milion e dyqind tridhjetë e katër mijë pesëqind gjashtëdhjetë e shtatë')
        self.assertEqual(num2words(12345678, lang='sq'), 'dymbëdhjetë milion e treqind dyzet e pesë mijë gjashtëqind shtatëdhjetë e tetë')

    def test_billions(self):
        """Test billions in Albanian"""
        self.assertEqual(num2words(1000000000, lang='sq'), 'një miliard')
        self.assertEqual(num2words(2000000000, lang='sq'), 'dy miliard')
        self.assertEqual(num2words(3000000000, lang='sq'), 'tre miliard')

    def test_negative_numbers(self):
        """Test negative numbers in Albanian"""
        self.assertEqual(num2words(-1, lang='sq'), 'minus një')
        self.assertEqual(num2words(-10, lang='sq'), 'minus dhjetë')
        self.assertEqual(num2words(-100, lang='sq'), 'minus njëqind')
        self.assertEqual(num2words(-1000, lang='sq'), 'minus një mijë')
        self.assertEqual(num2words(-1234, lang='sq'), 'minus një mijë dyqind tridhjetë e katër')

    def test_edge_cases(self):
        """Test edge cases and boundary values"""
        self.assertEqual(num2words(0, lang='sq'), 'zero')
        self.assertEqual(num2words(1, lang='sq'), 'një')
        self.assertEqual(num2words(999, lang='sq'), 'nëntëqind nëntëdhjetë e nëntë')
        self.assertEqual(num2words(1000, lang='sq'), 'një mijë')
        self.assertEqual(num2words(999999, lang='sq'), 'nëntëqind nëntëdhjetë e nëntë mijë nëntëqind nëntëdhjetë e nëntë')
        self.assertEqual(num2words(1000000, lang='sq'), 'një milion')

    def test_float_numbers(self):
        """Test float numbers in Albanian"""
        self.assertEqual(num2words(1.5, lang='sq'), 'një presje pesë')
        self.assertEqual(num2words(2.25, lang='sq'), 'dy presje dy pesë')
        self.assertEqual(num2words(10.75, lang='sq'), 'dhjetë presje shtatë pesë')
        self.assertEqual(num2words(100.01, lang='sq'), 'njëqind presje zero një')

    def test_currency_eur(self):
        """Test EUR currency formatting in Albanian"""
        self.assertEqual(num2words(1.00, lang='sq', to='currency', currency='EUR'), 'një euro, zero cent')
        self.assertEqual(num2words(2.00, lang='sq', to='currency', currency='EUR'), 'dy euro, zero cent')
        self.assertEqual(num2words(1.50, lang='sq', to='currency', currency='EUR'), 'një euro, pesëdhjetë cent')
        self.assertEqual(num2words(2.25, lang='sq', to='currency', currency='EUR'), 'dy euro, njëzet e pesë cent')

    def test_currency_usd(self):
        """Test USD currency formatting in Albanian"""
        self.assertEqual(num2words(1.00, lang='sq', to='currency', currency='USD'), 'një dollar, zero cent')
        self.assertEqual(num2words(2.00, lang='sq', to='currency', currency='USD'), 'dy dollar, zero cent')
        self.assertEqual(num2words(1.50, lang='sq', to='currency', currency='USD'), 'një dollar, pesëdhjetë cent')
        self.assertEqual(num2words(2.25, lang='sq', to='currency', currency='USD'), 'dy dollar, njëzet e pesë cent')

    def test_ordinal_numbers(self):
        """Test ordinal numbers in Albanian"""
        self.assertEqual(num2words(1, lang='sq', ordinal=True), 'i parë')
        self.assertEqual(num2words(2, lang='sq', ordinal=True), 'i dytë')
        self.assertEqual(num2words(3, lang='sq', ordinal=True), 'i tretë')
        self.assertEqual(num2words(4, lang='sq', ordinal=True), 'i katërt')
        self.assertEqual(num2words(5, lang='sq', ordinal=True), 'i pestë')
        self.assertEqual(num2words(10, lang='sq', ordinal=True), 'i dhjetë')
        self.assertEqual(num2words(21, lang='sq', ordinal=True), 'i njëzet e një')
        self.assertEqual(num2words(100, lang='sq', ordinal=True), 'i njëqind')

    def test_very_large_numbers(self):
        """Test very large numbers in Albanian"""
        self.assertEqual(num2words(1000000000000, lang='sq'), 'një trilion')
        self.assertEqual(num2words(1000000000000000, lang='sq'), 'një katrilion')