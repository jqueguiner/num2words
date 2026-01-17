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


class Num2WordsBGTest(TestCase):
    def test_cardinal_basic(self):
        # Test basic numbers 0-19
        self.assertEqual(num2words(0, lang='bg'), "нула")
        self.assertEqual(num2words(1, lang='bg'), "един")
        self.assertEqual(num2words(2, lang='bg'), "два")
        self.assertEqual(num2words(3, lang='bg'), "три")
        self.assertEqual(num2words(4, lang='bg'), "четири")
        self.assertEqual(num2words(5, lang='bg'), "пет")
        self.assertEqual(num2words(6, lang='bg'), "шест")
        self.assertEqual(num2words(7, lang='bg'), "седем")
        self.assertEqual(num2words(8, lang='bg'), "осем")
        self.assertEqual(num2words(9, lang='bg'), "девет")
        self.assertEqual(num2words(10, lang='bg'), "десет")
        self.assertEqual(num2words(11, lang='bg'), "единадесет")
        self.assertEqual(num2words(12, lang='bg'), "дванадесет")
        self.assertEqual(num2words(13, lang='bg'), "тринадесет")
        self.assertEqual(num2words(14, lang='bg'), "четиринадесет")
        self.assertEqual(num2words(15, lang='bg'), "петнадесет")
        self.assertEqual(num2words(16, lang='bg'), "шестнадесет")
        self.assertEqual(num2words(17, lang='bg'), "седемнадесет")
        self.assertEqual(num2words(18, lang='bg'), "осемнадесет")
        self.assertEqual(num2words(19, lang='bg'), "деветнадесет")

    def test_cardinal_tens(self):
        # Test tens 20-90
        self.assertEqual(num2words(20, lang='bg'), "двадесет")
        self.assertEqual(num2words(21, lang='bg'), "двадесет и един")
        self.assertEqual(num2words(25, lang='bg'), "двадесет и пет")
        self.assertEqual(num2words(30, lang='bg'), "тридесет")
        self.assertEqual(num2words(35, lang='bg'), "тридесет и пет")
        self.assertEqual(num2words(40, lang='bg'), "четиридесет")
        self.assertEqual(num2words(50, lang='bg'), "петдесет")
        self.assertEqual(num2words(60, lang='bg'), "шестдесет")
        self.assertEqual(num2words(70, lang='bg'), "седемдесет")
        self.assertEqual(num2words(80, lang='bg'), "осемдесет")
        self.assertEqual(num2words(90, lang='bg'), "деветдесет")
        self.assertEqual(num2words(99, lang='bg'), "деветдесет и девет")

    def test_cardinal_hundreds(self):
        # Test hundreds 100-900
        self.assertEqual(num2words(100, lang='bg'), "сто")
        self.assertEqual(num2words(101, lang='bg'), "сто и един")
        self.assertEqual(num2words(110, lang='bg'), "сто и десет")
        self.assertEqual(num2words(115, lang='bg'), "сто и петнадесет")
        self.assertEqual(num2words(123, lang='bg'), "сто двадесет и три")
        self.assertEqual(num2words(200, lang='bg'), "двеста")
        self.assertEqual(num2words(300, lang='bg'), "триста")
        self.assertEqual(num2words(400, lang='bg'), "четиристотин")
        self.assertEqual(num2words(500, lang='bg'), "петстотин")
        self.assertEqual(num2words(600, lang='bg'), "шестстотин")
        self.assertEqual(num2words(700, lang='bg'), "седемстотин")
        self.assertEqual(num2words(800, lang='bg'), "осемстотин")
        self.assertEqual(num2words(900, lang='bg'), "деветстотин")
        self.assertEqual(num2words(999, lang='bg'), "деветстотин деветдесет и девет")

    def test_cardinal_thousands(self):
        # Test thousands
        self.assertEqual(num2words(1000, lang='bg'), "хиляда")
        self.assertEqual(num2words(1001, lang='bg'), "хиляда и един")
        self.assertEqual(num2words(1234, lang='bg'), "хиляда двеста тридесет и четири")
        self.assertEqual(num2words(2000, lang='bg'), "две хиляди")
        self.assertEqual(num2words(2012, lang='bg'), "две хиляди и дванадесет")
        self.assertEqual(num2words(5000, lang='bg'), "пет хиляди")
        self.assertEqual(num2words(10000, lang='bg'), "десет хиляди")
        self.assertEqual(num2words(12345, lang='bg'), "дванадесет хиляди триста четиридесет и пет")
        self.assertEqual(num2words(100000, lang='bg'), "сто хиляди")
        self.assertEqual(num2words(999999, lang='bg'), "деветстотин деветдесет и девет хиляди деветстотин деветдесет и девет")

    def test_cardinal_millions(self):
        # Test millions
        self.assertEqual(num2words(1000000, lang='bg'), "един милион")
        self.assertEqual(num2words(2000000, lang='bg'), "два милиона")
        self.assertEqual(num2words(5000000, lang='bg'), "пет милиона")
        self.assertEqual(num2words(1234567, lang='bg'), "един милион двеста тридесет и четири хиляди петстотин шестдесет и седем")

    def test_cardinal_large_numbers(self):
        # Test large numbers 
        self.assertEqual(
            num2words(1234567890, lang='bg'),
            "един милиард двеста тридесет и четири милиона петстотин шестдесет и седем хиляди осемстотин деветдесет"
        )

    def test_negative_numbers(self):
        # Test negative numbers
        self.assertEqual(num2words(-1, lang='bg'), "минус един")
        self.assertEqual(num2words(-42, lang='bg'), "минус четиридесет и два")
        self.assertEqual(num2words(-100, lang='bg'), "минус сто")
        self.assertEqual(num2words(-1234, lang='bg'), "минус хиляда двеста тридесет и четири")

    def test_decimal_numbers(self):
        # Test decimal numbers
        self.assertEqual(num2words(10.02, lang='bg'), "десет цяло нула две")
        self.assertEqual(num2words(15.007, lang='bg'), "петнадесет цяло нула нула седем")
        self.assertEqual(num2words(123.45, lang='bg'), "сто двадесет и три цяло четиридесет и пет")
        self.assertEqual(num2words(123.50, lang='bg'), "сто двадесет и три цяло пет")

    def test_negative_decimals(self):
        # Test negative decimal numbers including edge cases
        self.assertEqual(num2words(-0.4, lang="bg"), "минус нула цяло четири")
        self.assertEqual(num2words(-0.5, lang="bg"), "минус нула цяло пет")
        self.assertEqual(num2words(-1.4, lang="bg"), "минус един цяло четири")
        self.assertEqual(num2words(-12.5, lang="bg"), "минус дванадесет цяло пет")

    def test_to_ordinal(self):
        # Ordinal numbers are not implemented yet - should raise NotImplementedError
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='bg', to='ordinal')

    def test_currency(self):
        # Test currency conversion
        self.assertEqual(
            num2words(10.0, lang='bg', to='currency', currency='BGN'),
            "десет лева, нула стотинки")
        self.assertEqual(
            num2words(1.0, lang='bg', to='currency', currency='BGN'),
            "един лев, нула стотинки")
        self.assertEqual(
            num2words(1234.56, lang='bg', to='currency', currency='BGN'),
            "хиляда двеста тридесет и четири лева, петдесет и шест стотинки")
        self.assertEqual(
            num2words(2.0, lang='bg', to='currency', currency='BGN'),
            "два лева, нула стотинки")
        self.assertEqual(
            num2words(5.0, lang='bg', to='currency', currency='BGN'),
            "пет лева, нула стотинки")

    def test_currency_with_separator(self):
        # Test currency with custom separator
        self.assertEqual(
            num2words(101.11, lang='bg', to='currency', currency='BGN',
                      separator=' и'),
            "сто и един лева и единадесет стотинки")

    def test_currency_euros(self):
        # Test EUR currency
        self.assertEqual(
            num2words(10.0, lang='bg', to='currency', currency='EUR'),
            "десет евро, нула цента")
        self.assertEqual(
            num2words(1.0, lang='bg', to='currency', currency='EUR'),
            "едно евро, нула цента")
        self.assertEqual(
            num2words(2.50, lang='bg', to='currency', currency='EUR'),
            "две евро, петдесет цента")

    def test_currency_without_cents(self):
        # Test currency without verbose cents
        self.assertEqual(
            num2words(19.50, lang='bg', to='currency', currency='BGN', cents=False),
            "деветнадесет лева, 50 стотинки"
        )

    def test_zero_combinations(self):
        # Test special zero combinations
        self.assertEqual(num2words(1000, lang='bg'), "хиляда")
        self.assertEqual(num2words(1000000, lang='bg'), "един милион")
        self.assertEqual(num2words(1001000, lang='bg'), "един милион и хиляда")
        self.assertEqual(num2words(1000001, lang='bg'), "един милион и един")

    def test_edge_cases(self):
        # Test various edge cases
        self.assertEqual(num2words(101, lang='bg'), "сто и един")
        self.assertEqual(num2words(111, lang='bg'), "сто и единадесет")
        self.assertEqual(num2words(1100, lang='bg'), "хиляда и сто")
        self.assertEqual(num2words(1111, lang='bg'), "хиляда сто и единадесет")