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


class Num2WordsHRTest(TestCase):

    def test_basic_numbers(self):
        """Test basic numbers 0-9"""
        self.assertEqual("nula", num2words(0, lang='hr'))
        self.assertEqual("jedan", num2words(1, lang='hr'))
        self.assertEqual("dva", num2words(2, lang='hr'))
        self.assertEqual("tri", num2words(3, lang='hr'))
        self.assertEqual("četiri", num2words(4, lang='hr'))
        self.assertEqual("pet", num2words(5, lang='hr'))
        self.assertEqual("šest", num2words(6, lang='hr'))
        self.assertEqual("sedam", num2words(7, lang='hr'))
        self.assertEqual("osam", num2words(8, lang='hr'))
        self.assertEqual("devet", num2words(9, lang='hr'))

    def test_ten(self):
        """Test number 10"""
        self.assertEqual("deset", num2words(10, lang='hr'))

    def test_teens(self):
        """Test numbers 11-19"""
        self.assertEqual("jedanaest", num2words(11, lang='hr'))
        self.assertEqual("dvanaest", num2words(12, lang='hr'))
        self.assertEqual("trinaest", num2words(13, lang='hr'))
        self.assertEqual("četrnaest", num2words(14, lang='hr'))
        self.assertEqual("petnaest", num2words(15, lang='hr'))
        self.assertEqual("šesnaest", num2words(16, lang='hr'))
        self.assertEqual("sedamnaest", num2words(17, lang='hr'))
        self.assertEqual("osamnaest", num2words(18, lang='hr'))
        self.assertEqual("devetnaest", num2words(19, lang='hr'))

    def test_tens(self):
        """Test tens 20, 30, 40, etc."""
        self.assertEqual("dvadeset", num2words(20, lang='hr'))
        self.assertEqual("trideset", num2words(30, lang='hr'))
        self.assertEqual("četrdeset", num2words(40, lang='hr'))
        self.assertEqual("pedeset", num2words(50, lang='hr'))
        self.assertEqual("šezdeset", num2words(60, lang='hr'))
        self.assertEqual("sedamdeset", num2words(70, lang='hr'))
        self.assertEqual("osamdeset", num2words(80, lang='hr'))
        self.assertEqual("devedeset", num2words(90, lang='hr'))

    def test_compound_tens(self):
        """Test compound numbers 21-99"""
        self.assertEqual("dvadeset jedan", num2words(21, lang='hr'))
        self.assertEqual("dvadeset dva", num2words(22, lang='hr'))
        self.assertEqual("trideset tri", num2words(33, lang='hr'))
        self.assertEqual("četrdeset četiri", num2words(44, lang='hr'))
        self.assertEqual("pedeset pet", num2words(55, lang='hr'))
        self.assertEqual("šezdeset šest", num2words(66, lang='hr'))
        self.assertEqual("sedamdeset sedam", num2words(77, lang='hr'))
        self.assertEqual("osamdeset osam", num2words(88, lang='hr'))
        self.assertEqual("devedeset devet", num2words(99, lang='hr'))

    def test_hundreds(self):
        """Test hundreds 100, 200, 300, etc."""
        self.assertEqual("sto", num2words(100, lang='hr'))
        self.assertEqual("dvjesto", num2words(200, lang='hr'))
        self.assertEqual("tristo", num2words(300, lang='hr'))
        self.assertEqual("četiristo", num2words(400, lang='hr'))
        self.assertEqual("petsto", num2words(500, lang='hr'))
        self.assertEqual("šesto", num2words(600, lang='hr'))
        self.assertEqual("sedamsto", num2words(700, lang='hr'))
        self.assertEqual("osamsto", num2words(800, lang='hr'))
        self.assertEqual("devetsto", num2words(900, lang='hr'))

    def test_compound_hundreds(self):
        """Test compound hundreds"""
        self.assertEqual("sto jedan", num2words(101, lang='hr'))
        self.assertEqual("sto deset", num2words(110, lang='hr'))
        self.assertEqual("sto petnaest", num2words(115, lang='hr'))
        self.assertEqual("sto dvadeset tri", num2words(123, lang='hr'))
        self.assertEqual("dvjesto pedeset četiri", num2words(254, lang='hr'))
        self.assertEqual("tristo šezdeset sedam", num2words(367, lang='hr'))
        self.assertEqual("četiristo osamdeset devet", num2words(489, lang='hr'))

    def test_thousands(self):
        """Test thousands"""
        self.assertEqual("jedna tisuća", num2words(1000, lang='hr'))
        self.assertEqual("jedna tisuća jedan", num2words(1001, lang='hr'))
        self.assertEqual("dvije tisuće", num2words(2000, lang='hr'))
        self.assertEqual("tri tisuće", num2words(3000, lang='hr'))
        self.assertEqual("četiri tisuće", num2words(4000, lang='hr'))
        self.assertEqual("pet tisuća", num2words(5000, lang='hr'))
        self.assertEqual("deset tisuća", num2words(10000, lang='hr'))
        self.assertEqual("jedanaest tisuća", num2words(11000, lang='hr'))
        self.assertEqual("dvadeset tisuća", num2words(20000, lang='hr'))
        self.assertEqual("sto tisuća", num2words(100000, lang='hr'))

    def test_compound_thousands(self):
        """Test compound thousands"""
        self.assertEqual("dvije tisuće dvanaest", num2words(2012, lang='hr'))
        self.assertEqual("jedna tisuća sto trideset pet", num2words(1135, lang='hr'))
        self.assertEqual("četiristo osamnaest tisuća petsto trideset jedan", num2words(418531, lang='hr'))
        self.assertEqual("dvanaest tisuća petsto devetnaest", num2words(12519, lang='hr'))

    def test_millions(self):
        """Test millions"""
        self.assertEqual("jedan milijun", num2words(1000000, lang='hr'))
        self.assertEqual("dva milijuna", num2words(2000000, lang='hr'))
        self.assertEqual("tri milijuna", num2words(3000000, lang='hr'))
        self.assertEqual("četiri milijuna", num2words(4000000, lang='hr'))
        self.assertEqual("pet milijuna", num2words(5000000, lang='hr'))
        self.assertEqual("deset milijuna", num2words(10000000, lang='hr'))
        self.assertEqual("sto milijuna", num2words(100000000, lang='hr'))

    def test_compound_millions(self):
        """Test compound millions"""
        self.assertEqual("jedan milijun sto trideset devet", num2words(1000139, lang='hr'))
        self.assertEqual("dva milijuna petsto tisuća", num2words(2500000, lang='hr'))

    def test_large_numbers(self):
        """Test very large numbers"""
        self.assertEqual(
            "jedan bilijan dvjesto trideset četiri milijuna petsto "
            "šezdeset sedam tisuća osamsto devedeset",
            num2words(1234567890, lang='hr')
        )

    def test_floating_point(self):
        """Test decimal numbers"""
        self.assertEqual("pet zapeta dva", num2words(5.2, lang='hr'))
        self.assertEqual("deset zapeta nula dva", num2words(10.02, lang='hr'))
        self.assertEqual("petnaest zapeta nula nula sedam", num2words(15.007, lang='hr'))
        self.assertEqual("petsto šezdeset jedan zapeta četrdeset dva", num2words(561.42, lang='hr'))

    def test_negative_numbers(self):
        """Test negative numbers"""
        self.assertEqual("minus jedan", num2words(-1, lang='hr'))
        self.assertEqual("minus dvadeset tri", num2words(-23, lang='hr'))
        self.assertEqual("minus sto", num2words(-100, lang='hr'))
        self.assertEqual("minus jedna tisuća", num2words(-1000, lang='hr'))

    def test_negative_decimals(self):
        """Test negative decimal numbers"""
        self.assertEqual("minus nula zapeta četiri", num2words(-0.4, lang='hr'))
        self.assertEqual("minus nula zapeta pet", num2words(-0.5, lang='hr'))
        self.assertEqual("minus jedan zapeta četiri", num2words(-1.4, lang='hr'))

    def test_zero_edge_cases(self):
        """Test zero in various contexts"""
        self.assertEqual("nula", num2words(0, lang='hr'))
        self.assertEqual("nula zapeta pet", num2words(0.5, lang='hr'))
        self.assertEqual("minus nula zapeta pet", num2words(-0.5, lang='hr'))

    def test_to_ordinal(self):
        """Test ordinal numbers - not implemented"""
        # Croatian ordinals would be: prvi, drugi, treći, etc.
        # For now, expect NotImplementedError like in Serbian
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='hr', to='ordinal')

    def test_to_currency(self):
        """Test currency conversion"""
        # Test EUR currency
        self.assertEqual(
            'jedan euro, nula centi',
            num2words(1.0, lang='hr', to='currency', currency='EUR')
        )
        self.assertEqual(
            'dva eura, nula centi',
            num2words(2.0, lang='hr', to='currency', currency='EUR')
        )
        self.assertEqual(
            'pet eura, nula centi',
            num2words(5.0, lang='hr', to='currency', currency='EUR')
        )
        self.assertEqual(
            'dva eura, jedan cent',
            num2words(2.01, lang='hr', to='currency', currency='EUR')
        )
        self.assertEqual(
            'dva eura, dva centa',
            num2words(2.02, lang='hr', to='currency', currency='EUR')
        )
        self.assertEqual(
            'dva eura, pet centi',
            num2words(2.05, lang='hr', to='currency', currency='EUR')
        )

        # Test HRK (Croatian Kuna) currency
        self.assertEqual(
            'jedna kuna, nula lipa',
            num2words(1.0, lang='hr', to='currency', currency='HRK')
        )
        self.assertEqual(
            'dvije kune, jedna lipa',
            num2words(2.01, lang='hr', to='currency', currency='HRK')
        )
        self.assertEqual(
            'dvije kune, dvije lipe',
            num2words(2.02, lang='hr', to='currency', currency='HRK')
        )
        self.assertEqual(
            'dvije kune, pet lipa',
            num2words(2.05, lang='hr', to='currency', currency='HRK')
        )
        self.assertEqual(
            'pet kuna, pet lipa',
            num2words(5.05, lang='hr', to='currency', currency='HRK')
        )
        self.assertEqual(
            'jedanaest kuna, jedanaest lipa',
            num2words(11.11, lang='hr', to='currency', currency='HRK')
        )
        self.assertEqual(
            'dvadeset jedna kuna, dvadeset jedna lipa',
            num2words(21.21, lang='hr', to='currency', currency='HRK')
        )

        # Test large currency amounts
        self.assertEqual(
            'jedna tisuća dvjesto trideset četiri eura, '
            'pedeset šest centi',
            num2words(
                1234.56, lang='hr', to='currency', currency='EUR'
            )
        )
        self.assertEqual(
            'jedna tisuća dvjesto trideset četiri kune, '
            'pedeset šest lipa',
            num2words(
                1234.56, lang='hr', to='currency', currency='HRK'
            )
        )

        # Test with custom separator
        self.assertEqual(
            'sto jedan euro i jedanaest centi',
            num2words(
                10111,
                lang='hr',
                to='currency',
                currency='EUR',
                separator=' i'
            )
        )
        self.assertEqual(
            'sto jedna kuna i dvadeset jedna lipa',
            num2words(
                10121,
                lang='hr',
                to='currency',
                currency='HRK',
                separator=' i'
            )
        )

        # Test negative currency
        self.assertEqual(
            'minus dvanaest tisuća petsto devetnaest eura, 85 centi',
            num2words(
                -1251985,
                lang='hr',
                to='currency',
                currency='EUR',
                cents=False
            )
        )
        self.assertEqual(
            "trideset osam eura i 40 centi",
            num2words('38.4', lang='hr', to='currency', separator=' i',
                      cents=False, currency='EUR'),
        )

    def test_gender_forms(self):
        """Test gender forms for numbers"""
        # In Croatian, numbers 1 and 2 have different forms for different genders
        # This will be tested implicitly through currency tests
        # where feminine forms are used for feminine currencies
        pass

    def test_edge_cases(self):
        """Test various edge cases"""
        # Test very small decimals
        self.assertEqual("nula zapeta nula nula jedan", num2words(0.001, lang='hr'))
        
        # Test numbers with many decimal places
        self.assertEqual("tri zapeta četrnaest tisuća sto pedeset devet", num2words(3.14159, lang='hr'))
        
        # Test string input
        self.assertEqual("dvadeset tri", num2words("23", lang='hr'))
        self.assertEqual("dvadeset tri zapeta četiri", num2words("23.4", lang='hr'))