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

from unittest import TestCase

from num2words import num2words


class Num2WordsMSTest(TestCase):
    def test_cardinal_basic_numbers(self):
        """Test basic numbers 0-9"""
        self.assertEqual(num2words(0, lang='ms'), "kosong")
        self.assertEqual(num2words(1, lang='ms'), "satu")
        self.assertEqual(num2words(2, lang='ms'), "dua")
        self.assertEqual(num2words(3, lang='ms'), "tiga")
        self.assertEqual(num2words(4, lang='ms'), "empat")
        self.assertEqual(num2words(5, lang='ms'), "lima")
        self.assertEqual(num2words(6, lang='ms'), "enam")
        self.assertEqual(num2words(7, lang='ms'), "tujuh")
        self.assertEqual(num2words(8, lang='ms'), "lapan")
        self.assertEqual(num2words(9, lang='ms'), "sembilan")

    def test_cardinal_ten_to_nineteen(self):
        """Test numbers 10-19"""
        self.assertEqual(num2words(10, lang='ms'), "sepuluh")
        self.assertEqual(num2words(11, lang='ms'), "sebelas")
        self.assertEqual(num2words(12, lang='ms'), "dua belas")
        self.assertEqual(num2words(13, lang='ms'), "tiga belas")
        self.assertEqual(num2words(14, lang='ms'), "empat belas")
        self.assertEqual(num2words(15, lang='ms'), "lima belas")
        self.assertEqual(num2words(16, lang='ms'), "enam belas")
        self.assertEqual(num2words(17, lang='ms'), "tujuh belas")
        self.assertEqual(num2words(18, lang='ms'), "lapan belas")
        self.assertEqual(num2words(19, lang='ms'), "sembilan belas")

    def test_cardinal_tens(self):
        """Test tens 20, 30, 40, etc."""
        self.assertEqual(num2words(20, lang='ms'), "dua puluh")
        self.assertEqual(num2words(30, lang='ms'), "tiga puluh")
        self.assertEqual(num2words(40, lang='ms'), "empat puluh")
        self.assertEqual(num2words(50, lang='ms'), "lima puluh")
        self.assertEqual(num2words(60, lang='ms'), "enam puluh")
        self.assertEqual(num2words(70, lang='ms'), "tujuh puluh")
        self.assertEqual(num2words(80, lang='ms'), "lapan puluh")
        self.assertEqual(num2words(90, lang='ms'), "sembilan puluh")

    def test_cardinal_twenty_to_ninety_nine(self):
        """Test compound numbers 21-99"""
        self.assertEqual(num2words(21, lang='ms'), "dua puluh satu")
        self.assertEqual(num2words(25, lang='ms'), "dua puluh lima")
        self.assertEqual(num2words(34, lang='ms'), "tiga puluh empat")
        self.assertEqual(num2words(47, lang='ms'), "empat puluh tujuh")
        self.assertEqual(num2words(58, lang='ms'), "lima puluh lapan")
        self.assertEqual(num2words(69, lang='ms'), "enam puluh sembilan")
        self.assertEqual(num2words(76, lang='ms'), "tujuh puluh enam")
        self.assertEqual(num2words(83, lang='ms'), "lapan puluh tiga")
        self.assertEqual(num2words(99, lang='ms'), "sembilan puluh sembilan")

    def test_cardinal_hundreds(self):
        """Test hundreds"""
        self.assertEqual(num2words(100, lang='ms'), "seratus")
        self.assertEqual(num2words(200, lang='ms'), "dua ratus")
        self.assertEqual(num2words(300, lang='ms'), "tiga ratus")
        self.assertEqual(num2words(400, lang='ms'), "empat ratus")
        self.assertEqual(num2words(500, lang='ms'), "lima ratus")
        self.assertEqual(num2words(600, lang='ms'), "enam ratus")
        self.assertEqual(num2words(700, lang='ms'), "tujuh ratus")
        self.assertEqual(num2words(800, lang='ms'), "lapan ratus")
        self.assertEqual(num2words(900, lang='ms'), "sembilan ratus")

    def test_cardinal_compound_hundreds(self):
        """Test compound hundreds with tens and units"""
        self.assertEqual(num2words(101, lang='ms'), "seratus satu")
        self.assertEqual(num2words(108, lang='ms'), "seratus lapan")
        self.assertEqual(num2words(111, lang='ms'), "seratus sebelas")
        self.assertEqual(num2words(125, lang='ms'), "seratus dua puluh lima")
        self.assertEqual(num2words(234, lang='ms'), "dua ratus tiga puluh empat")
        self.assertEqual(num2words(345, lang='ms'), "tiga ratus empat puluh lima")
        self.assertEqual(num2words(456, lang='ms'), "empat ratus lima puluh enam")
        self.assertEqual(num2words(567, lang='ms'), "lima ratus enam puluh tujuh")
        self.assertEqual(num2words(678, lang='ms'), "enam ratus tujuh puluh lapan")
        self.assertEqual(num2words(789, lang='ms'), "tujuh ratus lapan puluh sembilan")
        self.assertEqual(num2words(999, lang='ms'), "sembilan ratus sembilan puluh sembilan")

    def test_cardinal_thousands(self):
        """Test thousands"""
        self.assertEqual(num2words(1000, lang='ms'), "seribu")
        self.assertEqual(num2words(2000, lang='ms'), "dua ribu")
        self.assertEqual(num2words(3000, lang='ms'), "tiga ribu")
        self.assertEqual(num2words(5000, lang='ms'), "lima ribu")
        self.assertEqual(num2words(10000, lang='ms'), "sepuluh ribu")

    def test_cardinal_compound_thousands(self):
        """Test compound thousands"""
        self.assertEqual(num2words(1001, lang='ms'), "seribu satu")
        self.assertEqual(num2words(1075, lang='ms'), "seribu tujuh puluh lima")
        self.assertEqual(num2words(1234, lang='ms'), "seribu dua ratus tiga puluh empat")
        self.assertEqual(num2words(2345, lang='ms'), "dua ribu tiga ratus empat puluh lima")
        self.assertEqual(num2words(12345, lang='ms'), "dua belas ribu tiga ratus empat puluh lima")
        self.assertEqual(num2words(23456, lang='ms'), "dua puluh tiga ribu empat ratus lima puluh enam")
        self.assertEqual(num2words(123456, lang='ms'), "seratus dua puluh tiga ribu empat ratus lima puluh enam")
        self.assertEqual(num2words(999999, lang='ms'), "sembilan ratus sembilan puluh sembilan ribu sembilan ratus sembilan puluh sembilan")

    def test_cardinal_millions(self):
        """Test millions"""
        self.assertEqual(num2words(1000000, lang='ms'), "satu juta")
        self.assertEqual(num2words(2000000, lang='ms'), "dua juta")
        self.assertEqual(num2words(5000000, lang='ms'), "lima juta")
        self.assertEqual(num2words(10000000, lang='ms'), "sepuluh juta")

    def test_cardinal_compound_millions(self):
        """Test compound millions"""
        self.assertEqual(num2words(1000001, lang='ms'), "satu juta satu")
        self.assertEqual(num2words(1087231, lang='ms'), "satu juta lapan puluh tujuh ribu dua ratus tiga puluh satu")
        self.assertEqual(num2words(2500000, lang='ms'), "dua juta lima ratus ribu")
        self.assertEqual(num2words(12345678, lang='ms'), "dua belas juta tiga ratus empat puluh lima ribu enam ratus tujuh puluh lapan")

    def test_cardinal_billions(self):
        """Test billions"""
        self.assertEqual(num2words(1000000000, lang='ms'), "satu bilion")
        self.assertEqual(num2words(2000000000, lang='ms'), "dua bilion")
        self.assertEqual(num2words(1000000408, lang='ms'), "satu bilion empat ratus lapan")

    def test_cardinal_decimal_numbers(self):
        """Test decimal numbers"""
        self.assertEqual(num2words(1.5, lang='ms'), "satu perpuluhan lima")
        self.assertEqual(num2words(12.34, lang='ms'), "dua belas perpuluhan tiga empat")
        self.assertEqual(num2words(9.076, lang='ms'), "sembilan perpuluhan kosong tujuh enam")
        self.assertEqual(num2words(0.5, lang='ms'), "kosong perpuluhan lima")
        self.assertEqual(num2words(0.25, lang='ms'), "kosong perpuluhan dua lima")

    def test_cardinal_negative_numbers(self):
        """Test negative numbers"""
        self.assertEqual(num2words(-1, lang='ms'), "negatif satu")
        self.assertEqual(num2words(-23, lang='ms'), "negatif dua puluh tiga")
        self.assertEqual(num2words(-123, lang='ms'), "negatif seratus dua puluh tiga")
        self.assertEqual(num2words(-1234, lang='ms'), "negatif seribu dua ratus tiga puluh empat")
        self.assertEqual(num2words(-923, lang='ms'), "negatif sembilan ratus dua puluh tiga")

    def test_cardinal_negative_decimal_numbers(self):
        """Test negative decimal numbers"""
        self.assertEqual(num2words(-0.4, lang='ms'), "negatif kosong perpuluhan empat")
        self.assertEqual(num2words(-0.5, lang='ms'), "negatif kosong perpuluhan lima")
        self.assertEqual(num2words(-1.4, lang='ms'), "negatif satu perpuluhan empat")
        self.assertEqual(num2words(-10.25, lang='ms'), "negatif sepuluh perpuluhan dua lima")
        self.assertEqual(num2words(-0.234, lang='ms'), "negatif kosong perpuluhan dua tiga empat")

    def test_ordinal_basic_numbers(self):
        """Test ordinal numbers"""
        self.assertEqual(num2words(1, ordinal=True, lang='ms'), "pertama")
        self.assertEqual(num2words(2, ordinal=True, lang='ms'), "kedua")
        self.assertEqual(num2words(3, ordinal=True, lang='ms'), "ketiga")
        self.assertEqual(num2words(4, ordinal=True, lang='ms'), "keempat")
        self.assertEqual(num2words(5, ordinal=True, lang='ms'), "kelima")
        self.assertEqual(num2words(10, ordinal=True, lang='ms'), "kesepuluh")
        self.assertEqual(num2words(11, ordinal=True, lang='ms'), "kesebelas")
        self.assertEqual(num2words(20, ordinal=True, lang='ms'), "kedua puluh")
        self.assertEqual(num2words(21, ordinal=True, lang='ms'), "kedua puluh satu")
        self.assertEqual(num2words(100, ordinal=True, lang='ms'), "keseratus")

    def test_ordinal_for_negative_number(self):
        """Test ordinal with negative numbers should raise error"""
        self.assertRaises(TypeError, num2words, -12, ordinal=True, lang='ms')

    def test_ordinal_for_floating_number(self):
        """Test ordinal with floating numbers should raise error"""
        self.assertRaises(TypeError, num2words, 3.243, ordinal=True, lang='ms')

    def test_currency(self):
        """Test currency conversion"""
        # Note: This will use default currency handling, but could be customized for Malaysian Ringgit
        self.assertEqual(num2words(1, lang='ms', to='currency'), "satu ringgit")
        self.assertEqual(num2words(50, lang='ms', to='currency'), "lima puluh ringgit")
        self.assertEqual(num2words(100, lang='ms', to='currency'), "seratus ringgit")

    def test_year(self):
        """Test year conversion"""
        self.assertEqual(num2words(2023, lang='ms', to='year'), "dua ribu dua puluh tiga")
        self.assertEqual(num2words(1990, lang='ms', to='year'), "seribu sembilan ratus sembilan puluh")
        self.assertEqual(num2words(2000, lang='ms', to='year'), "dua ribu")

    def test_edge_cases(self):
        """Test edge cases and special scenarios"""
        # Test large numbers
        self.assertEqual(num2words(1000000000000, lang='ms'), "satu trilion")
        
        # Test zero in different contexts
        self.assertEqual(num2words(1000, lang='ms'), "seribu")
        self.assertEqual(num2words(1001, lang='ms'), "seribu satu")
        self.assertEqual(num2words(1010, lang='ms'), "seribu sepuluh")
        self.assertEqual(num2words(1100, lang='ms'), "seribu seratus")