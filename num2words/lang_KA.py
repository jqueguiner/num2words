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

# Georgian numerals
ONES = {
    0: 'ნული',
    1: 'ერთი',
    2: 'ორი',
    3: 'სამი',
    4: 'ოთხი',
    5: 'ხუთი',
    6: 'ექვსი',
    7: 'შვიდი',
    8: 'რვა',
    9: 'ცხრა'
}

TEENS = {
    10: 'ათი',
    11: 'თერთმეტი',
    12: 'თორმეტი',
    13: 'ცამეტი',
    14: 'თოთხმეტი',
    15: 'თხუთმეტი',
    16: 'თექვსმეტი',
    17: 'ჩვიდმეტი',
    18: 'თვრამეტი',
    19: 'ცხრამეტი'
}

# Georgian uses a vigesimal (base-20) system
TENS = {
    20: 'ოცი',
    30: 'ოცდაათი',
    40: 'ორმოცი',
    50: 'ორმოცდაათი',
    60: 'სამოცი',
    70: 'სამოცდაათი',
    80: 'ოთხმოცი',
    90: 'ოთხმოცდაათი'
}

HUNDREDS = {
    100: 'ასი',
    200: 'ორასი',
    300: 'სამასი',
    400: 'ოთხასი',
    500: 'ხუთასი',
    600: 'ექვსასი',
    700: 'შვიდასი',
    800: 'რვაასი',
    900: 'ცხრაასი'
}

# Ordinal numerals
ORDINAL_ONES = {
    1: 'პირველი',
    2: 'მეორე',
    3: 'მესამე',
    4: 'მეოთხე',
    5: 'მეხუთე',
    6: 'მეექვსე',
    7: 'მეშვიდე',
    8: 'მერვე',
    9: 'მეცხრე'
}

ORDINAL_TEENS = {
    10: 'მეათე',
    11: 'მეთერთმეტე',
    12: 'მეთორმეტე',
    13: 'მეცამეტე',
    14: 'მეთოთხმეტე',
    15: 'მეთხუთმეტე',
    16: 'მეთექვსმეტე',
    17: 'მეჩვიდმეტე',
    18: 'მეთვრამეტე',
    19: 'მეცხრამეტე'
}

ORDINAL_TENS = {
    20: 'მეოცე',
    30: 'მეოცდაათე',
    40: 'მეორმოცე',
    50: 'მეორმოცდაათე',
    60: 'მესამოცე',
    70: 'მესამოცდაათე',
    80: 'მეოთხმოცე',
    90: 'მეოთხმოცდაათე'
}

ORDINAL_HUNDREDS = {
    100: 'მეასე',
    200: 'მეორასე',
    300: 'მესამასე',
    400: 'მეოთხასე',
    500: 'მეხუთასე',
    600: 'მეექვსასე',
    700: 'მეშვიდასე',
    800: 'მერვაასე',
    900: 'მეცხრაასე'
}

ORDINAL_LARGE = {
    1000: 'მეათასე',
    1000000: 'მემილიონე',
    1000000000: 'მემილიარდე'
}


