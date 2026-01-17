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


class Num2WordsAFTest(TestCase):
    def test_numbers_0_to_20(self):
        self.assertEqual(num2words(0, lang='af'), "nul")
        self.assertEqual(num2words(1, lang='af'), "een")
        self.assertEqual(num2words(2, lang='af'), "twee")
        self.assertEqual(num2words(3, lang='af'), "drie")
        self.assertEqual(num2words(4, lang='af'), "vier")
        self.assertEqual(num2words(5, lang='af'), "vyf")
        self.assertEqual(num2words(6, lang='af'), "ses")
        self.assertEqual(num2words(7, lang='af'), "sewe")
        self.assertEqual(num2words(8, lang='af'), "agt")
        self.assertEqual(num2words(9, lang='af'), "nege")
        self.assertEqual(num2words(10, lang='af'), "tien")
        self.assertEqual(num2words(11, lang='af'), "elf")
        self.assertEqual(num2words(12, lang='af'), "twaalf")
        self.assertEqual(num2words(13, lang='af'), "dertien")
        self.assertEqual(num2words(14, lang='af'), "veertien")
        self.assertEqual(num2words(15, lang='af'), "vyftien")
        self.assertEqual(num2words(16, lang='af'), "sestien")
        self.assertEqual(num2words(17, lang='af'), "sewentien")
        self.assertEqual(num2words(18, lang='af'), "agtien")
        self.assertEqual(num2words(19, lang='af'), "negentien")
        self.assertEqual(num2words(20, lang='af'), "twintig")

    def test_tens(self):
        self.assertEqual(num2words(30, lang='af'), "dertig")
        self.assertEqual(num2words(40, lang='af'), "veertig")
        self.assertEqual(num2words(50, lang='af'), "vyftig")
        self.assertEqual(num2words(60, lang='af'), "sestig")
        self.assertEqual(num2words(70, lang='af'), "sewentig")
        self.assertEqual(num2words(80, lang='af'), "tagtig")
        self.assertEqual(num2words(90, lang='af'), "negentig")

    def test_compound_numbers(self):
        self.assertEqual(num2words(21, lang='af'), "een-en-twintig")
        self.assertEqual(num2words(35, lang='af'), "vyf-en-dertig")
        self.assertEqual(num2words(47, lang='af'), "sewe-en-veertig")
        self.assertEqual(num2words(59, lang='af'), "nege-en-vyftig")
        self.assertEqual(num2words(64, lang='af'), "vier-en-sestig")
        self.assertEqual(num2words(78, lang='af'), "agt-en-sewentig")
        self.assertEqual(num2words(82, lang='af'), "twee-en-tagtig")
        self.assertEqual(num2words(99, lang='af'), "nege-en-negentig")

    def test_hundreds(self):
        self.assertEqual(num2words(100, lang='af'), "eenhonderd")
        self.assertEqual(num2words(200, lang='af'), "tweehonderd")
        self.assertEqual(num2words(300, lang='af'), "driehonderd")
        self.assertEqual(num2words(400, lang='af'), "vierhonderd")
        self.assertEqual(num2words(500, lang='af'), "vyfhonderd")
        self.assertEqual(num2words(600, lang='af'), "seshonderd")
        self.assertEqual(num2words(700, lang='af'), "sewehonderd")
        self.assertEqual(num2words(800, lang='af'), "agthonderd")
        self.assertEqual(num2words(900, lang='af'), "negehonderd")

    def test_hundreds_with_tens_and_units(self):
        self.assertEqual(num2words(101, lang='af'), "eenhonderd en een")
        self.assertEqual(num2words(110, lang='af'), "eenhonderd en tien")
        self.assertEqual(num2words(123, lang='af'), "eenhonderd drie-en-twintig")
        self.assertEqual(num2words(245, lang='af'), "tweehonderd vyf-en-veertig")
        self.assertEqual(num2words(367, lang='af'), "driehonderd sewe-en-sestig")
        self.assertEqual(num2words(489, lang='af'), "vierhonderd nege-en-tagtig")
        self.assertEqual(num2words(555, lang='af'), "vyfhonderd vyf-en-vyftig")
        self.assertEqual(num2words(678, lang='af'), "seshonderd agt-en-sewentig")
        self.assertEqual(num2words(799, lang='af'), "sewehonderd nege-en-negentig")
        self.assertEqual(num2words(888, lang='af'), "agthonderd agt-en-tagtig")
        self.assertEqual(num2words(999, lang='af'), "negehonderd nege-en-negentig")

    def test_thousands(self):
        self.assertEqual(num2words(1000, lang='af'), "eenduisend")
        self.assertEqual(num2words(2000, lang='af'), "tweeduisend")
        self.assertEqual(num2words(3000, lang='af'), "drieduisend")
        self.assertEqual(num2words(4000, lang='af'), "vierduisend")
        self.assertEqual(num2words(5000, lang='af'), "vyfduisend")
        self.assertEqual(num2words(10000, lang='af'), "tienduisend")
        self.assertEqual(num2words(20000, lang='af'), "twintigduisend")
        self.assertEqual(num2words(50000, lang='af'), "vyftigduisend")
        self.assertEqual(num2words(100000, lang='af'), "eenhonderdduisend")
        self.assertEqual(num2words(500000, lang='af'), "vyfhonderdduisend")

    def test_thousands_complex(self):
        self.assertEqual(num2words(1001, lang='af'), "eenduisend en een")
        self.assertEqual(num2words(1010, lang='af'), "eenduisend en tien")
        self.assertEqual(num2words(1100, lang='af'), "eenduisend eenhonderd")
        self.assertEqual(num2words(1234, lang='af'), "eenduisend tweehonderd vier-en-dertig")
        self.assertEqual(num2words(2345, lang='af'), "tweeduisend driehonderd vyf-en-veertig")
        self.assertEqual(num2words(12345, lang='af'), "twaalfduisend driehonderd vyf-en-veertig")
        self.assertEqual(num2words(123456, lang='af'), "eenhonderd drie-en-twintigduisend vierhonderd ses-en-vyftig")
        self.assertEqual(num2words(999999, lang='af'), "negehonderd nege-en-negentigduisend negehonderd nege-en-negentig")

    def test_millions(self):
        self.assertEqual(num2words(1000000, lang='af'), "een miljoen")
        self.assertEqual(num2words(2000000, lang='af'), "twee miljoen")
        self.assertEqual(num2words(3000000, lang='af'), "drie miljoen")
        self.assertEqual(num2words(5000000, lang='af'), "vyf miljoen")
        self.assertEqual(num2words(10000000, lang='af'), "tien miljoen")
        self.assertEqual(num2words(100000000, lang='af'), "eenhonderd miljoen")

    def test_millions_complex(self):
        self.assertEqual(num2words(1000001, lang='af'), "een miljoen en een")
        self.assertEqual(num2words(1234567, lang='af'), "een miljoen tweehonderd vier-en-dertigduisend vyfhonderd sewe-en-sestig")
        self.assertEqual(num2words(12345678, lang='af'), "twaalf miljoen driehonderd vyf-en-veertigduisend seshonderd agt-en-sewentig")
        self.assertEqual(num2words(999999999, lang='af'), "negehonderd nege-en-negentig miljoen negehonderd nege-en-negentigduisend negehonderd nege-en-negentig")

    def test_billions(self):
        self.assertEqual(num2words(1000000000, lang='af'), "een miljard")
        self.assertEqual(num2words(2000000000, lang='af'), "twee miljard")
        self.assertEqual(num2words(5000000000, lang='af'), "vyf miljard")

    def test_decimal_numbers(self):
        self.assertEqual(num2words(0.5, lang='af'), "nul komma vyf")
        self.assertEqual(num2words(1.5, lang='af'), "een komma vyf")
        self.assertEqual(num2words(3.14, lang='af'), "drie komma een vier")
        self.assertEqual(num2words(12.345, lang='af'), "twaalf komma drie vier vyf")
        self.assertEqual(num2words(99.99, lang='af'), "nege-en-negentig komma nege nege")

    def test_negative_numbers(self):
        self.assertEqual(num2words(-1, lang='af'), "minus een")
        self.assertEqual(num2words(-10, lang='af'), "minus tien")
        self.assertEqual(num2words(-23, lang='af'), "minus drie-en-twintig")
        self.assertEqual(num2words(-100, lang='af'), "minus eenhonderd")
        self.assertEqual(num2words(-1000, lang='af'), "minus eenduisend")
        self.assertEqual(num2words(-1234, lang='af'), "minus eenduisend tweehonderd vier-en-dertig")

    def test_ordinal_numbers(self):
        self.assertEqual(num2words(1, ordinal=True, lang='af'), "eerste")
        self.assertEqual(num2words(2, ordinal=True, lang='af'), "tweede")
        self.assertEqual(num2words(3, ordinal=True, lang='af'), "derde")
        self.assertEqual(num2words(4, ordinal=True, lang='af'), "vierde")
        self.assertEqual(num2words(5, ordinal=True, lang='af'), "vyfde")
        self.assertEqual(num2words(6, ordinal=True, lang='af'), "sesde")
        self.assertEqual(num2words(7, ordinal=True, lang='af'), "sewende")
        self.assertEqual(num2words(8, ordinal=True, lang='af'), "agste")
        self.assertEqual(num2words(9, ordinal=True, lang='af'), "negende")
        self.assertEqual(num2words(10, ordinal=True, lang='af'), "tiende")
        self.assertEqual(num2words(11, ordinal=True, lang='af'), "elfde")
        self.assertEqual(num2words(12, ordinal=True, lang='af'), "twaalfde")
        self.assertEqual(num2words(13, ordinal=True, lang='af'), "dertiende")
        self.assertEqual(num2words(14, ordinal=True, lang='af'), "veertiende")
        self.assertEqual(num2words(15, ordinal=True, lang='af'), "vyftiende")
        self.assertEqual(num2words(20, ordinal=True, lang='af'), "twintigste")
        self.assertEqual(num2words(21, ordinal=True, lang='af'), "een-en-twintigste")
        self.assertEqual(num2words(30, ordinal=True, lang='af'), "dertigste")
        self.assertEqual(num2words(100, ordinal=True, lang='af'), "eenhonderdste")
        self.assertEqual(num2words(1000, ordinal=True, lang='af'), "eenduisendste")
        self.assertEqual(num2words(1000000, ordinal=True, lang='af'), "een miljoenste")

    def test_ordinal_for_negative_numbers(self):
        self.assertRaises(TypeError, num2words, -12, ordinal=True, lang='af')

    def test_ordinal_for_floating_numbers(self):
        self.assertRaises(TypeError, num2words, 2.453, ordinal=True, lang='af')

    def test_to_currency_zar(self):
        self.assertEqual(
            num2words('38.4', lang='af', to='currency', separator=' en',
                      cents=False, currency='ZAR'),
            "agt-en-dertig rand en 40 sent"
        )
        self.assertEqual(
            num2words('0', lang='af', to='currency', separator=' en',
                      cents=False, currency='ZAR'),
            "nul rand"
        )
        self.assertEqual(
            num2words('1.01', lang='af', to='currency', separator=' en',
                      cents=False, currency='ZAR'),
            "een rand en 1 sent"
        )
        self.assertEqual(
            num2words('4778.00', lang='af', to='currency', separator=' en',
                      cents=False, currency='ZAR'),
            "vierduisend sewehonderd agt-en-sewentig rand"
        )
        self.assertEqual(
            num2words('4778.15', lang='af', to='currency', separator=' en',
                      cents=True, currency='ZAR'),
            "vierduisend sewehonderd agt-en-sewentig rand en vyftien sent"
        )

    def test_to_currency_eur(self):
        self.assertEqual(
            num2words('123.45', lang='af', to='currency', separator=' en',
                      cents=False, currency='EUR'),
            "eenhonderd drie-en-twintig euro en 45 sent"
        )

    def test_to_currency_usd(self):
        self.assertEqual(
            num2words('250.00', lang='af', to='currency', separator=' en',
                      cents=False, currency='USD'),
            "tweehonderd vyftig dollar"
        )