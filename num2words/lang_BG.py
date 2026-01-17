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
from .utils import get_digits, splitbyx

ZERO = ('нула',)

ONES = {
    1: ('един', 'една', 'едно'),  # masculine, feminine, neuter
    2: ('два', 'две', 'две'),     # masculine, feminine, neuter  
    3: ('три',),
    4: ('четири',),
    5: ('пет',),
    6: ('шест',),
    7: ('седем',),
    8: ('осем',),
    9: ('девет',),
}

TENS = {
    0: ('десет',),
    1: ('единадесет',),
    2: ('дванадесет',),
    3: ('тринадесет',),
    4: ('четиринадесет',),
    5: ('петнадесет',),
    6: ('шестнадесет',),
    7: ('седемнадесет',),
    8: ('осемнадесет',),
    9: ('деветнадесет',),
}

TWENTIES = {
    2: ('двадесет',),
    3: ('тридесет',),
    4: ('четиридесет',),
    5: ('петдесет',),
    6: ('шестдесет',),
    7: ('седемдесет',),
    8: ('осемдесет',),
    9: ('деветдесет',),
}

HUNDREDS = {
    1: ('сто',),
    2: ('двеста',),
    3: ('триста',),
    4: ('четиристотин',),
    5: ('петстотин',),
    6: ('шестстотин',),
    7: ('седемстотин',),
    8: ('осемстотин',),
    9: ('деветстотин',),
}

THOUSANDS = {
    1: ('хиляда', 'хиляди', 'хиляди'),  # 10^3
    2: ('милион', 'милиона', 'милиона'),  # 10^6
    3: ('милиард', 'милиарда', 'милиарда'),  # 10^9
    4: ('трилион', 'трилиона', 'трилиона'),  # 10^12
    5: ('квадрилион', 'квадрилиона', 'квадрилиона'),  # 10^15
    6: ('квинтилион', 'квинтилиона', 'квинтилиона'),  # 10^18
}


