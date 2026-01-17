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
Module for converting numbers to words in Albanian (Shqip).
"""

from __future__ import unicode_literals

from .base import Num2Word_Base


class Num2Word_SQ(Num2Word_Base):
    """Convert numbers to Albanian words."""
    
    CURRENCY_FORMS = {
        'EUR': (('euro', 'euro'), ('cent', 'cent')),
        'USD': (('dollar', 'dollar'), ('cent', 'cent')),
        'ALL': (('lek', 'lekë'), ('qindarkë', 'qindarkë')),  # Albanian Lek
        'GBP': (('paund', 'paund'), ('peni', 'peni')),
    }

    def __init__(self):
        super(Num2Word_SQ, self).__init__()
        
        # Basic numbers 0-19
        self.ones = {
            0: 'zero',
            1: 'një',
            2: 'dy',
            3: 'tre',
            4: 'katër',
            5: 'pesë',
            6: 'gjashtë',
            7: 'shtatë',
            8: 'tetë',
            9: 'nëntë',
            10: 'dhjetë',
            11: 'njëmbëdhjetë',
            12: 'dymbëdhjetë',
            13: 'trembëdhjetë',
            14: 'katërmbëdhjetë',
            15: 'pesëmbëdhjetë',
            16: 'gjashtëmbëdhjetë',
            17: 'shtatëmbëdhjetë',
            18: 'tetëmbëdhjetë',
            19: 'nëntëmbëdhjetë',
        }
        
        # Tens 20-90
        self.tens = {
            20: 'njëzet',
            30: 'tridhjetë',
            40: 'dyzet',
            50: 'pesëdhjetë',
            60: 'gjashtëdhjetë',
            70: 'shtatëdhjetë',
            80: 'tetëdhjetë',
            90: 'nëntëdhjetë',
        }
        
        # Scale words
        self.scale = {
            100: 'qind',
            1000: 'mijë',
            1000000: 'milion',
            1000000000: 'miliard',
            1000000000000: 'trilion',
            1000000000000000: 'katrilion',
        }
        
        # Ordinal words for basic numbers
        self.ordinal_ones = {
            1: 'i parë',
            2: 'i dytë',
            3: 'i tretë',
            4: 'i katërt',
            5: 'i pestë',
            6: 'i gjashtë',
            7: 'i shtatë',
            8: 'i tetë',
            9: 'i nëntë',
            10: 'i dhjetë',
        }

    def int_to_word(self, number):
        """Convert an integer to its Albanian word representation."""
        if number == 0:
            return self.ones[0]
        
        if number < 0:
            return 'minus ' + self.int_to_word(-number)
        
        return self._int_to_word_positive(number)

    def _int_to_word_positive(self, number):
        """Convert a positive integer to Albanian words."""
        if number < 20:
            return self.ones[number]
        elif number < 100:
            return self._convert_tens(number)
        elif number < 1000:
            return self._convert_hundreds(number)
        elif number < 1000000:
            return self._convert_thousands(number)
        elif number < 1000000000:
            return self._convert_millions(number)
        elif number < 1000000000000:
            return self._convert_billions(number)
        else:
            return self._convert_trillions(number)

    def _convert_tens(self, number):
        """Convert numbers 20-99 to Albanian words."""
        tens_digit = (number // 10) * 10
        ones_digit = number % 10
        
        if ones_digit == 0:
            return self.tens[tens_digit]
        else:
            return self.tens[tens_digit] + ' e ' + self.ones[ones_digit]

    def _convert_hundreds(self, number):
        """Convert numbers 100-999 to Albanian words."""
        hundreds_digit = number // 100
        remainder = number % 100
        
        if hundreds_digit == 1:
            result = 'njëqind'
        else:
            result = self.ones[hundreds_digit] + 'qind'
        
        if remainder > 0:
            if remainder < 20:
                result += ' e ' + self.ones[remainder]
            elif remainder % 10 == 0:
                result += ' ' + self.tens[remainder]
            else:
                result += ' ' + self._convert_tens(remainder)
        
        return result

    def _convert_thousands(self, number):
        """Convert numbers 1,000-999,999 to Albanian words."""
        thousands = number // 1000
        remainder = number % 1000
        
        if thousands == 1:
            result = 'një mijë'
        elif thousands < 20:
            result = self.ones[thousands] + ' mijë'
        elif thousands < 100:
            result = self._convert_tens(thousands) + ' mijë'
        else:
            result = self._convert_hundreds(thousands) + ' mijë'
        
        if remainder > 0:
            # Use 'e' only when the remainder is less than 100 or when it's a pure tens/hundreds
            if remainder < 100 or remainder % 100 == 0:
                result += ' e ' + self._int_to_word_positive(remainder)
            else:
                result += ' ' + self._int_to_word_positive(remainder)
        
        return result

    def _convert_millions(self, number):
        """Convert numbers 1,000,000-999,999,999 to Albanian words."""
        millions = number // 1000000
        remainder = number % 1000000
        
        if millions == 1:
            result = 'një milion'
        else:
            result = self._int_to_word_positive(millions) + ' milion'
        
        if remainder > 0:
            # Use 'e' when the remainder is small (under 1000) or when connecting to thousands
            result += ' e ' + self._int_to_word_positive(remainder)
        
        return result

    def _convert_billions(self, number):
        """Convert numbers 1,000,000,000-999,999,999,999 to Albanian words."""
        billions = number // 1000000000
        remainder = number % 1000000000
        
        if billions == 1:
            result = 'një miliard'
        else:
            result = self._int_to_word_positive(billions) + ' miliard'
        
        if remainder > 0:
            # Use 'e' to connect billions to the remainder
            result += ' e ' + self._int_to_word_positive(remainder)
        
        return result

    def _convert_trillions(self, number):
        """Convert numbers 1,000,000,000,000+ to Albanian words."""
        if number < 1000000000000000:  # Less than quadrillion
            trillions = number // 1000000000000
            remainder = number % 1000000000000
            
            if trillions == 1:
                result = 'një trilion'
            else:
                result = self._int_to_word_positive(trillions) + ' trilion'
            
            if remainder > 0:
                # Use 'e' to connect trillions to the remainder
                result += ' e ' + self._int_to_word_positive(remainder)
            
            return result
        else:
            # Handle quadrillions and higher
            quadrillions = number // 1000000000000000
            remainder = number % 1000000000000000
            
            if quadrillions == 1:
                result = 'një katrilion'
            else:
                result = self._int_to_word_positive(quadrillions) + ' katrilion'
            
            if remainder > 0:
                # Use 'e' to connect quadrillions to the remainder
                result += ' e ' + self._int_to_word_positive(remainder)
            
            return result

    def to_cardinal(self, number):
        """Convert number to cardinal form."""
        if isinstance(number, str):
            number = float(number)
        
        if isinstance(number, float):
            if number.is_integer():
                return self.int_to_word(int(number))
            else:
                return self.float_to_word(number)
        else:
            return self.int_to_word(number)

    def to_ordinal(self, number):
        """Convert number to ordinal form."""
        if isinstance(number, str):
            number = int(number)
            
        if number in self.ordinal_ones:
            return self.ordinal_ones[number]
        else:
            # For larger numbers, prefix with 'i' 
            return 'i ' + self.int_to_word(number)

    def pluralize(self, n, forms):
        """Return proper form based on number."""
        if len(forms) == 2:
            return forms[1] if n != 1 else forms[0]
        else:
            return forms[0]

    def float_to_word(self, val):
        """Convert float to words using 'presje' as decimal separator."""
        pre = int(val)
        post = abs(val - pre)
        
        out = [self.int_to_word(pre)]
        if post:
            out.append('presje')
            
            # Convert decimal part to string and handle properly
            decimal_str = f"{post:.10f}"[2:].rstrip('0')  # Remove '0.' and trailing zeros
            if not decimal_str:  # If all zeros after rstrip
                decimal_str = '0'
                
            for digit in decimal_str:
                out.append(self.ones[int(digit)])
        
        return ' '.join(out)

