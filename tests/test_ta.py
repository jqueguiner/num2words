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


class Num2WordsTATest(TestCase):
    def test_basic_numbers(self):
        """Test basic numbers 0-19"""
        self.assertEqual(num2words(0, lang="ta"), "பூஜ்ஜியம்")
        self.assertEqual(num2words(1, lang="ta"), "ஒன்று")
        self.assertEqual(num2words(2, lang="ta"), "இரண்டு")
        self.assertEqual(num2words(3, lang="ta"), "மூன்று")
        self.assertEqual(num2words(4, lang="ta"), "நான்கு")
        self.assertEqual(num2words(5, lang="ta"), "ஐந்து")
        self.assertEqual(num2words(6, lang="ta"), "ஆறு")
        self.assertEqual(num2words(7, lang="ta"), "ஏழு")
        self.assertEqual(num2words(8, lang="ta"), "எட்டு")
        self.assertEqual(num2words(9, lang="ta"), "ஒன்பது")
        self.assertEqual(num2words(10, lang="ta"), "பத்து")
        
        # Test teens (11-19)
        self.assertEqual(num2words(11, lang="ta"), "பதினொன்று")
        self.assertEqual(num2words(12, lang="ta"), "பன்னிரண்டு")
        self.assertEqual(num2words(13, lang="ta"), "பதின்மூன்று")
        self.assertEqual(num2words(14, lang="ta"), "பதினான்கு")
        self.assertEqual(num2words(15, lang="ta"), "பதினைந்து")
        self.assertEqual(num2words(16, lang="ta"), "பதினாறு")
        self.assertEqual(num2words(17, lang="ta"), "பதினேழு")
        self.assertEqual(num2words(18, lang="ta"), "பதினெட்டு")
        self.assertEqual(num2words(19, lang="ta"), "பத்தொன்பது")

    def test_tens(self):
        """Test tens (20, 30, 40, etc.)"""
        self.assertEqual(num2words(20, lang="ta"), "இருபது")
        self.assertEqual(num2words(30, lang="ta"), "முப்பது")
        self.assertEqual(num2words(40, lang="ta"), "நாற்பது")
        self.assertEqual(num2words(50, lang="ta"), "ஐம்பது")
        self.assertEqual(num2words(60, lang="ta"), "அறுபது")
        self.assertEqual(num2words(70, lang="ta"), "எழுபது")
        self.assertEqual(num2words(80, lang="ta"), "எண்பது")
        self.assertEqual(num2words(90, lang="ta"), "தொண்ணூறு")

    def test_compound_numbers(self):
        """Test compound numbers (21, 22, etc.)"""
        self.assertEqual(num2words(21, lang="ta"), "இருபத்தி ஒன்று")
        self.assertEqual(num2words(22, lang="ta"), "இருபத்தி இரண்டு")
        self.assertEqual(num2words(35, lang="ta"), "முப்பத்தி ஐந்து")
        self.assertEqual(num2words(42, lang="ta"), "நாற்பத்தி இரண்டு")
        self.assertEqual(num2words(56, lang="ta"), "ஐம்பத்தி ஆறு")
        self.assertEqual(num2words(67, lang="ta"), "அறுபத்தி ஏழு")
        self.assertEqual(num2words(78, lang="ta"), "எழுபத்தி எட்டு")
        self.assertEqual(num2words(89, lang="ta"), "எண்பத்தி ஒன்பது")
        self.assertEqual(num2words(99, lang="ta"), "தொண்ணூற்றி ஒன்பது")

    def test_hundreds(self):
        """Test hundreds (100, 200, etc.)"""
        self.assertEqual(num2words(100, lang="ta"), "நூறு")
        self.assertEqual(num2words(200, lang="ta"), "இருநூறு")
        self.assertEqual(num2words(300, lang="ta"), "முன்னூறு")
        self.assertEqual(num2words(400, lang="ta"), "நானூறு")
        self.assertEqual(num2words(500, lang="ta"), "ஐநூறு")
        self.assertEqual(num2words(600, lang="ta"), "அறுநூறு")
        self.assertEqual(num2words(700, lang="ta"), "எழுநூறு")
        self.assertEqual(num2words(800, lang="ta"), "எண்ணூறு")
        self.assertEqual(num2words(900, lang="ta"), "தொள்ளாயிரம்")

    def test_compound_hundreds(self):
        """Test compound hundreds (101, 234, etc.)"""
        self.assertEqual(num2words(101, lang="ta"), "நூற்றி ஒன்று")
        self.assertEqual(num2words(111, lang="ta"), "நூற்றி பதினொன்று")
        self.assertEqual(num2words(123, lang="ta"), "நூற்றி இருபத்தி மூன்று")
        self.assertEqual(num2words(234, lang="ta"), "இருநூற்றி முப்பத்தி நான்கு")
        self.assertEqual(num2words(345, lang="ta"), "முன்னூற்றி நாற்பத்தி ஐந்து")
        self.assertEqual(num2words(456, lang="ta"), "நானூற்றி ஐம்பத்தி ஆறு")
        self.assertEqual(num2words(567, lang="ta"), "ஐநூற்றி அறுபத்தி ஏழு")
        self.assertEqual(num2words(678, lang="ta"), "அறுநூற்றி எழுபத்தி எட்டு")
        self.assertEqual(num2words(789, lang="ta"), "எழுநூற்றி எண்பத்தி ஒன்பது")
        self.assertEqual(num2words(891, lang="ta"), "எண்ணூற்றி தொண்ணூற்றி ஒன்று")
        self.assertEqual(num2words(912, lang="ta"), "தொள்ளாயிரத்தி பன்னிரண்டு")

    def test_thousands(self):
        """Test thousands"""
        self.assertEqual(num2words(1000, lang="ta"), "ஆயிரம்")
        self.assertEqual(num2words(2000, lang="ta"), "இரண்டு ஆயிரம்")
        self.assertEqual(num2words(3000, lang="ta"), "மூன்று ஆயிரம்")
        self.assertEqual(num2words(10000, lang="ta"), "பத்து ஆயிரம்")
        self.assertEqual(num2words(25000, lang="ta"), "இருபத்தி ஐந்து ஆயிரம்")
        self.assertEqual(num2words(99000, lang="ta"), "தொண்ணூற்றி ஒன்பது ஆயிரம்")

    def test_compound_thousands(self):
        """Test compound thousands"""
        self.assertEqual(num2words(1001, lang="ta"), "ஆயிரத்தி ஒன்று")
        self.assertEqual(num2words(1234, lang="ta"), "ஆயிரத்தி இருநூற்றி முப்பத்தி நான்கு")
        self.assertEqual(num2words(2345, lang="ta"), "இரண்டு ஆயிரத்தி முன்னூற்றி நாற்பத்தி ஐந்து")
        self.assertEqual(num2words(12345, lang="ta"), "பன்னிரண்டு ஆயிரத்தி முன்னூற்றி நாற்பத்தி ஐந்து")
        self.assertEqual(num2words(54321, lang="ta"), "ஐம்பத்தி நான்கு ஆயிரத்தி முன்னூற்றி இருபத்தி ஒன்று")

    def test_lakhs(self):
        """Test lakhs (100,000s)"""
        self.assertEqual(num2words(100000, lang="ta"), "லட்சம்")
        self.assertEqual(num2words(200000, lang="ta"), "இரண்டு லட்சம்")
        self.assertEqual(num2words(500000, lang="ta"), "ஐந்து லட்சம்")
        self.assertEqual(num2words(1000000, lang="ta"), "பத்து லட்சம்")
        self.assertEqual(num2words(2500000, lang="ta"), "இருபத்தி ஐந்து லட்சம்")

    def test_compound_lakhs(self):
        """Test compound lakhs"""
        self.assertEqual(num2words(100001, lang="ta"), "லட்சத்தி ஒன்று")
        self.assertEqual(num2words(123456, lang="ta"), "லட்சத்தி இருபத்தி மூன்று ஆயிரத்தி நானூற்றி ஐம்பத்தி ஆறு")
        self.assertEqual(num2words(654321, lang="ta"), "ஆறு லட்சத்தி ஐம்பத்தி நான்கு ஆயிரத்தி முன்னூற்றி இருபத்தி ஒன்று")

    def test_crores(self):
        """Test crores (10,000,000s)"""
        self.assertEqual(num2words(10000000, lang="ta"), "கோடி")
        self.assertEqual(num2words(20000000, lang="ta"), "இரண்டு கோடி")
        self.assertEqual(num2words(50000000, lang="ta"), "ஐந்து கோடி")
        self.assertEqual(num2words(100000000, lang="ta"), "பத்து கோடி")

    def test_compound_crores(self):
        """Test compound crores"""
        self.assertEqual(num2words(10000001, lang="ta"), "கோடியே ஒன்று")
        self.assertEqual(num2words(12345678, lang="ta"), "கோடியே இருபத்தி மூன்று லட்சத்தி நாற்பத்தி ஐந்து ஆயிரத்தி அறுநூற்றி எழுபத்தி எட்டு")

    def test_large_numbers(self):
        """Test large numbers for comprehensive coverage"""
        self.assertEqual(num2words(1729, lang="ta"), "ஆயிரத்தி எழுநூற்றி இருபத்தி ஒன்பது")
        self.assertEqual(num2words(9999, lang="ta"), "ஒன்பது ஆயிரத்தி தொள்ளாயிரத்தி தொண்ணூற்றி ஒன்பது")
        self.assertEqual(num2words(999999, lang="ta"), "ஒன்பது லட்சத்தி தொண்ணூற்றி ஒன்பது ஆயிரத்தி தொள்ளாயிரத்தி தொண்ணூற்றி ஒன்பது")

    def test_cardinal_for_float_number(self):
        """Test floating point numbers"""
        self.assertEqual(num2words(1.61803, lang="ta"), "ஒன்று தசமம் ஆறு ஒன்று எட்டு பூஜ்ஜியம் மூன்று")
        self.assertEqual(num2words(34.876, lang="ta"), "முப்பத்தி நான்கு தசமம் எட்டு ஏழு ஆறு")
        self.assertEqual(num2words(3.14, lang="ta"), "மூன்று தசமம் ஒன்று நான்கு")
        self.assertEqual(num2words(0.5, lang="ta"), "பூஜ்ஜியம் தசமம் ஐந்து")
        self.assertEqual(num2words(0.01, lang="ta"), "பூஜ்ஜியம் தசமம் பூஜ்ஜியம் ஒன்று")

    def test_negative_numbers(self):
        """Test negative numbers"""
        self.assertEqual(num2words(-1, lang="ta"), "(-) ஒன்று")
        self.assertEqual(num2words(-42, lang="ta"), "(-) நாற்பத்தி இரண்டு")
        self.assertEqual(num2words(-100, lang="ta"), "(-) நூறு")
        self.assertEqual(num2words(-1234, lang="ta"), "(-) ஆயிரத்தி இருநூற்றி முப்பத்தி நான்கு")

    def test_negative_decimals(self):
        """Test negative decimal numbers"""
        self.assertEqual(num2words(-0.4, lang="ta"), "(-) பூஜ்ஜியம் தசமம் நான்கு")
        self.assertEqual(num2words(-0.5, lang="ta"), "(-) பூஜ்ஜியம் தசமம் ஐந்து")
        self.assertEqual(num2words(-1.4, lang="ta"), "(-) ஒன்று தசமம் நான்கு")
        self.assertEqual(num2words(-3.14, lang="ta"), "(-) மூன்று தசமம் ஒன்று நான்கு")

    def test_ordinal_numbers(self):
        """Test ordinal numbers"""
        self.assertEqual(num2words(1, lang='ta', to='ordinal'), "முதல்")
        self.assertEqual(num2words(2, lang='ta', to='ordinal'), "இரண்டாம்")
        self.assertEqual(num2words(3, lang='ta', to='ordinal'), "மூன்றாம்")
        self.assertEqual(num2words(4, lang='ta', to='ordinal'), "நான்காம்")
        self.assertEqual(num2words(5, lang='ta', to='ordinal'), "ஐந்தாம்")
        self.assertEqual(num2words(10, lang='ta', to='ordinal'), "பத்தாம்")
        self.assertEqual(num2words(21, lang='ta', to='ordinal'), "இருபத்தி ஒன்றாம்")
        self.assertEqual(num2words(100, lang='ta', to='ordinal'), "நூறாம்")

    def test_ordinal_num(self):
        """Test ordinal numbers in numeric form"""
        self.assertEqual(num2words(1, lang="ta", to='ordinal_num'), "1ம்")
        self.assertEqual(num2words(2, lang="ta", to='ordinal_num'), "2ம்")
        self.assertEqual(num2words(3, lang="ta", to='ordinal_num'), "3ம்")
        self.assertEqual(num2words(10, lang="ta", to='ordinal_num'), "10ம்")
        self.assertEqual(num2words(21, lang="ta", to='ordinal_num'), "21ம்")
        self.assertEqual(num2words(100, lang="ta", to='ordinal_num'), "100ம்")

    def test_edge_cases(self):
        """Test edge cases and boundary values"""
        self.assertEqual(num2words(0, lang="ta"), "பூஜ்ஜியம்")
        self.assertEqual(num2words(1, lang="ta"), "ஒன்று")
        self.assertEqual(num2words(999, lang="ta"), "தொள்ளாயிரத்தி தொண்ணூற்றி ஒன்பது")
        self.assertEqual(num2words(1000, lang="ta"), "ஆயிரம்")
        self.assertEqual(num2words(99999, lang="ta"), "தொண்ணூற்றி ஒன்பது ஆயிரத்தி தொள்ளாயிரத்தி தொண்ணூற்றி ஒன்பது")
        self.assertEqual(num2words(100000, lang="ta"), "லட்சம்")
        self.assertEqual(num2words(9999999, lang="ta"), "தொண்ணூற்றி ஒன்பது லட்சத்தி தொண்ணூற்றி ஒன்பது ஆயிரத்தி தொள்ளாயிரத்தி தொண்ணூற்றி ஒன்பது")
        self.assertEqual(num2words(10000000, lang="ta"), "கோடி")