class Num2Word_KA(Num2Word_Base):
    CURRENCY_FORMS = {
        'GEL': (('ლარი', 'ლარი'), ('თეთრი', 'თეთრი')),
        'USD': (('დოლარი', 'დოლარი'), ('ცენტი', 'ცენტი')),
        'EUR': (('ევრო', 'ევრო'), ('ცენტი', 'ცენტი')),
        'RUB': (('რუბლი', 'რუბლი'), ('კოპეკი', 'კოპეკი')),
        'TRY': (('ლირა', 'ლირა'), ('კურუში', 'კურუში')),
        'GBP': (('ფუნტი', 'ფუნტი'), ('პენსი', 'პენსი')),
        'CHF': (('ფრანკი', 'ფრანკი'), ('სანტიმი', 'სანტიმი')),
        'JPY': (('იენი', 'იენი'), ('სენი', 'სენი')),
        'CNY': (('იუანი', 'იუანი'), ('ფენი', 'ფენი')),
    }

    def set_high_numwords(self, high):
        max = 3 + 10 * len(high)
        for word, n in zip(high, range(max, 3, -10)):
            self.cards[10 ** n] = word

    def setup(self):
        self.negword = "მინუს "
        self.pointword = "მთელი"
        self.exclude_title = ["და", "მთელი", "მინუს"]

        self.high_numwords = [(10**12, "ტრილიონი"), (10**9, "მილიარდი"),
                              (10**6, "მილიონი")]
        self.mid_numwords = [(1000, "ათასი"), (100, "ასი"),
                             (80, "ოთხმოცი"), (60, "სამოცი"),
                             (40, "ორმოცი"), (20, "ოცი")]
        self.low_numwords = ["ცხრამეტი", "თვრამეტი", "ჩვიდმეტი", "თექვსმეტი",
                             "თხუთმეტი", "თოთხმეტი", "ცამეტი", "თორმეტი",
                             "თერთმეტი", "ათი", "ცხრა", "რვა", "შვიდი", "ექვსი",
                             "ხუთი", "ოთხი", "სამი", "ორი", "ერთი", "ნული"]

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            # For 1000, don't need to add "ერთი"
            if nnum == 1000:
                return next
            if nnum < 1000:
                return next
            ctext = "ერთი"

        # Handle hundreds - Georgian has special combined forms
        if nnum == 100 and cnum < 10:
            if cnum == 1:
                return ("ასი", 100)
            elif cnum == 2:
                return ("ორასი", 200)
            elif cnum == 3:
                return ("სამასი", 300)
            elif cnum == 4:
                return ("ოთხასი", 400)
            elif cnum == 5:
                return ("ხუთასი", 500)
            elif cnum == 6:
                return ("ექვსასი", 600)
            elif cnum == 7:
                return ("შვიდასი", 700)
            elif cnum == 8:
                return ("რვაასი", 800)
            elif cnum == 9:
                return ("ცხრაასი", 900)

        # Handle thousands and large numbers with additional digits
        if nnum < cnum and cnum >= 1000:
            # In Georgian, thousands drop the final "ი" when followed by other numbers
            if ctext.endswith("ათასი"):
                ctext = ctext[:-1]  # "ათასი" -> "ათას"
            elif ctext.endswith("მილიონი"):
                ctext = ctext[:-1]  # "მილიონი" -> "მილიონ"
            elif ctext.endswith("მილიარდი"):
                ctext = ctext[:-1]  # "მილიარდი" -> "მილიარდ"
            return (f"{ctext} {ntext}", cnum + nnum)

        # Handle hundreds with additional digits  
        if nnum < cnum and cnum >= 100 and cnum < 1000:
            # In Georgian, hundreds drop the final "ი" when followed by other numbers
            if ctext.endswith("ასი"):
                ctext = ctext[:-1]  # "ასი" -> "ას", "ორასი" -> "ორას", etc.
            return (f"{ctext} {ntext}", cnum + nnum)

        # Handle Georgian vigesimal system
        if nnum < 100:
            if cnum < 100:
                # For Georgian vigesimal system where larger number comes first
                # ctext is the larger number (e.g., "ოცი"), ntext is smaller (e.g., "ერთი")
                if cnum == 20:
                    # Special case for 20 + 10 = 30 (ოცდაათი)
                    if nnum == 10:
                        return ("ოცდაათი", 30)
                    return (f"ოცდა{ntext}", cnum + nnum)
                elif cnum == 40:
                    # Special case for 40 + 10 = 50 (ორმოცდაათი)
                    if nnum == 10:
                        return ("ორმოცდაათი", 50)
                    return (f"ორმოცდა{ntext}", cnum + nnum)
                elif cnum == 60:
                    # Special case for 60 + 10 = 70 (სამოცდაათი)  
                    if nnum == 10:
                        return ("სამოცდაათი", 70)
                    return (f"სამოცდა{ntext}", cnum + nnum)
                elif cnum == 80:
                    # Special case for 80 + 10 = 90 (ოთხმოცდაათი)
                    if nnum == 10:
                        return ("ოთხმოცდაათი", 90)
                    return (f"ოთხმოცდა{ntext}", cnum + nnum)
                else:
                    return (f"{ctext}{ntext}", cnum + nnum)
            return (f"{ctext} {ntext}", cnum + nnum)

        # Handle multiplication for thousands, millions, billions 
        if nnum >= 1000 and cnum < 1000:
            # For Georgian: "ორი ათასი" means 2 * 1000 = 2000
            if nnum == 1000:
                return (f"{ctext} ათასი", cnum * 1000)
            elif nnum == 1000000:
                return (f"{ctext} მილიონი", cnum * 1000000)
            elif nnum == 1000000000:
                return (f"{ctext} მილიარდი", cnum * 1000000000)

        return (f"{ctext} {ntext}", cnum + nnum)

    def to_cardinal(self, value):
        if value == 0:
            return 'ნული'

        if value == 1000:
            return 'ათასი'

        # Handle millions
        if value >= 1000000 and value < 1000000000:
            millions = value // 1000000
            rest = value % 1000000
            if millions == 1:
                millions_part = 'ერთი მილიონ' if rest != 0 else 'ერთი მილიონი'
            else:
                millions_part = f'{self.to_cardinal(millions)} მილიონ' if rest != 0 else f'{self.to_cardinal(millions)} მილიონი'
            if rest == 0:
                return millions_part
            return f'{millions_part} {self.to_cardinal(rest)}'

        # Handle billions
        if value >= 1000000000 and value < 1000000000000:
            billions = value // 1000000000
            rest = value % 1000000000
            if billions == 1:
                billions_part = 'ერთი მილიარდ' if rest != 0 else 'ერთი მილიარდი'
            else:
                billions_part = f'{self.to_cardinal(billions)} მილიარდ' if rest != 0 else f'{self.to_cardinal(billions)} მილიარდი'
            if rest == 0:
                return billions_part
            return f'{billions_part} {self.to_cardinal(rest)}'

        # Handle trillions
        if value >= 1000000000000:
            trillions = value // 1000000000000
            rest = value % 1000000000000
            if trillions == 1:
                trillions_part = 'ერთი ტრილიონი'
            else:
                trillions_part = f'{self.to_cardinal(trillions)} ტრილიონი'
            if rest == 0:
                return trillions_part
            return f'{trillions_part} {self.to_cardinal(rest)}'

        # Use standard implementation for other cases
        result = super(Num2Word_KA, self).to_cardinal(value)
        return result

    def to_ordinal(self, value):
        if value == 0:
            return 'ნულოვანი'

        if value < 20:
            if value < 10:
                return ORDINAL_ONES.get(value, f"მე{ONES[value]}ე")
            else:
                return ORDINAL_TEENS.get(value, f"მე{TEENS[value]}ე")

        if value < 100:
            if value in ORDINAL_TENS:
                return ORDINAL_TENS[value]
            tens = (value // 10) * 10
            units = value % 10
            if units == 0:
                return ORDINAL_TENS.get(tens, f"მე{TENS[tens]}ე")
            if units == 1:
                # Use the combining form for vigesimal numbers
                if tens == 20:
                    return "ოცდაპირველი"
                elif tens == 40:
                    return "ორმოცდაპირველი"
                elif tens == 60:
                    return "სამოცდაპირველი"
                elif tens == 80:
                    return "ოთხმოცდაპირველი"
                elif tens in [30, 50, 70, 90]:
                    return f"{TENS[tens]} პირველი"
                else:
                    return f"{TENS[tens]}პირველი"
            else:
                # Handle other units for vigesimal numbers
                if tens == 20:
                    return f"ოცდა{ORDINAL_ONES.get(units, f'მე{ONES[units]}ე')}"
                elif tens == 40:
                    return f"ორმოცდა{ORDINAL_ONES.get(units, f'მე{ONES[units]}ე')}"
                elif tens == 60:
                    return f"სამოცდა{ORDINAL_ONES.get(units, f'მე{ONES[units]}ე')}"
                elif tens == 80:
                    return f"ოთხმოცდა{ORDINAL_ONES.get(units, f'მე{ONES[units]}ე')}"
                elif tens in [30, 50, 70, 90]:
                    return f"{TENS[tens]} {ORDINAL_ONES.get(units, f'მე{ONES[units]}ე')}"
                else:
                    return f"{TENS[tens]}{ORDINAL_ONES.get(units, f'მე{ONES[units]}ე')}"

        if value in ORDINAL_HUNDREDS:
            return ORDINAL_HUNDREDS[value]

        if value in ORDINAL_LARGE:
            return ORDINAL_LARGE[value]

        # For larger numbers use simple rule - add "მე" prefix and "ე" suffix
        cardinal = self.to_cardinal(value)
        if value == 100:
            return "მეასე"
        elif value == 1000:
            return "მეათასე"
        elif value == 1000000:
            return f"{cardinal}ე"
        else:
            # Special handling for complex ordinals
            if value > 100 and value % 100 != 0:
                hundreds_part = (value // 100) * 100
                remainder = value % 100
                if remainder == 1:
                    hundreds_str = self.to_cardinal(hundreds_part)
                    # Drop "ი" from hundreds when followed by ordinals
                    if hundreds_str.endswith("ასი"):
                        hundreds_str = hundreds_str[:-1]
                    elif hundreds_str.endswith("ათასი"):
                        hundreds_str = hundreds_str[:-1]
                    return f"{hundreds_str} პირველი"
                else:
                    return f"{self.to_cardinal(hundreds_part)} {self.to_ordinal(remainder)}"
            return f"მე{cardinal}ე"

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        if value == 1:
            return "1-ლი"
        else:
            return f"{value}-ე"

    def pluralize(self, n, forms):
        # Georgian doesn't have complex plural rules like some languages
        # Most words remain the same in plural
        if forms:
            if len(forms) >= 2:
                return forms[0]  # Georgian typically uses the same form
            return forms[0]
        return ''

    def to_year(self, val, longval=True):
        return f"{self.to_cardinal(val)} წელი"

    def to_currency(self, val, currency='GEL', cents=True):
        """
        Convert a value to Georgian currency format.
        """
        result = []
        is_negative = val < 0
        val = abs(val)

        if currency in self.CURRENCY_FORMS:
            if cents:
                # Get cents
                cents = int(round(val * 100))
                # Split whole and cents
                whole, cents = cents // 100, cents % 100
            else:
                whole, cents = int(val), 0

            # Main currency part
            if whole:
                result.append(self.to_cardinal(whole))
                result.append(
                    self.pluralize(whole, self.CURRENCY_FORMS[currency][0])
                )
            elif not cents:  # Handle case where whole is 0 and no cents
                result.append(self.to_cardinal(0))
                result.append(
                    self.pluralize(0, self.CURRENCY_FORMS[currency][0])
                )

            # Add cents
            if cents:
                if whole:
                    result.append(self.to_cardinal(cents))
                    result.append(
                        self.pluralize(cents, self.CURRENCY_FORMS[currency][1])
                    )
                else:
                    result.append(self.to_cardinal(cents))
                    result.append(
                        self.pluralize(cents, self.CURRENCY_FORMS[currency][1])
                    )

            if is_negative:
                result.insert(0, 'მინუს')

            return ' '.join(result)
        else:
            return self.to_cardinal(val)

    def to_cardinal_negative(self, value):
        # Convert negative number
        if value < 0:
            return f"მინუს {self.to_cardinal(abs(value))}"
        return self.to_cardinal(value)