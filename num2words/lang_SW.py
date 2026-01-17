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
Module for converting numbers to words in Swahili (Kiswahili).
Swahili is a Bantu language spoken in East Africa.
"""

from __future__ import unicode_literals

from .base import Num2Word_Base


class Num2Word_SW(Num2Word_Base):
    """Convert numbers to Swahili words."""
    
    CURRENCY_FORMS = {
        'USD': (('dola', 'dola'), ('senti', 'senti')),
        'EUR': (('yuro', 'yuro'), ('senti', 'senti')),
        'GBP': (('pauni', 'pauni'), ('peni', 'peni')),
        'KES': (('shilingi', 'shilingi'), ('senti', 'senti')),  # Kenyan Shilling
        'TZS': (('shilingi', 'shilingi'), ('senti', 'senti')),  # Tanzanian Shilling
        'UGX': (('shilingi', 'shilingi'), ('senti', 'senti')),  # Ugandan Shilling
    }

    def __init__(self):
        super(Num2Word_SW, self).__init__()
        
        # Basic numbers 0-10
        self.ones = {
            0: 'sifuri',
            1: 'moja',
            2: 'mbili',
            3: 'tatu',
            4: 'nne',
            5: 'tano',
            6: 'sita',
            7: 'saba',
            8: 'nane',
            9: 'tisa',
            10: 'kumi'
        }
        
        # Tens
        self.tens = {
            20: 'ishirini',
            30: 'thelathini',
            40: 'arobaini',
            50: 'hamsini',
            60: 'sitini',
            70: 'sabini',
            80: 'themanini',
            90: 'tisini'
        }
        
        # Scale words
        self.scale = {
            100: 'mia',
            1000: 'elfu',
            1000000: 'milioni',
            1000000000: 'bilioni',
            1000000000000: 'trilioni'
        }
        
        # Special ordinals in Swahili
        self.ordinals = {
            1: 'kwanza',
            2: 'pili',
            3: 'tatu',
            4: 'nne',
            5: 'tano',
            6: 'sita',
            7: 'saba',
            8: 'nane',
            9: 'tisa',
            10: 'kumi'
        }

    def setup(self):
        super(Num2Word_SW, self).setup()
        self.negword = "hasara"
        self.pointword = "nukta"

    def _int_to_sw_word(self, number):
        """Convert an integer to Swahili words."""
        
        if number == 0:
            return self.ones[0]
        
        if number < 0:
            return self.negword + " " + self._int_to_sw_word(-number)
            
        if number <= 10:
            return self.ones[number]
            
        # Numbers 11-19
        if number < 20:
            return "kumi na " + self.ones[number - 10]
            
        # Numbers 20-99
        if number < 100:
            tens, units = divmod(number, 10)
            if units == 0:
                return self.tens[tens * 10]
            else:
                return self.tens[tens * 10] + " na " + self.ones[units]
                
        # Numbers 100-999
        if number < 1000:
            hundreds, remainder = divmod(number, 100)
            result = "mia " + self.ones[hundreds]
            if remainder > 0:
                result += " na " + self._int_to_sw_word(remainder)
            return result
                    
        # Numbers 1000-999999
        if number < 1000000:
            thousands, remainder = divmod(number, 1000)
            result = "elfu " + self._int_to_sw_word(thousands)
            if remainder > 0:
                result += " na " + self._int_to_sw_word(remainder)
            return result
                
        # Numbers 1000000-999999999
        if number < 1000000000:
            millions, remainder = divmod(number, 1000000)
            result = "milioni " + self._int_to_sw_word(millions)
            if remainder > 0:
                result += " na " + self._int_to_sw_word(remainder)
            return result
                        
        # Numbers 1000000000-999999999999
        if number < 1000000000000:
            billions, remainder = divmod(number, 1000000000)
            result = "bilioni " + self._int_to_sw_word(billions)
            if remainder > 0:
                result += " na " + self._int_to_sw_word(remainder)
            return result
                    
        # Trillions
        trillions, remainder = divmod(number, 1000000000000)
        result = "trilioni " + self._int_to_sw_word(trillions)
        if remainder > 0:
            result += " na " + self._int_to_sw_word(remainder)
        return result
    
    def to_cardinal(self, number):
        """Convert a number to its cardinal representation."""
        try:
            if isinstance(number, str):
                number = float(number) if '.' in number else int(number)
            
            # Handle floats
            if isinstance(number, float):
                return self.to_cardinal_float(number)
                
            return self._int_to_sw_word(int(number))
            
        except Exception:
            return self._int_to_sw_word(int(number))
    
    def to_cardinal_float(self, number):
        """Convert a float to its cardinal representation."""
        sign = ""
        if number < 0:
            sign = self.negword + " "
            number = abs(number)
            
        integer_part = int(number)
        decimal_str = str(number)
        
        if '.' in decimal_str:
            decimal_part = decimal_str.split('.')[1]
        else:
            decimal_part = ''
        
        result = self._int_to_sw_word(integer_part)
        
        if decimal_part:
            result += " " + self.pointword
            for digit in decimal_part:
                result += " " + self.ones[int(digit)]
                
        return sign + result
    
    def to_ordinal(self, number):
        """Convert a number to its ordinal representation."""
        # Special ordinal forms for basic numbers
        if number in self.ordinals:
            return "wa " + self.ordinals[number]
        
        # For other numbers, use the cardinal with "wa" prefix
        cardinal = self._int_to_sw_word(number)
        return "wa " + cardinal
    
    def to_ordinal_num(self, number):
        """Convert a number to its abbreviated ordinal form."""
        # Swahili uses period after number for ordinals
        return str(number) + "."
    
    def to_currency(self, n, currency='USD', cents=True, separator='na'):
        """Convert a number to a currency representation."""
        result = []
        value = self.float_to_value(n)
        
        if value < 0:
            result.append(self.negword)
            value = abs(value)
            
        integer_part, decimal_part = self._split_currency(value)
        
        # Get currency forms
        if currency not in self.CURRENCY_FORMS:
            # Default to treating as USD if currency not found
            currency_forms = self.CURRENCY_FORMS['USD']
        else:
            currency_forms = self.CURRENCY_FORMS[currency]
            
        major_singular, major_plural = currency_forms[0]
        minor_singular, minor_plural = currency_forms[1]
        
        # Major currency unit
        if integer_part == 0 and decimal_part > 0:
            # Only cents/minor units
            pass
        else:
            result.append(major_singular + " " + self._int_to_sw_word(integer_part))
            
        # Minor currency unit (cents)
        if cents and decimal_part > 0:
            if integer_part > 0:
                result.append(separator)
            result.append(minor_singular + " " + self._int_to_sw_word(decimal_part))
                
        return " ".join(result)
    
    def _split_currency(self, value):
        """Split a currency value into integer and decimal parts."""
        integer_part = int(value)
        decimal_part = int(round((value - integer_part) * 100))
        return integer_part, decimal_part
    
    def to_year(self, number):
        """Convert a number to a year representation."""
        # In Swahili, years are typically expressed as regular cardinal numbers
        return self._int_to_sw_word(number)
    
    def float_to_value(self, n):
        """Convert string or float to float value."""
        if isinstance(n, str):
            return float(n)
        return n