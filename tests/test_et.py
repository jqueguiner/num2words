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


class Num2WordsETTest(TestCase):
    def test_to_cardinal(self):
        # Test basic numbers 0-10
        self.assertEqual(num2words(0, lang='et'), 'null')
        self.assertEqual(num2words(1, lang='et'), 'üks')
        self.assertEqual(num2words(2, lang='et'), 'kaks')
        self.assertEqual(num2words(3, lang='et'), 'kolm')
        self.assertEqual(num2words(4, lang='et'), 'neli')
        self.assertEqual(num2words(5, lang='et'), 'viis')
        self.assertEqual(num2words(6, lang='et'), 'kuus')
        self.assertEqual(num2words(7, lang='et'), 'seitse')
        self.assertEqual(num2words(8, lang='et'), 'kaheksa')
        self.assertEqual(num2words(9, lang='et'), 'üheksa')
        self.assertEqual(num2words(10, lang='et'), 'kümme')

        # Test teens 11-19
        self.assertEqual(num2words(11, lang='et'), 'üksteist')
        self.assertEqual(num2words(12, lang='et'), 'kaksteist')
        self.assertEqual(num2words(13, lang='et'), 'kolmteist')
        self.assertEqual(num2words(14, lang='et'), 'neliteist')
        self.assertEqual(num2words(15, lang='et'), 'viisteist')
        self.assertEqual(num2words(16, lang='et'), 'kuusteist')
        self.assertEqual(num2words(17, lang='et'), 'seitseteist')
        self.assertEqual(num2words(18, lang='et'), 'kaheksateist')
        self.assertEqual(num2words(19, lang='et'), 'üheksateist')

        # Test tens 20-90
        self.assertEqual(num2words(20, lang='et'), 'kakskümmend')
        self.assertEqual(num2words(30, lang='et'), 'kolmkümmend')
        self.assertEqual(num2words(40, lang='et'), 'nelikümmend')
        self.assertEqual(num2words(50, lang='et'), 'viiskümmend')
        self.assertEqual(num2words(60, lang='et'), 'kuuskümmend')
        self.assertEqual(num2words(70, lang='et'), 'seitsekümmend')
        self.assertEqual(num2words(80, lang='et'), 'kaheksakümmend')
        self.assertEqual(num2words(90, lang='et'), 'üheksakümmend')

        # Test compound numbers 21-99
        self.assertEqual(num2words(21, lang='et'), 'kakskümmend üks')
        self.assertEqual(num2words(35, lang='et'), 'kolmkümmend viis')
        self.assertEqual(num2words(47, lang='et'), 'nelikümmend seitse')
        self.assertEqual(num2words(58, lang='et'), 'viiskümmend kaheksa')
        self.assertEqual(num2words(69, lang='et'), 'kuuskümmend üheksa')
        self.assertEqual(num2words(73, lang='et'), 'seitsekümmend kolm')
        self.assertEqual(num2words(84, lang='et'), 'kaheksakümmend neli')
        self.assertEqual(num2words(96, lang='et'), 'üheksakümmend kuus')
        self.assertEqual(num2words(99, lang='et'), 'üheksakümmend üheksa')

        # Test hundreds
        self.assertEqual(num2words(100, lang='et'), 'sada')
        self.assertEqual(num2words(101, lang='et'), 'sada üks')
        self.assertEqual(num2words(110, lang='et'), 'sada kümme')
        self.assertEqual(num2words(115, lang='et'), 'sada viisteist')
        self.assertEqual(num2words(123, lang='et'), 'sada kakskümmend kolm')
        self.assertEqual(num2words(200, lang='et'), 'kakssada')
        self.assertEqual(num2words(300, lang='et'), 'kolmsada')
        self.assertEqual(num2words(400, lang='et'), 'nelisada')
        self.assertEqual(num2words(500, lang='et'), 'viissada')
        self.assertEqual(num2words(600, lang='et'), 'kuussada')
        self.assertEqual(num2words(700, lang='et'), 'seitsesada')
        self.assertEqual(num2words(800, lang='et'), 'kaheksasada')
        self.assertEqual(num2words(900, lang='et'), 'üheksasada')
        self.assertEqual(num2words(999, lang='et'), 'üheksasada üheksakümmend üheksa')

        # Test thousands
        self.assertEqual(num2words(1000, lang='et'), 'tuhat')
        self.assertEqual(num2words(1001, lang='et'), 'tuhat üks')
        self.assertEqual(num2words(1100, lang='et'), 'tuhat sada')
        self.assertEqual(num2words(1234, lang='et'), 'tuhat kakssada kolmkümmend neli')
        self.assertEqual(num2words(2000, lang='et'), 'kaks tuhat')
        self.assertEqual(num2words(2012, lang='et'), 'kaks tuhat kaksteist')
        self.assertEqual(num2words(5000, lang='et'), 'viis tuhat')
        self.assertEqual(num2words(10000, lang='et'), 'kümme tuhat')
        self.assertEqual(num2words(11000, lang='et'), 'üksteist tuhat')
        self.assertEqual(num2words(21000, lang='et'), 'kakskümmend üks tuhat')
        self.assertEqual(num2words(100000, lang='et'), 'sada tuhat')
        self.assertEqual(num2words(999000, lang='et'), 'üheksasada üheksakümmend üheksa tuhat')

        # Test millions
        self.assertEqual(num2words(1000000, lang='et'), 'miljon')
        self.assertEqual(num2words(2000000, lang='et'), 'kaks miljonit')
        self.assertEqual(num2words(1000139, lang='et'), 'miljon sada kolmkümmend üheksa')
        self.assertEqual(num2words(1234567, lang='et'), 'miljon kakssada kolmkümmend neli tuhat viissada kuuskümmend seitse')

        # Test large numbers
        self.assertEqual(num2words(1000000000, lang='et'), 'miljard')
        self.assertEqual(num2words(2000000000, lang='et'), 'kaks miljardit')
        self.assertEqual(num2words(1000000000000, lang='et'), 'biljon')

        # Test complex large number
        self.assertEqual(
            num2words(1234567890, lang='et'),
            'miljard kakssada kolmkümmend neli miljonit viissada kuuskümmend seitse tuhat kaheksasada üheksakümmend'
        )

    def test_negative_numbers(self):
        # Test negative numbers
        self.assertEqual(num2words(-1, lang='et'), 'miinus üks')
        self.assertEqual(num2words(-5, lang='et'), 'miinus viis')
        self.assertEqual(num2words(-15, lang='et'), 'miinus viisteist')
        self.assertEqual(num2words(-123, lang='et'), 'miinus sada kakskümmend kolm')
        self.assertEqual(num2words(-5000, lang='et'), 'miinus viis tuhat')

    def test_decimals(self):
        # Test decimal numbers
        self.assertEqual(num2words(5.2, lang='et'), 'viis koma kaks')
        self.assertEqual(num2words(10.02, lang='et'), 'kümme koma null kaks')
        self.assertEqual(num2words(15.007, lang='et'), 'viisteist koma null null seitse')
        self.assertEqual(num2words(123.45, lang='et'), 'sada kakskümmend kolm koma nelikümmend viis')
        self.assertEqual(num2words(561.42, lang='et'), 'viissada kuuskümmend üks koma nelikümmend kaks')

    def test_negative_decimals(self):
        # Test negative decimals including -0.4
        self.assertEqual(num2words(-0.4, lang='et'), 'miinus null koma neli')
        self.assertEqual(num2words(-0.5, lang='et'), 'miinus null koma viis')
        self.assertEqual(num2words(-1.4, lang='et'), 'miinus üks koma neli')
        self.assertEqual(num2words(-5000.22, lang='et'), 'miinus viis tuhat koma kakskümmend kaks')

    def test_to_ordinal(self):
        # Estonian ordinals are not implemented yet, should raise NotImplementedError
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='et', to='ordinal')

    def test_to_currency(self):
        # Test EUR currency
        self.assertEqual(
            num2words(1.0, lang='et', to='currency', currency='EUR'),
            'üks euro, null senti'
        )
        self.assertEqual(
            num2words(2.0, lang='et', to='currency', currency='EUR'),
            'kaks eurot, null senti'
        )
        self.assertEqual(
            num2words(5.0, lang='et', to='currency', currency='EUR'),
            'viis eurot, null senti'
        )
        self.assertEqual(
            num2words(1.50, lang='et', to='currency', currency='EUR'),
            'üks euro, viiskümmend senti'
        )
        self.assertEqual(
            num2words(123.45, lang='et', to='currency', currency='EUR'),
            'sada kakskümmend kolm eurot, nelikümmend viis senti'
        )

        # Test USD currency
        self.assertEqual(
            num2words(1.0, lang='et', to='currency', currency='USD'),
            'üks dollar, null senti'
        )
        self.assertEqual(
            num2words(5.25, lang='et', to='currency', currency='USD'),
            'viis dollarit, kakskümmend viis senti'
        )

        # Test EEK (historical Estonian kroon)
        self.assertEqual(
            num2words(1.0, lang='et', to='currency', currency='EEK'),
            'üks kroon, null senti'
        )
        self.assertEqual(
            num2words(10.5, lang='et', to='currency', currency='EEK'),
            'kümme krooni, viiskümmend senti'
        )

        # Test with custom separator
        self.assertEqual(
            num2words(10.25, lang='et', to='currency', separator=' ja',
                      currency='EUR'),
            'kümme eurot ja kakskümmend viis senti'
        )

        # Test cents=False option
        self.assertEqual(
            num2words(123.45, lang='et', to='currency', cents=False,
                      currency='EUR'),
            'sada kakskümmend kolm eurot, 45 senti'
        )

        # Test negative currency
        self.assertEqual(
            num2words(-25.50, lang='et', to='currency', currency='EUR'),
            'miinus kakskümmend viis eurot, viiskümmend senti'
        )

    def test_edge_cases(self):
        # Test edge cases and special numbers
        self.assertEqual(num2words(0, lang='et'), 'null')
        
        # Test very large numbers
        self.assertEqual(
            num2words(999999999999, lang='et'),
            'üheksasada üheksakümmend üheksa miljardit üheksasada üheksakümmend üheksa miljonit üheksasada üheksakümmend üheksa tuhat üheksasada üheksakümmend üheksa'
        )

    def test_currency_pluralization(self):
        # Test that currency forms are properly pluralized
        # Note: Integer values represent cents, floats represent main currency units
        
        # Test cents (integer inputs)
        self.assertEqual(
            num2words(1, lang='et', to='currency', currency='EUR'),
            'null eurot, üks sent'
        )
        self.assertEqual(
            num2words(5, lang='et', to='currency', currency='EUR'),
            'null eurot, viis senti'
        )
        
        # Test main currency units (float inputs)  
        self.assertEqual(
            num2words(1.0, lang='et', to='currency', currency='EUR'),
            'üks euro, null senti'
        )
        self.assertEqual(
            num2words(2.0, lang='et', to='currency', currency='EUR'),
            'kaks eurot, null senti'
        )
        self.assertEqual(
            num2words(5.0, lang='et', to='currency', currency='USD'),
            'viis dollarit, null senti'
        )
        
        # Test partitive plural (11-19)
        self.assertEqual(
            num2words(11.0, lang='et', to='currency', currency='EUR'),
            'üksteist eurot, null senti'
        )
        self.assertEqual(
            num2words(15.0, lang='et', to='currency', currency='USD'),
            'viisteist dollarit, null senti'
        )