class Num2Word_BG(Num2Word_Base):
    CURRENCY_FORMS = {
        'BGN': (
            ('лев', 'лева', 'лева'), ('стотинка', 'стотинки', 'стотинки')
        ),
        'EUR': (
            ('евро', 'евро', 'евро'), ('цент', 'цента', 'цента')
        ),
    }

    def setup(self):
        self.negword = "минус"
        self.pointword = "цяло"

    def to_cardinal(self, number):
        n = str(number).replace(',', '.')
        if '.' in n:
            is_negative = n.startswith('-')
            abs_n = n[1:] if is_negative else n
            left, right = abs_n.split('.')
            leading_zero_count = len(right) - len(right.lstrip('0'))
            # Decimal parts use feminine gender in Bulgarian for numbers like "две"
            decimal_part = ((ZERO[0] + ' ') * leading_zero_count +
                            self._int2word(int(right), 'f'))
            result = u'%s %s %s' % (
                self._int2word(int(left)),
                self.pointword,
                decimal_part
            )
            if is_negative:
                result = self.negword + ' ' + result
            return result
        else:
            # Handle negative numbers
            if number < 0:
                return self.negword + ' ' + self._int2word(abs(int(number)))
            return self._int2word(int(n))

    def pluralize(self, n, forms):
        if n == 1:
            form = 0
        elif n == 2:
            form = 1 
        else:
            form = 2
        return forms[form]

    def to_ordinal(self, number):
        raise NotImplementedError()

    def _int2word(self, n, gender='m'):
        if n == 0:
            return ZERO[0]

        words = []
        chunks = list(splitbyx(str(n), 3))
        i = len(chunks)
        
        non_zero_chunks = [(x, len(chunks) - 1 - idx) for idx, x in enumerate(chunks) if x != 0]
        
        for idx, (x, i) in enumerate(non_zero_chunks):
            # Add "и" between major groups when appropriate
            if idx > 0:  # Not the first chunk
                prev_i = non_zero_chunks[idx - 1][1]
                
                should_add_i = False
                
                if i == 0:  # Final chunk (units)
                    _, _, n3 = get_digits(x)
                    if n3 == 0:  # No hundreds - add "и" 
                        should_add_i = True
                    elif prev_i == 1 and x % 100 == 0 and x > 0:
                        # Thousands to exact hundreds (like 1100)
                        should_add_i = True
                elif i == 1 and prev_i > 1:  # Millions+ to thousands
                    # Check if this is the last non-zero chunk
                    if idx == len(non_zero_chunks) - 1:
                        should_add_i = True
                        
                if should_add_i:
                    words.append('и')

            # Convert chunk to words
            # Use gender based on the thousand level
            if i == 0:
                chunk_gender = gender  # Use provided gender for main number
            elif i == 1:
                chunk_gender = 'f'  # thousands are feminine (хиляди)
            else:
                chunk_gender = 'm'  # millions and above are masculine
            
            chunk_words = self._convert_chunk(x, i, chunk_gender)
            words.extend(chunk_words)

        return ' '.join(words)

    def _convert_chunk(self, x, thousand_index, gender='m'):
        """Convert a 3-digit chunk to words"""
        n1, n2, n3 = get_digits(x)
        words = []
        
        # Handle hundreds
        if n3 > 0:
            words.append(HUNDREDS[n3][0])

        # Handle tens and ones
        tens_ones_words = []
        if n2 > 1:
            # Twenties, thirties, etc.
            tens_ones_words.append(TWENTIES[n2][0])
            if n1 > 0:
                tens_ones_words.append('и')
                tens_ones_words.append(self._get_ones_word(n1, gender))
        elif n2 == 1:
            # Teens
            tens_ones_words.append(TENS[n1][0])
        elif n1 > 0:
            # Just ones (but not if we're at thousand level and it's 1)
            if not (thousand_index > 0 and x == 1):
                tens_ones_words.append(self._get_ones_word(n1, gender))

        # Add "и" between hundreds and tens/ones but only for direct connection
        # Don't add "и" if tens is a simple twenty, thirty etc (деветдесет)
        if words and tens_ones_words:
            # Check if we have compound tens (which already have "и")
            has_compound_tens = n2 > 1 and n1 > 0
            # Check if we have simple tens (like деветдесет with no ones)
            has_simple_tens = n2 > 1 and n1 == 0
            # Only add "и" for simple cases: hundreds + single digit or hundreds + teen
            # NOT for compound tens (twenty-one) or simple tens (twenty, thirty etc)
            if not has_compound_tens and not has_simple_tens:
                words.append('и')
        
        words.extend(tens_ones_words)

        # Add thousand/million/billion suffix
        if thousand_index > 0:
            # For millions, billions and above - add "един" if the chunk is 1
            # But for thousands (index 1), we don't add "един" - just "хиляда"
            if x == 1 and thousand_index >= 2:  # millions and above need "един"
                words = ['един'] + words
            words.append(self.pluralize(x, THOUSANDS[thousand_index]))

        return words

    def _get_ones_word(self, digit, gender='m'):
        """Get the word for a ones digit with proper gender agreement"""
        if digit == 0:
            return ZERO[0]
        
        ones_forms = ONES[digit]
        if len(ones_forms) == 1:
            return ones_forms[0]
        
        # Handle gender agreement for 1 and 2
        gender_index = 0  # masculine by default
        if gender == 'f':
            gender_index = 1  # feminine
        elif gender == 'n':
            gender_index = 2  # neuter
            
        return ones_forms[gender_index]

    def _money_verbose(self, number, currency):
        """Handle gender agreement for currency"""
        # Bulgarian currency forms:
        # BGN: лев (masculine), стотинка (feminine) 
        # EUR: евро (neuter), цент (masculine)
        if currency == 'BGN':
            gender = 'm'  # лев is masculine
        elif currency == 'EUR':
            gender = 'n'  # евро is neuter  
        else:
            gender = 'm'  # default
            
        return self._int2word(number, gender)

    def _cents_verbose(self, number, currency):
        """Handle gender agreement for cents"""
        if currency == 'BGN':
            gender = 'f'  # стотинка is feminine
        elif currency == 'EUR': 
            gender = 'm'  # цент is masculine
        else:
            gender = 'm'  # default
            
        return self._int2word(number, gender)