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

from .base import Num2Word_Base
from .currency import parse_currency_parts


class Num2Word_BG(Num2Word_Base):
    CURRENCY_FORMS = {
        'BGN': (
            ('лев', 'лева'), ('стотинка', 'стотинки')
        ),
        'EUR': (
            ('евро', 'евро'), ('цент', 'цента')
        ),
        'USD': (
            ('долар', 'долара'), ('цент', 'цента')
        ),
        'GBP': (
            ('паунд', 'паунда'), ('пени', 'пенса')
        ),
    }

    def __init__(self):
        super(Num2Word_BG, self).__init__()
        
        self.ones = {
            0: 'нула',
            1: 'едно',
            2: 'две',
            3: 'три',
            4: 'четири',
            5: 'пет',
            6: 'шест',
            7: 'седем',
            8: 'осем',
            9: 'девет'
        }
        
        self.ones_masculine = {
            1: 'един',
            2: 'два'
        }
        
        self.ones_feminine = {
            1: 'една',
            2: 'две'
        }
        
        self.tens = {
            10: 'десет',
            11: 'единадесет',
            12: 'дванадесет',
            13: 'тринадесет',
            14: 'четиринадесет',
            15: 'петнадесет',
            16: 'шестнадесет',
            17: 'седемнадесет',
            18: 'осемнадесет',
            19: 'деветнадесет',
            20: 'двадесет',
            30: 'тридесет',
            40: 'четиридесет',
            50: 'петдесет',
            60: 'шестдесет',
            70: 'седемдесет',
            80: 'осемдесет',
            90: 'деветдесет'
        }
        
        self.scale = {
            100: ('сто', 'ста'),
            1000: ('хиляда', 'хиляди'),
            1000000: ('милион', 'милиона'),
            1000000000: ('милиард', 'милиарда'),
            1000000000000: ('трилион', 'трилиона')
        }
        
        self.ordinals = {
            1: 'първи',
            2: 'втори',
            3: 'трети',
            4: 'четвърти',
            5: 'пети',
            6: 'шести',
            7: 'седми',
            8: 'осми',
            9: 'девети',
            10: 'десети',
            11: 'единадесети',
            12: 'дванадесети',
            13: 'тринадесети',
            14: 'четиринадесети',
            15: 'петнадесети',
            16: 'шестнадесети',
            17: 'седемнадесети',
            18: 'осемнадесети',
            19: 'деветнадесети',
            20: 'двадесети',
            30: 'тридесети',
            40: 'четиридесети',
            50: 'петдесети',
            60: 'шестдесети',
            70: 'седемдесети',
            80: 'осемдесети',
            90: 'деветдесети',
            100: 'стотен',
            1000: 'хиляден'
        }
        
        self.negword = "минус "
        self.pointword = "точка"

    def _setup(self):
        super(Num2Word_BG, self)._setup()

    def _int_to_word(self, n, masculine=False, feminine=False):
        """
        Converts a number to words in Bulgarian.
        Args:
            n: integer to convert
            masculine: whether to use masculine form for ones
            feminine: whether to use feminine form for ones
        """
        if n == 0:
            return self.ones[0]
        
        parts = []
        
        # Handle billions
        if n >= 1000000000:
            billions = n // 1000000000
            if billions == 1:
                parts.append('един милиард')
            elif billions == 2:
                parts.append('два милиарда')
            else:
                parts.append(self._int_to_word(billions) + ' милиарда')
            n %= 1000000000
        
        # Handle millions
        if n >= 1000000:
            millions = n // 1000000
            if millions == 1:
                parts.append('един милион')
            elif millions == 2:
                parts.append('два милиона')
            else:
                parts.append(self._int_to_word(millions) + ' милиона')
            n %= 1000000
        
        # Handle thousands
        if n >= 1000:
            thousands = n // 1000
            if thousands == 1:
                parts.append('хиляда')
            elif thousands == 2:
                parts.append('две хиляди')
            else:
                parts.append(self._int_to_word(thousands) + ' хиляди')
            n %= 1000
        
        # Handle hundreds
        if n >= 100:
            hundreds = n // 100
            if hundreds == 1:
                parts.append('сто')
            elif hundreds == 2:
                parts.append('двеста')
            elif hundreds == 3:
                parts.append('триста')
            else:
                parts.append(self.ones[hundreds] + 'стотин')
            n %= 100
        
        # Handle tens and ones
        if n >= 20:
            tens = (n // 10) * 10
            parts.append(self.tens[tens])
            n %= 10
            if n > 0:
                parts.append('и')
                if feminine and n in self.ones_feminine:
                    parts.append(self.ones_feminine[n])
                elif masculine and n in self.ones_masculine:
                    parts.append(self.ones_masculine[n])
                else:
                    parts.append(self.ones[n])
        elif n >= 10:
            parts.append(self.tens[n])
        elif n > 0:
            if feminine and n in self.ones_feminine:
                parts.append(self.ones_feminine[n])
            elif masculine and n in self.ones_masculine:
                parts.append(self.ones_masculine[n])
            else:
                parts.append(self.ones[n])
        
        return ' '.join(parts)

    def _int_to_cardinal(self, n):
        if n == 0:
            return self.ones[0]
        
        if n < 0:
            return self.negword + self._int_to_word(-n)
        
        return self._int_to_word(n, masculine=True)

    def _int_to_ordinal(self, n):
        if n in self.ordinals:
            return self.ordinals[n]
        
        # For complex numbers, form ordinal by adding -ти/-ен to cardinal
        cardinal = self._int_to_cardinal(n)
        
        # Handle different endings
        if cardinal.endswith('един'):
            return cardinal[:-4] + 'първи'
        elif cardinal.endswith('два'):
            return cardinal[:-3] + 'втори'
        elif cardinal.endswith('три'):
            return cardinal[:-3] + 'трети'
        elif cardinal.endswith('т'):
            return cardinal + 'и'
        else:
            return cardinal + 'ти'

    def to_cardinal(self, n):
        try:
            if isinstance(n, str):
                n = int(n)
            
            if n < 0:
                return self.negword + self.to_cardinal(-n)
            
            return self._int_to_cardinal(n)
        except:
            return self._int_to_cardinal(int(n))

    def to_ordinal(self, n):
        try:
            if isinstance(n, str):
                n = int(n)
            
            return self._int_to_ordinal(n)
        except:
            return self._int_to_ordinal(int(n))

    def to_ordinal_num(self, n):
        try:
            if isinstance(n, str):
                n = int(n)
            
            # Bulgarian ordinal suffixes
            if n % 100 in [11, 12, 13, 14, 15, 16, 17, 18, 19]:
                return str(n) + '-ти'
            elif n % 10 == 1:
                return str(n) + '-ви'
            elif n % 10 == 2:
                return str(n) + '-ри'
            elif n % 10 in [7, 8]:
                return str(n) + '-ми'
            else:
                return str(n) + '-ти'
        except:
            return str(n) + '-ти'

    def to_currency(self, n, currency='BGN'):
        try:
            left, right, is_negative = parse_currency_parts(n)
            
            if currency not in self.CURRENCY_FORMS:
                raise NotImplementedError(
                    'Currency code "%s" not implemented for "%s"' %
                    (currency, self.__class__.__name__))
            
            cr_major, cr_minor = self.CURRENCY_FORMS[currency]
            
            result = []
            
            if is_negative:
                result.append(self.negword.strip())
            
            # Handle major currency with appropriate gender
            if currency == 'EUR':
                # EUR uses neuter forms (default ones)
                if left == 1:
                    left_words = 'едно'
                elif left == 2:
                    left_words = 'две'
                else:
                    left_words = self._int_to_word(left, masculine=False, feminine=False)
            else:
                # BGN, USD, GBP use masculine forms
                left_words = self._int_to_word(left, masculine=True, feminine=False)
            result.append(left_words)
            
            # Plural form for major currency
            if left == 1:
                result.append(cr_major[0])
            else:
                result.append(cr_major[1])
            
            # Handle cents if non-zero
            if right > 0:
                result.append('и')
                # Use feminine form for стотинка (feminine noun)
                if right == 1:
                    result.append('една')
                elif right == 2:
                    result.append('две')
                else:
                    right_words = self._int_to_cardinal(right)
                    result.append(right_words)
                
                # Plural form for minor currency
                if right == 1:
                    result.append(cr_minor[0])
                else:
                    result.append(cr_minor[1])
            
            return ' '.join(result)
        except NotImplementedError:
            raise
        except:
            return str(n) + ' ' + currency

    def to_year(self, n):
        if n < 1000:
            return self._int_to_cardinal(n)
        elif n < 2000:
            # Years like 1999 -> "хиляда деветстотин деветдесет и девет"
            thousands = n // 1000
            remainder = n % 1000
            if thousands == 1:
                result = 'хиляда'
            else:
                result = self._int_to_cardinal(thousands) + ' хиляди'
            
            if remainder > 0:
                result += ' ' + self._int_to_cardinal(remainder)
            return result
        else:
            # Years like 2023 -> "две хиляди двадесет и три"
            return self._int_to_cardinal(n)