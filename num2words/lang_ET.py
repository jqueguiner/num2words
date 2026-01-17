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

ZERO = ('null',)

ONES = {
    1: ('üks',),
    2: ('kaks',),
    3: ('kolm',),
    4: ('neli',),
    5: ('viis',),
    6: ('kuus',),
    7: ('seitse',),
    8: ('kaheksa',),
    9: ('üheksa',),
}

TENS = {
    0: ('kümme',),
    1: ('üksteist',),
    2: ('kaksteist',),
    3: ('kolmteist',),
    4: ('neliteist',),
    5: ('viisteist',),
    6: ('kuusteist',),
    7: ('seitseteist',),
    8: ('kaheksateist',),
    9: ('üheksateist',),
}

TWENTIES = {
    2: ('kakskümmend',),
    3: ('kolmkümmend',),
    4: ('nelikümmend',),
    5: ('viiskümmend',),
    6: ('kuuskümmend',),
    7: ('seitsekümmend',),
    8: ('kaheksakümmend',),
    9: ('üheksakümmend',),
}

# Estonian hundred forms: sada (one hundred), kakssada (two hundred), etc.
HUNDRED = ('sada', 'sada')

THOUSANDS = {
    1: ('tuhat', 'tuhat', 'tuhat'),  # tuhat (singular and plural)
    2: ('miljon', 'miljonit', 'miljonit'),  # million
    3: ('miljard', 'miljardit', 'miljardit'),  # billion
    4: ('biljon', 'biljonit', 'biljonit'),  # trillion
    5: ('triljon', 'triljonit', 'triljonit'),  # quadrillion
    6: ('kvadriljon', 'kvadriljonit', 'kvadriljonit'),  # quintillion
}

# Currency forms: (singular nominative, plural nominative/genitive, partitive plural)
GENERIC_CENTS = ('sent', 'senti', 'senti')
GENERIC_DOLLARS = ('dollar', 'dollarit', 'dollarit')
GENERIC_EUROS = ('euro', 'eurot', 'eurot')
GENERIC_KROONS = ('kroon', 'krooni', 'krooni')


class Num2Word_ET(Num2Word_Base):
    CURRENCY_FORMS = {
        'EUR': (GENERIC_EUROS, GENERIC_CENTS),
        'USD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'EEK': (GENERIC_KROONS, GENERIC_CENTS),  # Historical Estonian kroon
    }

    def setup(self):
        self.negword = "miinus"
        self.pointword = "koma"

    def to_cardinal(self, number):
        n = str(number).replace(',', '.')
        base_str, n = self.parse_minus(n)
        if '.' in n:
            left, right = n.split('.')
            leading_zero_count = len(right) - len(right.lstrip('0'))
            decimal_part = ((ZERO[0] + ' ') * leading_zero_count +
                            self._int2word(int(right)))
            return '%s%s %s %s' % (
                base_str,
                self._int2word(int(left)),
                self.pointword,
                decimal_part
            )
        else:
            return "%s%s" % (base_str, self._int2word(int(n)))

    def pluralize(self, n, forms):
        """
        Estonian pluralization rules for currency:
        - 1: singular nominative (form 0)
        - 2-10: plural nominative (form 1)  
        - 11-19: partitive plural (form 2)
        - 20, 30, etc.: partitive plural (form 2)
        - 21, 31, etc.: singular nominative (form 0) if ending in 1, else partitive plural (form 2)
        """
        if n == 1:
            return forms[0]
        elif 2 <= n <= 10:
            return forms[1]
        elif 11 <= n <= 19:
            return forms[2] if len(forms) > 2 else forms[1]
        elif n % 10 == 1 and n % 100 != 11:
            return forms[0]
        else:
            return forms[2] if len(forms) > 2 else forms[1]

    def to_ordinal(self, number):
        raise NotImplementedError()

    def _int2word(self, n):
        if n == 0:
            return ZERO[0]

        words = []
        chunks = list(splitbyx(str(n), 3))
        i = len(chunks)
        for x in chunks:
            i -= 1

            if x == 0:
                continue

            n1, n2, n3 = get_digits(x)

            # Handle hundreds
            if n3 > 0:
                if n3 == 1:
                    words.append(HUNDRED[0])  # sada
                else:
                    # kakssada, kolmsada, etc.
                    words.append(ONES[n3][0] + HUNDRED[0])

            # Handle tens and ones
            if n2 > 1:
                words.append(TWENTIES[n2][0])

            if n2 == 1:
                words.append(TENS[n1][0])
            elif n1 > 0:
                # Special case: don't add "üks" before thousands when it's exactly 1000
                if not (i > 0 and x == 1):
                    words.append(ONES[n1][0])

            # Handle scale words (tuhat, miljon, etc.)
            if i > 0:
                words.append(self.pluralize(x, THOUSANDS[i]))

        return ' '.join(words)