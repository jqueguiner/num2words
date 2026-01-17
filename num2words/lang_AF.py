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

from __future__ import print_function, unicode_literals
from .base import Num2Word_Base
from .currency import parse_currency_parts


class Num2Word_AF(Num2Word_Base):
    CURRENCY_FORMS = {
        'ZAR': (('rand', 'rand'), ('sent', 'sent')),
        'EUR': (('euro', 'euro'), ('sent', 'sent')),
        'GBP': (('pond', 'pond'), ('penny', 'pence')),
        'USD': (('dollar', 'dollar'), ('sent', 'sent')),
    }

    def __init__(self):
        super(Num2Word_AF, self).__init__()
        
        self.negword = "minus "
        self.pointword = "komma"
        
        # Error messages in Afrikaans
        self.errmsg_floatord = (
            "Die desimale getal %s kan nie as 'n rangnommer " +
            "omgeskakel word nie."
        )
        self.errmsg_nonnum = (
            "Slegs getalle (tipe (%s)) kan na " +
            "woorde omgeskakel word."
        )
        self.errmsg_negord = (
            "Die negatiewe getal %s kan nie na 'n " +
            "rangnommer omgeskakel word nie."
        )
        self.errmsg_toobig = "Die getal %s is te groot, moet kleiner as %s wees."
        
        # Define number words
        self.numbers = {
            0: 'nul',
            1: 'een',
            2: 'twee', 
            3: 'drie',
            4: 'vier',
            5: 'vyf',
            6: 'ses',
            7: 'sewe',
            8: 'agt',
            9: 'nege',
            10: 'tien',
            11: 'elf',
            12: 'twaalf',
            13: 'dertien',
            14: 'veertien',
            15: 'vyftien',
            16: 'sestien',
            17: 'sewentien',
            18: 'agtien',
            19: 'negentien',
            20: 'twintig',
            30: 'dertig',
            40: 'veertig',
            50: 'vyftig',
            60: 'sestig',
            70: 'sewentig',
            80: 'tagtig',
            90: 'negentig'
        }

    def _int_to_word(self, n):
        """
        Convert an integer to its word representation in Afrikaans.
        """
        if n in self.numbers:
            return self.numbers[n]
            
        # Handle negative numbers
        if n < 0:
            return self.negword + self._int_to_word(-n)
            
        # Handle numbers 21-99
        if n < 100:
            tens = (n // 10) * 10
            units = n % 10
            if units > 0:
                return self.numbers[units] + "-en-" + self.numbers[tens]
            else:
                return self.numbers[tens]
                
        # Handle hundreds 100-999
        if n < 1000:
            hundreds = n // 100
            remainder = n % 100
            
            # Always use the word for the number of hundreds
            result = self.numbers[hundreds] + "honderd"
                
            if remainder > 0:
                if remainder <= 20:
                    result += " en " + self._int_to_word(remainder)
                else:
                    result += " " + self._int_to_word(remainder)
                    
            return result
            
        # Handle thousands 1000-999999
        if n < 1000000:
            thousands = n // 1000
            remainder = n % 1000
            
            # Always include the number word before "duisend"
            result = self._int_to_word(thousands) + "duisend"
                
            if remainder > 0:
                if remainder < 100:
                    result += " en " + self._int_to_word(remainder)
                else:
                    result += " " + self._int_to_word(remainder)
                    
            return result
            
        # Handle millions 1000000-999999999
        if n < 1000000000:
            millions = n // 1000000
            remainder = n % 1000000
            
            result = self._int_to_word(millions) + " miljoen"
            
            if remainder > 0:
                if remainder < 100:
                    result += " en " + self._int_to_word(remainder)
                else:
                    result += " " + self._int_to_word(remainder)
                    
            return result
            
        # Handle billions
        if n < 1000000000000:
            billions = n // 1000000000
            remainder = n % 1000000000
            
            result = self._int_to_word(billions) + " miljard"
            
            if remainder > 0:
                if remainder < 100:
                    result += " en " + self._int_to_word(remainder)
                else:
                    result += " " + self._int_to_word(remainder)
                    
            return result
            
        # For larger numbers, use default behavior
        return str(n)

    def _int_to_ordinal(self, n):
        """
        Convert an integer to its ordinal representation.
        """
        # Special ordinal mappings
        ordinals = {
            1: 'eerste',
            2: 'tweede', 
            3: 'derde',
            4: 'vierde',
            5: 'vyfde',
            6: 'sesde',
            7: 'sewende',
            8: 'agste',
            9: 'negende',
            10: 'tiende',
            11: 'elfde',
            12: 'twaalfde',
            13: 'dertiende',
            14: 'veertiende',
            15: 'vyftiende',
            16: 'sestiende',
            17: 'sewentiende',
            18: 'agtiende',
            19: 'negentiende',
            20: 'twintigste',
            30: 'dertigste',
            40: 'veertigste',
            50: 'vyftigste',
            60: 'sestigste',
            70: 'sewentigste',
            80: 'tagtigste',
            90: 'negentigste',
            100: 'eenhonderdste',
            1000: 'eenduisendste',
            1000000: 'een miljoenste'
        }
        
        if n in ordinals:
            return ordinals[n]
            
        # For compound numbers, add 'ste' to the end
        cardinal = self._int_to_word(n)
        if "-en-" in cardinal:
            return cardinal + "ste"
            
        # Default: add appropriate ending
        if cardinal.endswith(("ig", "tig")):
            return cardinal + "ste"
        else:
            return cardinal + "de"

    def to_cardinal(self, n):
        """Public interface to convert a number to its cardinal representation."""
        try:
            if isinstance(n, str):
                if '.' in n:
                    # Handle decimal numbers
                    parts = n.split('.')
                    left = int(parts[0])
                    right = parts[1]
                    result = self._int_to_word(left) + " " + self.pointword
                    for digit in right:
                        result += " " + self._int_to_word(int(digit))
                    return result
                else:
                    n = int(n)
            elif isinstance(n, float):
                # Handle float numbers
                n_str = str(n)
                if '.' in n_str:
                    parts = n_str.split('.')
                    left = int(parts[0])
                    right = parts[1]
                    result = self._int_to_word(left) + " " + self.pointword
                    for digit in right:
                        result += " " + self._int_to_word(int(digit))
                    return result
                else:
                    n = int(n)
                    
            return self._int_to_word(n)
        except Exception:
            return str(n)

    def to_ordinal(self, n):
        """Public interface to convert a number to its ordinal representation."""
        try:
            if isinstance(n, str):
                n = float(n) if '.' in n else int(n)
            
            # Use base class validation
            self.verify_ordinal(n)
                
            return self._int_to_ordinal(int(n))
        except TypeError:
            # Re-raise type errors from validation
            raise
        except Exception:
            return str(n)

    def to_ordinal_num(self, n):
        """Convert to abbreviated ordinal form (1ste, 2de, etc.)."""
        try:
            if isinstance(n, str):
                n = int(n)
                
            if n == 1:
                return "1ste"
            elif n == 2:
                return "2de"
            elif n == 3:
                return "3de"
            elif n == 8:
                return "8ste"
            else:
                # General pattern
                if n % 10 == 0 or n > 19:
                    return "%dste" % n
                else:
                    return "%dde" % n
        except Exception:
            return "%dste" % n

    def to_currency(self, n, currency='ZAR', cents=True, separator=' en',
                    cents_separator=','):
        """Convert number to currency format."""
        try:
            left, right, is_negative = parse_currency_parts(n)
            
            minus_str = ""
            if is_negative:
                minus_str = self.negword
                
            left_words = self._int_to_word(left)
            
            # Get currency forms
            cr_major, cr_minor = self.CURRENCY_FORMS.get(
                currency.upper(), self.CURRENCY_FORMS['ZAR'])
                
            # Determine singular or plural form for major currency
            major_unit = cr_major[0] if left == 1 else cr_major[1]
            
            if right > 0:
                # Format main amount with currency
                result = minus_str + left_words + " " + major_unit
                
                # Add separator
                result += separator
                
                # Format cents
                if cents:
                    cents_words = self._int_to_word(right)
                else:
                    cents_words = str(right)
                    
                # Determine singular or plural form for minor currency
                minor_unit = cr_minor[0] if right == 1 else cr_minor[1]
                result += " " + cents_words + " " + minor_unit
            else:
                result = minus_str + left_words + " " + major_unit
                
            return result
            
        except Exception:
            return str(n)

    def to_year(self, n):
        """Convert a number to a year representation."""
        # For now, just use cardinal
        return self.to_cardinal(n)