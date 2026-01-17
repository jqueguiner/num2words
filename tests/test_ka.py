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
from num2words.lang_KA import Num2Word_KA


class Num2WordsKATest(TestCase):
    """Test suite for Georgian number to words converter."""

    def test_basic_cardinal_numbers(self):
        """Test basic cardinal number conversion."""
        # Single digits
        self.assertEqual(num2words(0, lang="ka"), "ნული")
        self.assertEqual(num2words(1, lang="ka"), "ერთი")
        self.assertEqual(num2words(2, lang="ka"), "ორი")
        self.assertEqual(num2words(3, lang="ka"), "სამი")
        self.assertEqual(num2words(4, lang="ka"), "ოთხი")
        self.assertEqual(num2words(5, lang="ka"), "ხუთი")
        self.assertEqual(num2words(6, lang="ka"), "ექვსი")
        self.assertEqual(num2words(7, lang="ka"), "შვიდი")
        self.assertEqual(num2words(8, lang="ka"), "რვა")
        self.assertEqual(num2words(9, lang="ka"), "ცხრა")

        # Teens
        self.assertEqual(num2words(10, lang="ka"), "ათი")
        self.assertEqual(num2words(11, lang="ka"), "თერთმეტი")
        self.assertEqual(num2words(12, lang="ka"), "თორმეტი")
        self.assertEqual(num2words(13, lang="ka"), "ცამეტი")
        self.assertEqual(num2words(14, lang="ka"), "თოთხმეტი")
        self.assertEqual(num2words(15, lang="ka"), "თხუთმეტი")
        self.assertEqual(num2words(16, lang="ka"), "თექვსმეტი")
        self.assertEqual(num2words(17, lang="ka"), "ჩვიდმეტი")
        self.assertEqual(num2words(18, lang="ka"), "თვრამეტი")
        self.assertEqual(num2words(19, lang="ka"), "ცხრამეტი")

        # Tens
        self.assertEqual(num2words(20, lang="ka"), "ოცი")
        self.assertEqual(num2words(21, lang="ka"), "ოცდაერთი")
        self.assertEqual(num2words(25, lang="ka"), "ოცდახუთი")
        self.assertEqual(num2words(30, lang="ka"), "ოცდაათი")
        self.assertEqual(num2words(40, lang="ka"), "ორმოცი")
        self.assertEqual(num2words(42, lang="ka"), "ორმოცდაორი")
        self.assertEqual(num2words(50, lang="ka"), "ორმოცდაათი")
        self.assertEqual(num2words(60, lang="ka"), "სამოცი")
        self.assertEqual(num2words(70, lang="ka"), "სამოცდაათი")
        self.assertEqual(num2words(80, lang="ka"), "ოთხმოცი")
        self.assertEqual(num2words(90, lang="ka"), "ოთხმოცდაათი")
        self.assertEqual(num2words(99, lang="ka"), "ოთხმოცდაცხრამეტი")

    def test_hundreds(self):
        """Test hundreds conversion."""
        self.assertEqual(num2words(100, lang="ka"), "ასი")
        self.assertEqual(num2words(101, lang="ka"), "ას ერთი")
        self.assertEqual(num2words(111, lang="ka"), "ას თერთმეტი")
        self.assertEqual(num2words(150, lang="ka"), "ას ორმოცდაათი")
        self.assertEqual(num2words(200, lang="ka"), "ორასი")
        self.assertEqual(num2words(300, lang="ka"), "სამასი")
        self.assertEqual(num2words(400, lang="ka"), "ოთხასი")
        self.assertEqual(num2words(500, lang="ka"), "ხუთასი")
        self.assertEqual(num2words(600, lang="ka"), "ექვსასი")
        self.assertEqual(num2words(700, lang="ka"), "შვიდასი")
        self.assertEqual(num2words(800, lang="ka"), "რვაასი")
        self.assertEqual(num2words(900, lang="ka"), "ცხრაასი")
        self.assertEqual(num2words(999, lang="ka"), "ცხრაას ოთხმოცდაცხრამეტი")

    def test_thousands(self):
        """Test thousands conversion."""
        self.assertEqual(num2words(1000, lang="ka"), "ათასი")
        self.assertEqual(num2words(1001, lang="ka"), "ათას ერთი")
        self.assertEqual(num2words(1100, lang="ka"), "ათას ასი")
        self.assertEqual(num2words(1234, lang="ka"), "ათას ორას ოცდათოთხმეტი")
        self.assertEqual(num2words(2000, lang="ka"), "ორი ათასი")
        self.assertEqual(num2words(10000, lang="ka"), "ათი ათასი")
        self.assertEqual(num2words(100000, lang="ka"), "ასი ათასი")
        self.assertEqual(num2words(999999, lang="ka"), "ცხრაას ოთხმოცდაცხრამეტი ათას ცხრაას ოთხმოცდაცხრამეტი")

    def test_millions(self):
        """Test millions conversion."""
        self.assertEqual(num2words(1000000, lang="ka"), "ერთი მილიონი")
        self.assertEqual(num2words(2000000, lang="ka"), "ორი მილიონი")
        self.assertEqual(num2words(1000001, lang="ka"), "ერთი მილიონ ერთი")
        self.assertEqual(num2words(1234567, lang="ka"), "ერთი მილიონ ორას ოცდათოთხმეტი ათას ხუთას სამოცდაშვიდი")

    def test_billions(self):
        """Test billions conversion."""
        self.assertEqual(num2words(1000000000, lang="ka"), "ერთი მილიარდი")
        self.assertEqual(num2words(2000000000, lang="ka"), "ორი მილიარდი")
        self.assertEqual(num2words(1000000001, lang="ka"), "ერთი მილიარდ ერთი")

    def test_ordinal_numbers(self):
        """Test ordinal number conversion."""
        self.assertEqual(num2words(1, lang="ka", to="ordinal"), "პირველი")
        self.assertEqual(num2words(2, lang="ka", to="ordinal"), "მეორე")
        self.assertEqual(num2words(3, lang="ka", to="ordinal"), "მესამე")
        self.assertEqual(num2words(4, lang="ka", to="ordinal"), "მეოთხე")
        self.assertEqual(num2words(5, lang="ka", to="ordinal"), "მეხუთე")
        self.assertEqual(num2words(6, lang="ka", to="ordinal"), "მეექვსე")
        self.assertEqual(num2words(7, lang="ka", to="ordinal"), "მეშვიდე")
        self.assertEqual(num2words(8, lang="ka", to="ordinal"), "მერვე")
        self.assertEqual(num2words(9, lang="ka", to="ordinal"), "მეცხრე")
        self.assertEqual(num2words(10, lang="ka", to="ordinal"), "მეათე")
        self.assertEqual(num2words(11, lang="ka", to="ordinal"), "მეთერთმეტე")
        self.assertEqual(num2words(20, lang="ka", to="ordinal"), "მეოცე")
        self.assertEqual(num2words(21, lang="ka", to="ordinal"), "ოცდაპირველი")
        self.assertEqual(num2words(100, lang="ka", to="ordinal"), "მეასე")
        self.assertEqual(num2words(101, lang="ka", to="ordinal"), "ას პირველი")
        self.assertEqual(num2words(1000, lang="ka", to="ordinal"), "მეათასე")

    def test_ordinal_num(self):
        """Test ordinal number with suffix."""
        self.assertEqual(num2words(1, lang="ka", to="ordinal_num"), "1-ლი")
        self.assertEqual(num2words(2, lang="ka", to="ordinal_num"), "2-ე")
        self.assertEqual(num2words(3, lang="ka", to="ordinal_num"), "3-ე")
        self.assertEqual(num2words(10, lang="ka", to="ordinal_num"), "10-ე")
        self.assertEqual(num2words(21, lang="ka", to="ordinal_num"), "21-ე")
        self.assertEqual(num2words(100, lang="ka", to="ordinal_num"), "100-ე")

    def test_currency_gel(self):
        """Test Georgian Lari (GEL) currency conversion."""
        self.assertEqual(
            num2words(1, lang="ka", to="currency", currency="GEL"),
            "ერთი ლარი"
        )
        self.assertEqual(
            num2words(2, lang="ka", to="currency", currency="GEL"),
            "ორი ლარი"
        )
        self.assertEqual(
            num2words(100, lang="ka", to="currency", currency="GEL"),
            "ასი ლარი"
        )
        self.assertEqual(
            num2words(1.50, lang="ka", to="currency", currency="GEL"),
            "ერთი ლარი ორმოცდაათი თეთრი"
        )
        self.assertEqual(
            num2words(0.99, lang="ka", to="currency", currency="GEL"),
            "ოთხმოცდაცხრამეტი თეთრი"
        )

    def test_currency_usd(self):
        """Test USD currency conversion."""
        self.assertEqual(
            num2words(1, lang="ka", to="currency", currency="USD"),
            "ერთი დოლარი"
        )
        self.assertEqual(
            num2words(100, lang="ka", to="currency", currency="USD"),
            "ასი დოლარი"
        )
        self.assertEqual(
            num2words(1.50, lang="ka", to="currency", currency="USD"),
            "ერთი დოლარი ორმოცდაათი ცენტი"
        )

    def test_currency_eur(self):
        """Test EUR currency conversion."""
        self.assertEqual(
            num2words(1, lang="ka", to="currency", currency="EUR"),
            "ერთი ევრო"
        )
        self.assertEqual(
            num2words(100, lang="ka", to="currency", currency="EUR"),
            "ასი ევრო"
        )
        self.assertEqual(
            num2words(2.75, lang="ka", to="currency", currency="EUR"),
            "ორი ევრო სამოცდათხუთმეტი ცენტი"
        )

    def test_negative_numbers(self):
        """Test negative number conversion."""
        self.assertEqual(num2words(-1, lang="ka"), "მინუს ერთი")
        self.assertEqual(num2words(-42, lang="ka"), "მინუს ორმოცდაორი")
        self.assertEqual(num2words(-100, lang="ka"), "მინუს ასი")
        self.assertEqual(num2words(-1000, lang="ka"), "მინუს ათასი")

    def test_decimal_numbers(self):
        """Test decimal number conversion."""
        self.assertEqual(num2words(0.5, lang="ka"), "ნული მთელი ხუთი")
        self.assertEqual(num2words(1.5, lang="ka"), "ერთი მთელი ხუთი")
        self.assertEqual(num2words(3.14, lang="ka"), "სამი მთელი ერთი ოთხი")
        self.assertEqual(num2words(0.01, lang="ka"), "ნული მთელი ნული ერთი")
        self.assertEqual(num2words(10.99, lang="ka"), "ათი მთელი ცხრა ცხრა")

    def test_negative_decimals(self):
        """Test negative decimal number conversion."""
        self.assertEqual(num2words(-0.4, lang="ka"), "მინუს ნული მთელი ოთხი")
        self.assertEqual(num2words(-0.5, lang="ka"), "მინუს ნული მთელი ხუთი")
        self.assertEqual(num2words(-1.4, lang="ka"), "მინუს ერთი მთელი ოთხი")
        self.assertEqual(num2words(-2.75, lang="ka"), "მინუს ორი მთელი შვიდი ხუთი")

    def test_year_conversion(self):
        """Test year conversion."""
        self.assertEqual(num2words(2000, lang="ka", to="year"), "ორი ათასი წელი")
        self.assertEqual(num2words(2023, lang="ka", to="year"), "ორი ათას ოცდასამი წელი")
        self.assertEqual(num2words(1990, lang="ka", to="year"), "ათას ცხრაას ოთხმოცდაათი წელი")

    def test_large_numbers(self):
        """Test very large numbers."""
        converter = Num2Word_KA()
        
        # Test trillion
        self.assertEqual(num2words(1000000000000, lang="ka"), "ერთი ტრილიონი")
        
        # Test complex large numbers
        result = converter.to_cardinal(1234567890123)
        self.assertTrue(isinstance(result, str))
        self.assertTrue(len(result) > 0)
        
        # Test edge cases
        result2 = converter.to_cardinal(999999999999)
        self.assertTrue(isinstance(result2, str))
        self.assertTrue("ცხრაას" in result2)

    def test_zero_special_cases(self):
        """Test special cases involving zero."""
        self.assertEqual(num2words(0, lang="ka"), "ნული")
        self.assertEqual(num2words(0, lang="ka", to="ordinal"), "ნულოვანი")
        self.assertEqual(num2words(0.0, lang="ka", to="currency", currency="GEL"), "ნული ლარი")

    def test_edge_cases(self):
        """Test edge cases and special scenarios."""
        # Test 1000 special case
        self.assertEqual(num2words(1000, lang="ka"), "ათასი")
        
        # Test million/billion edge cases
        self.assertEqual(num2words(1000000, lang="ka"), "ერთი მილიონი")
        self.assertEqual(num2words(1000000000, lang="ka"), "ერთი მილიარდი")
        
        # Test complex combinations
        self.assertEqual(num2words(1001001, lang="ka"), "ერთი მილიონ ათას ერთი")
        self.assertEqual(num2words(1000001000, lang="ka"), "ერთი მილიარდ ათასი")

    def test_pluralization(self):
        """Test pluralization rules."""
        converter = Num2Word_KA()
        
        # Test basic pluralization
        self.assertEqual(converter.pluralize(1, ("ლარი", "ლარი")), "ლარი")
        self.assertEqual(converter.pluralize(2, ("ლარი", "ლარი")), "ლარი")
        self.assertEqual(converter.pluralize(5, ("ლარი", "ლარი")), "ლარი")
        
        # Test empty forms
        self.assertEqual(converter.pluralize(5, []), "")
        self.assertEqual(converter.pluralize(5, ["ლარი"]), "ლარი")

    def test_merge_method(self):
        """Test merge method functionality."""
        converter = Num2Word_KA()
        
        # Basic merge tests
        result = converter.merge(("ორი", 2), ("ათასი", 1000))
        self.assertEqual(result[0], "ორი ათასი")
        self.assertEqual(result[1], 2000)
        
        result2 = converter.merge(("სამი", 3), ("ასი", 100))
        self.assertEqual(result2[0], "სამასი")
        self.assertEqual(result2[1], 300)

    def test_special_georgian_combinations(self):
        """Test special Georgian number combinations."""
        # Test vigesimal system combinations
        self.assertEqual(num2words(23, lang="ka"), "ოცდასამი")
        self.assertEqual(num2words(37, lang="ka"), "ოცდაჩვიდმეტი")
        self.assertEqual(num2words(44, lang="ka"), "ორმოცდაოთხი")
        self.assertEqual(num2words(67, lang="ka"), "სამოცდაშვიდი")
        self.assertEqual(num2words(89, lang="ka"), "ოთხმოცდაცხრა")
        
        # Test hundred combinations
        self.assertEqual(num2words(345, lang="ka"), "სამას ორმოცდახუთი")
        self.assertEqual(num2words(678, lang="ka"), "ექვსას სამოცდათვრამეტი")

    def test_currency_negative(self):
        """Test negative currency conversion."""
        self.assertEqual(
            num2words(-1.50, lang="ka", to="currency", currency="GEL"),
            "მინუს ერთი ლარი ორმოცდაათი თეთრი"
        )
        self.assertEqual(
            num2words(-100, lang="ka", to="currency", currency="USD"),
            "მინუს ასი დოლარი"
        )

    def test_unknown_currency(self):
        """Test unknown currency fallback."""
        self.assertEqual(
            num2words(10, lang="ka", to="currency", currency="XXX"),
            "ათი"
        )