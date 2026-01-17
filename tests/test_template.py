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

"""
STANDARD TEST TEMPLATE FOR NUM2WORDS2 LANGUAGES

This template defines the minimum set of tests that every language 
implementation should have to ensure consistent quality and coverage.

To use this template for a new language:
1. Copy this file to test_XX.py (where XX is your language code)
2. Replace 'LANG_CODE' with your actual language code
3. Replace expected outputs with correct translations for your language
4. Add any language-specific tests at the end
"""

from unittest import TestCase
from num2words2 import num2words

# Replace with your language code
LANG_CODE = 'xx'


class Num2WordsXXTest(TestCase):
    """Standard test suite for language XX."""
    
    # ========================================================================
    # REQUIRED TEST CATEGORY 1: CARDINAL NUMBERS
    # ========================================================================
    
    def test_cardinal_basic(self):
        """Test basic cardinal numbers 0-20."""
        # Every language MUST handle 0-20
        test_cases = [
            (0, "zero"),
            (1, "one"),
            (2, "two"),
            (3, "three"),
            (4, "four"),
            (5, "five"),
            (6, "six"),
            (7, "seven"),
            (8, "eight"),
            (9, "nine"),
            (10, "ten"),
            (11, "eleven"),
            (12, "twelve"),
            (13, "thirteen"),
            (14, "fourteen"),
            (15, "fifteen"),
            (16, "sixteen"),
            (17, "seventeen"),
            (18, "eighteen"),
            (19, "nineteen"),
            (20, "twenty"),
        ]
        for num, expected in test_cases:
            self.assertEqual(num2words(num, lang=LANG_CODE), expected)
    
    def test_cardinal_tens(self):
        """Test multiples of ten."""
        test_cases = [
            (10, "ten"),
            (20, "twenty"),
            (30, "thirty"),
            (40, "forty"),
            (50, "fifty"),
            (60, "sixty"),
            (70, "seventy"),
            (80, "eighty"),
            (90, "ninety"),
        ]
        for num, expected in test_cases:
            self.assertEqual(num2words(num, lang=LANG_CODE), expected)
    
    def test_cardinal_hundreds(self):
        """Test hundreds."""
        test_cases = [
            (100, "one hundred"),
            (200, "two hundred"),
            (500, "five hundred"),
            (999, "nine hundred ninety-nine"),
        ]
        for num, expected in test_cases:
            self.assertEqual(num2words(num, lang=LANG_CODE), expected)
    
    def test_cardinal_thousands(self):
        """Test thousands."""
        test_cases = [
            (1000, "one thousand"),
            (1234, "one thousand two hundred thirty-four"),
            (5000, "five thousand"),
            (10000, "ten thousand"),
            (100000, "one hundred thousand"),
            (999999, "nine hundred ninety-nine thousand nine hundred ninety-nine"),
        ]
        for num, expected in test_cases:
            self.assertEqual(num2words(num, lang=LANG_CODE), expected)
    
    def test_cardinal_millions(self):
        """Test millions."""
        test_cases = [
            (1000000, "one million"),
            (2000000, "two million"),
            (1234567, "one million two hundred thirty-four thousand five hundred sixty-seven"),
        ]
        for num, expected in test_cases:
            self.assertEqual(num2words(num, lang=LANG_CODE), expected)
    
    # ========================================================================
    # REQUIRED TEST CATEGORY 2: ORDINAL NUMBERS
    # ========================================================================
    
    def test_ordinal(self):
        """Test ordinal number conversion."""
        test_cases = [
            (0, "zeroth"),
            (1, "first"),
            (2, "second"),
            (3, "third"),
            (4, "fourth"),
            (5, "fifth"),
            (10, "tenth"),
            (11, "eleventh"),
            (12, "twelfth"),
            (20, "twentieth"),
            (21, "twenty-first"),
            (100, "one hundredth"),
            (101, "one hundred first"),
            (1000, "one thousandth"),
        ]
        for num, expected in test_cases:
            self.assertEqual(num2words(num, lang=LANG_CODE, to='ordinal'), expected)
    
    def test_ordinal_num(self):
        """Test ordinal number with numeral prefix."""
        test_cases = [
            (1, "1st"),
            (2, "2nd"),
            (3, "3rd"),
            (4, "4th"),
            (10, "10th"),
            (11, "11th"),
            (12, "12th"),
            (13, "13th"),
            (20, "20th"),
            (21, "21st"),
            (22, "22nd"),
            (23, "23rd"),
            (100, "100th"),
            (101, "101st"),
        ]
        for num, expected in test_cases:
            self.assertEqual(num2words(num, lang=LANG_CODE, to='ordinal_num'), expected)
    
    # ========================================================================
    # REQUIRED TEST CATEGORY 3: DECIMAL NUMBERS
    # ========================================================================
    
    def test_decimal(self):
        """Test decimal number conversion."""
        test_cases = [
            (0.0, "zero point zero"),
            (0.1, "zero point one"),
            (0.5, "zero point five"),
            (1.5, "one point five"),
            (10.25, "ten point two five"),
            (100.99, "one hundred point nine nine"),
            (1234.5678, "one thousand two hundred thirty-four point five six seven eight"),
        ]
        for num, expected in test_cases:
            self.assertEqual(num2words(num, lang=LANG_CODE), expected)
    
    # ========================================================================
    # REQUIRED TEST CATEGORY 4: NEGATIVE NUMBERS
    # ========================================================================
    
    def test_negative(self):
        """Test negative number conversion."""
        test_cases = [
            (-1, "minus one"),
            (-10, "minus ten"),
            (-100, "minus one hundred"),
            (-1000, "minus one thousand"),
            (-0.5, "minus zero point five"),
        ]
        for num, expected in test_cases:
            self.assertEqual(num2words(num, lang=LANG_CODE), expected)
    
    # ========================================================================
    # REQUIRED TEST CATEGORY 5: CURRENCY
    # ========================================================================
    
    def test_currency(self):
        """Test currency conversion with default currency for the language."""
        # Note: Replace 'USD' and expected outputs with appropriate 
        # default currency for your language
        test_cases = [
            (0, "zero dollars"),
            (1, "one dollar"),
            (2, "two dollars"),
            (10, "ten dollars"),
            (100, "one hundred dollars"),
            (1.50, "one dollar and fifty cents"),
            (10.25, "ten dollars and twenty-five cents"),
            (100.99, "one hundred dollars and ninety-nine cents"),
        ]
        for num, expected in test_cases:
            self.assertEqual(
                num2words(num, lang=LANG_CODE, to='currency'),
                expected
            )
    
    def test_currency_specific(self):
        """Test specific currency codes."""
        # Test at least USD, EUR, and GBP if supported
        test_cases = [
            (1, 'USD', "one dollar"),
            (1, 'EUR', "one euro"),
            (1, 'GBP', "one pound"),
            (2, 'USD', "two dollars"),
            (2, 'EUR', "two euros"),
            (2, 'GBP', "two pounds"),
        ]
        for num, currency, expected in test_cases:
            try:
                result = num2words(num, lang=LANG_CODE, to='currency', 
                                 currency=currency)
                self.assertEqual(result, expected)
            except NotImplementedError:
                # Currency might not be supported - that's OK
                pass
    
    # ========================================================================
    # REQUIRED TEST CATEGORY 6: YEAR
    # ========================================================================
    
    def test_year(self):
        """Test year conversion."""
        test_cases = [
            (1900, "nineteen hundred"),
            (1999, "nineteen ninety-nine"),
            (2000, "two thousand"),
            (2001, "two thousand one"),
            (2010, "two thousand ten"),
            (2020, "two thousand twenty"),
            (2021, "two thousand twenty-one"),
            (2100, "twenty-one hundred"),
        ]
        for num, expected in test_cases:
            self.assertEqual(num2words(num, lang=LANG_CODE, to='year'), expected)
    
    # ========================================================================
    # REQUIRED TEST CATEGORY 7: LARGE NUMBERS
    # ========================================================================
    
    def test_large_numbers(self):
        """Test very large numbers."""
        test_cases = [
            (1000000000, "one billion"),
            (1000000000000, "one trillion"),
        ]
        for num, expected in test_cases:
            self.assertEqual(num2words(num, lang=LANG_CODE), expected)
    
    # ========================================================================
    # REQUIRED TEST CATEGORY 8: EDGE CASES
    # ========================================================================
    
    def test_edge_cases(self):
        """Test edge cases and special scenarios."""
        # Test empty/None handling if applicable
        # Test very long decimal numbers
        # Test numbers with many zeros
        pass
    
    # ========================================================================
    # LANGUAGE-SPECIFIC TESTS
    # ========================================================================
    
    # Add any language-specific tests below this line
    # For example:
    # - Gender-specific ordinals (French, Spanish, etc.)
    # - Special counting systems (Japanese, Chinese, etc.)
    # - Dialectal variations
    # - Special formatting rules