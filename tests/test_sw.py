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


class Num2WordsSWTest(TestCase):
    """Test suite for Swahili number to words converter."""

    def test_basic_cardinal_numbers(self):
        """Test basic cardinal number conversion (0-10)."""
        self.assertEqual(num2words(0, lang="sw"), "sifuri")
        self.assertEqual(num2words(1, lang="sw"), "moja")
        self.assertEqual(num2words(2, lang="sw"), "mbili")
        self.assertEqual(num2words(3, lang="sw"), "tatu")
        self.assertEqual(num2words(4, lang="sw"), "nne")
        self.assertEqual(num2words(5, lang="sw"), "tano")
        self.assertEqual(num2words(6, lang="sw"), "sita")
        self.assertEqual(num2words(7, lang="sw"), "saba")
        self.assertEqual(num2words(8, lang="sw"), "nane")
        self.assertEqual(num2words(9, lang="sw"), "tisa")
        self.assertEqual(num2words(10, lang="sw"), "kumi")

    def test_teens(self):
        """Test teens (11-19) in Swahili."""
        self.assertEqual(num2words(11, lang="sw"), "kumi na moja")
        self.assertEqual(num2words(12, lang="sw"), "kumi na mbili")
        self.assertEqual(num2words(13, lang="sw"), "kumi na tatu")
        self.assertEqual(num2words(14, lang="sw"), "kumi na nne")
        self.assertEqual(num2words(15, lang="sw"), "kumi na tano")
        self.assertEqual(num2words(16, lang="sw"), "kumi na sita")
        self.assertEqual(num2words(17, lang="sw"), "kumi na saba")
        self.assertEqual(num2words(18, lang="sw"), "kumi na nane")
        self.assertEqual(num2words(19, lang="sw"), "kumi na tisa")

    def test_tens(self):
        """Test tens (20, 30, 40, etc.) in Swahili."""
        self.assertEqual(num2words(20, lang="sw"), "ishirini")
        self.assertEqual(num2words(30, lang="sw"), "thelathini")
        self.assertEqual(num2words(40, lang="sw"), "arobaini")
        self.assertEqual(num2words(50, lang="sw"), "hamsini")
        self.assertEqual(num2words(60, lang="sw"), "sitini")
        self.assertEqual(num2words(70, lang="sw"), "sabini")
        self.assertEqual(num2words(80, lang="sw"), "themanini")
        self.assertEqual(num2words(90, lang="sw"), "tisini")

    def test_compound_numbers(self):
        """Test compound numbers (21-99) in Swahili."""
        self.assertEqual(num2words(21, lang="sw"), "ishirini na moja")
        self.assertEqual(num2words(25, lang="sw"), "ishirini na tano")
        self.assertEqual(num2words(35, lang="sw"), "thelathini na tano")
        self.assertEqual(num2words(47, lang="sw"), "arobaini na saba")
        self.assertEqual(num2words(59, lang="sw"), "hamsini na tisa")
        self.assertEqual(num2words(64, lang="sw"), "sitini na nne")
        self.assertEqual(num2words(78, lang="sw"), "sabini na nane")
        self.assertEqual(num2words(82, lang="sw"), "themanini na mbili")
        self.assertEqual(num2words(99, lang="sw"), "tisini na tisa")

    def test_hundreds(self):
        """Test hundreds in Swahili."""
        self.assertEqual(num2words(100, lang="sw"), "mia moja")
        self.assertEqual(num2words(200, lang="sw"), "mia mbili")
        self.assertEqual(num2words(300, lang="sw"), "mia tatu")
        self.assertEqual(num2words(400, lang="sw"), "mia nne")
        self.assertEqual(num2words(500, lang="sw"), "mia tano")
        self.assertEqual(num2words(600, lang="sw"), "mia sita")
        self.assertEqual(num2words(700, lang="sw"), "mia saba")
        self.assertEqual(num2words(800, lang="sw"), "mia nane")
        self.assertEqual(num2words(900, lang="sw"), "mia tisa")

    def test_hundreds_with_tens_and_units(self):
        """Test hundreds with tens and units in Swahili."""
        self.assertEqual(num2words(101, lang="sw"), "mia moja na moja")
        self.assertEqual(num2words(111, lang="sw"), "mia moja na kumi na moja")
        self.assertEqual(num2words(125, lang="sw"), "mia moja na ishirini na tano")
        self.assertEqual(num2words(235, lang="sw"), "mia mbili na thelathini na tano")
        self.assertEqual(num2words(345, lang="sw"), "mia tatu na arobaini na tano")
        self.assertEqual(num2words(456, lang="sw"), "mia nne na hamsini na sita")
        self.assertEqual(num2words(567, lang="sw"), "mia tano na sitini na saba")
        self.assertEqual(num2words(678, lang="sw"), "mia sita na sabini na nane")
        self.assertEqual(num2words(789, lang="sw"), "mia saba na themanini na tisa")
        self.assertEqual(num2words(999, lang="sw"), "mia tisa na tisini na tisa")

    def test_thousands(self):
        """Test thousands in Swahili."""
        self.assertEqual(num2words(1000, lang="sw"), "elfu moja")
        self.assertEqual(num2words(2000, lang="sw"), "elfu mbili")
        self.assertEqual(num2words(3000, lang="sw"), "elfu tatu")
        self.assertEqual(num2words(4000, lang="sw"), "elfu nne")
        self.assertEqual(num2words(5000, lang="sw"), "elfu tano")
        self.assertEqual(num2words(6000, lang="sw"), "elfu sita")
        self.assertEqual(num2words(7000, lang="sw"), "elfu saba")
        self.assertEqual(num2words(8000, lang="sw"), "elfu nane")
        self.assertEqual(num2words(9000, lang="sw"), "elfu tisa")
        self.assertEqual(num2words(10000, lang="sw"), "elfu kumi")

    def test_thousands_complex(self):
        """Test complex thousand numbers in Swahili."""
        self.assertEqual(num2words(1001, lang="sw"), "elfu moja na moja")
        self.assertEqual(num2words(1010, lang="sw"), "elfu moja na kumi")
        self.assertEqual(num2words(1100, lang="sw"), "elfu moja na mia moja")
        self.assertEqual(num2words(1234, lang="sw"), "elfu moja na mia mbili na thelathini na nne")
        self.assertEqual(num2words(2345, lang="sw"), "elfu mbili na mia tatu na arobaini na tano")
        self.assertEqual(num2words(5678, lang="sw"), "elfu tano na mia sita na sabini na nane")
        self.assertEqual(num2words(9999, lang="sw"), "elfu tisa na mia tisa na tisini na tisa")

    def test_ten_thousands(self):
        """Test ten thousands and higher in Swahili."""
        self.assertEqual(num2words(10000, lang="sw"), "elfu kumi")
        self.assertEqual(num2words(15000, lang="sw"), "elfu kumi na tano")
        self.assertEqual(num2words(20000, lang="sw"), "elfu ishirini")
        self.assertEqual(num2words(25000, lang="sw"), "elfu ishirini na tano")
        self.assertEqual(num2words(50000, lang="sw"), "elfu hamsini")
        self.assertEqual(num2words(99000, lang="sw"), "elfu tisini na tisa")
        self.assertEqual(num2words(99999, lang="sw"), "elfu tisini na tisa na mia tisa na tisini na tisa")

    def test_hundred_thousands(self):
        """Test hundred thousands in Swahili."""
        self.assertEqual(num2words(100000, lang="sw"), "elfu mia moja")
        self.assertEqual(num2words(200000, lang="sw"), "elfu mia mbili")
        self.assertEqual(num2words(500000, lang="sw"), "elfu mia tano")
        self.assertEqual(num2words(999000, lang="sw"), "elfu mia tisa na tisini na tisa")
        self.assertEqual(num2words(999999, lang="sw"), "elfu mia tisa na tisini na tisa na mia tisa na tisini na tisa")

    def test_millions(self):
        """Test millions in Swahili."""
        self.assertEqual(num2words(1000000, lang="sw"), "milioni moja")
        self.assertEqual(num2words(2000000, lang="sw"), "milioni mbili")
        self.assertEqual(num2words(5000000, lang="sw"), "milioni tano")
        self.assertEqual(num2words(1000001, lang="sw"), "milioni moja na moja")
        self.assertEqual(num2words(1001000, lang="sw"), "milioni moja na elfu moja")
        self.assertEqual(num2words(1234567, lang="sw"), "milioni moja na elfu mia mbili na thelathini na nne na mia tano na sitini na saba")
        self.assertEqual(num2words(9999999, lang="sw"), "milioni tisa na elfu mia tisa na tisini na tisa na mia tisa na tisini na tisa")

    def test_tens_of_millions(self):
        """Test tens of millions in Swahili."""
        self.assertEqual(num2words(10000000, lang="sw"), "milioni kumi")
        self.assertEqual(num2words(50000000, lang="sw"), "milioni hamsini")
        self.assertEqual(num2words(99000000, lang="sw"), "milioni tisini na tisa")

    def test_hundreds_of_millions(self):
        """Test hundreds of millions in Swahili."""
        self.assertEqual(num2words(100000000, lang="sw"), "milioni mia moja")
        self.assertEqual(num2words(500000000, lang="sw"), "milioni mia tano")
        self.assertEqual(num2words(999000000, lang="sw"), "milioni mia tisa na tisini na tisa")

    def test_billions(self):
        """Test billions in Swahili."""
        self.assertEqual(num2words(1000000000, lang="sw"), "bilioni moja")
        self.assertEqual(num2words(2000000000, lang="sw"), "bilioni mbili")
        self.assertEqual(num2words(5000000000, lang="sw"), "bilioni tano")

    def test_negative_numbers(self):
        """Test negative numbers in Swahili."""
        self.assertEqual(num2words(-1, lang="sw"), "hasara moja")
        self.assertEqual(num2words(-5, lang="sw"), "hasara tano")
        self.assertEqual(num2words(-10, lang="sw"), "hasara kumi")
        self.assertEqual(num2words(-15, lang="sw"), "hasara kumi na tano")
        self.assertEqual(num2words(-20, lang="sw"), "hasara ishirini")
        self.assertEqual(num2words(-100, lang="sw"), "hasara mia moja")
        self.assertEqual(num2words(-234, lang="sw"), "hasara mia mbili na thelathini na nne")
        self.assertEqual(num2words(-1000, lang="sw"), "hasara elfu moja")
        self.assertEqual(num2words(-999999, lang="sw"), "hasara elfu mia tisa na tisini na tisa na mia tisa na tisini na tisa")

    def test_decimal_numbers(self):
        """Test decimal numbers in Swahili."""
        self.assertEqual(num2words(0.5, lang="sw"), "sifuri nukta tano")
        self.assertEqual(num2words(0.7, lang="sw"), "sifuri nukta saba")
        self.assertEqual(num2words(1.5, lang="sw"), "moja nukta tano")
        self.assertEqual(num2words(2.3, lang="sw"), "mbili nukta tatu")
        self.assertEqual(num2words(5.75, lang="sw"), "tano nukta saba tano")
        self.assertEqual(num2words(10.5, lang="sw"), "kumi nukta tano")
        self.assertEqual(num2words(15.25, lang="sw"), "kumi na tano nukta mbili tano")
        self.assertEqual(num2words(100.01, lang="sw"), "mia moja nukta sifuri moja")
        self.assertEqual(num2words(999.99, lang="sw"), "mia tisa na tisini na tisa nukta tisa tisa")

    def test_negative_decimals(self):
        """Test negative decimal numbers in Swahili."""
        self.assertEqual(num2words(-0.4, lang="sw"), "hasara sifuri nukta nne")
        self.assertEqual(num2words(-0.5, lang="sw"), "hasara sifuri nukta tano")
        self.assertEqual(num2words(-1.4, lang="sw"), "hasara moja nukta nne")
        self.assertEqual(num2words(-10.25, lang="sw"), "hasara kumi nukta mbili tano")
        self.assertEqual(num2words(-100.5, lang="sw"), "hasara mia moja nukta tano")

    def test_ordinal_numbers(self):
        """Test ordinal numbers in Swahili."""
        self.assertEqual(num2words(1, lang="sw", to="ordinal"), "wa kwanza")
        self.assertEqual(num2words(2, lang="sw", to="ordinal"), "wa pili")
        self.assertEqual(num2words(3, lang="sw", to="ordinal"), "wa tatu")
        self.assertEqual(num2words(4, lang="sw", to="ordinal"), "wa nne")
        self.assertEqual(num2words(5, lang="sw", to="ordinal"), "wa tano")
        self.assertEqual(num2words(6, lang="sw", to="ordinal"), "wa sita")
        self.assertEqual(num2words(7, lang="sw", to="ordinal"), "wa saba")
        self.assertEqual(num2words(8, lang="sw", to="ordinal"), "wa nane")
        self.assertEqual(num2words(9, lang="sw", to="ordinal"), "wa tisa")
        self.assertEqual(num2words(10, lang="sw", to="ordinal"), "wa kumi")
        self.assertEqual(num2words(11, lang="sw", to="ordinal"), "wa kumi na moja")
        self.assertEqual(num2words(20, lang="sw", to="ordinal"), "wa ishirini")
        self.assertEqual(num2words(21, lang="sw", to="ordinal"), "wa ishirini na moja")
        self.assertEqual(num2words(100, lang="sw", to="ordinal"), "wa mia moja")
        self.assertEqual(num2words(1000, lang="sw", to="ordinal"), "wa elfu moja")

    def test_ordinal_num(self):
        """Test ordinal number suffix format."""
        self.assertEqual(num2words(1, lang="sw", to="ordinal_num"), "1.")
        self.assertEqual(num2words(2, lang="sw", to="ordinal_num"), "2.")
        self.assertEqual(num2words(10, lang="sw", to="ordinal_num"), "10.")
        self.assertEqual(num2words(21, lang="sw", to="ordinal_num"), "21.")
        self.assertEqual(num2words(103, lang="sw", to="ordinal_num"), "103.")

    def test_currency_basic(self):
        """Test basic currency conversion in Swahili."""
        # USD tests
        self.assertEqual(
            num2words(1, lang="sw", to="currency", currency="USD"),
            "dola moja"
        )
        self.assertEqual(
            num2words(2, lang="sw", to="currency", currency="USD"),
            "dola mbili"
        )
        self.assertEqual(
            num2words(100, lang="sw", to="currency", currency="USD"),
            "dola mia moja"
        )

        # EUR tests  
        self.assertEqual(
            num2words(1, lang="sw", to="currency", currency="EUR"),
            "yuro moja"
        )
        self.assertEqual(
            num2words(5, lang="sw", to="currency", currency="EUR"),
            "yuro tano"
        )

        # GBP tests
        self.assertEqual(
            num2words(1, lang="sw", to="currency", currency="GBP"),
            "pauni moja"
        )

    def test_currency_with_cents(self):
        """Test currency conversion with cents/fractional values."""
        self.assertEqual(
            num2words(1.50, lang="sw", to="currency", currency="USD"),
            "dola moja na senti hamsini"
        )
        self.assertEqual(
            num2words(5.25, lang="sw", to="currency", currency="USD"),
            "dola tano na senti ishirini na tano"
        )
        self.assertEqual(
            num2words(100.99, lang="sw", to="currency", currency="USD"),
            "dola mia moja na senti tisini na tisa"
        )

        # Euro with cents
        self.assertEqual(
            num2words(2.75, lang="sw", to="currency", currency="EUR"),
            "yuro mbili na senti sabini na tano"
        )

        # Test with only cents (no whole currency)
        self.assertEqual(
            num2words(0.50, lang="sw", to="currency", currency="USD"),
            "senti hamsini"
        )
        self.assertEqual(
            num2words(0.25, lang="sw", to="currency", currency="USD"),
            "senti ishirini na tano"
        )

    def test_currency_negative(self):
        """Test negative currency values."""
        self.assertEqual(
            num2words(-1, lang="sw", to="currency", currency="USD"),
            "hasara dola moja"
        )
        self.assertEqual(
            num2words(-5.50, lang="sw", to="currency", currency="USD"),
            "hasara dola tano na senti hamsini"
        )

    def test_currency_large_amounts(self):
        """Test currency with large amounts."""
        self.assertEqual(
            num2words(1000, lang="sw", to="currency", currency="USD"),
            "dola elfu moja"
        )
        self.assertEqual(
            num2words(1000000, lang="sw", to="currency", currency="USD"),
            "dola milioni moja"
        )

    def test_year_conversion(self):
        """Test year conversion in Swahili."""
        self.assertEqual(num2words(1990, lang="sw", to="year"), "elfu moja na mia tisa na tisini")
        self.assertEqual(num2words(2000, lang="sw", to="year"), "elfu mbili")
        self.assertEqual(num2words(2024, lang="sw", to="year"), "elfu mbili na ishirini na nne")
        self.assertEqual(num2words(1066, lang="sw", to="year"), "elfu moja na sitini na sita")
        self.assertEqual(num2words(1865, lang="sw", to="year"), "elfu moja na mia nane na sitini na tano")

    def test_edge_cases(self):
        """Test edge cases and special scenarios."""
        # Test zero explicitly
        self.assertEqual(num2words(0, lang="sw"), "sifuri")
        
        # Test very large numbers
        self.assertEqual(num2words(1000000000, lang="sw"), "bilioni moja")
        self.assertEqual(num2words(1000000000000, lang="sw"), "trilioni moja")
        
        # Test numbers around boundaries
        self.assertEqual(num2words(999, lang="sw"), "mia tisa na tisini na tisa")
        self.assertEqual(num2words(1001, lang="sw"), "elfu moja na moja")
        self.assertEqual(num2words(999999, lang="sw"), "elfu mia tisa na tisini na tisa na mia tisa na tisini na tisa")
        self.assertEqual(num2words(1000001, lang="sw"), "milioni moja na moja")

    def test_comprehensive_number_ranges(self):
        """Test comprehensive number ranges to ensure completeness."""
        # Test all basic numbers 1-20
        expected_basic = [
            "moja", "mbili", "tatu", "nne", "tano", 
            "sita", "saba", "nane", "tisa", "kumi",
            "kumi na moja", "kumi na mbili", "kumi na tatu", "kumi na nne", "kumi na tano",
            "kumi na sita", "kumi na saba", "kumi na nane", "kumi na tisa", "ishirini"
        ]
        for i, expected in enumerate(expected_basic, 1):
            self.assertEqual(num2words(i, lang="sw"), expected)

        # Test all tens
        expected_tens = {
            20: "ishirini", 30: "thelathini", 40: "arobaini", 50: "hamsini",
            60: "sitini", 70: "sabini", 80: "themanini", 90: "tisini"
        }
        for num, expected in expected_tens.items():
            self.assertEqual(num2words(num, lang="sw"), expected)

        # Test all hundreds
        expected_hundreds = {
            100: "mia moja", 200: "mia mbili", 300: "mia tatu", 400: "mia nne",
            500: "mia tano", 600: "mia sita", 700: "mia saba", 800: "mia nane", 900: "mia tisa"
        }
        for num, expected in expected_hundreds.items():
            self.assertEqual(num2words(num, lang="sw"), expected)