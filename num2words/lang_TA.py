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


class Num2Word_TA(Num2Word_Base):
    """
    Tamil (TA) Num2Word class
    """

    # Irregular ordinals for specific numbers
    _irregular_ordinals = {
        1: "முதல்",
        2: "இரண்டாம்",
        3: "மூன்றாம்"
    }

    def setup(self):
        # Numbers from 0-99 in reverse order (99 down to 0)
        # This matches the pattern used in other language implementations
        self.low_numwords = [
            "தொண்ணூற்றி ஒன்பது",  # 99
            "தொண்ணூற்றி எட்டு",     # 98
            "தொண்ணூற்றி ஏழு",      # 97
            "தொண்ணூற்றி ஆறு",      # 96
            "தொண்ணூற்றி ஐந்து",     # 95
            "தொண்ணூற்றி நான்கு",     # 94
            "தொண்ணூற்றி மூன்று",     # 93
            "தொண்ணூற்றி இரண்டு",     # 92
            "தொண்ணூற்றி ஒன்று",     # 91
            "தொண்ணூறு",            # 90
            "எண்பத்தி ஒன்பது",      # 89
            "எண்பத்தி எட்டு",       # 88
            "எண்பத்தி ஏழு",        # 87
            "எண்பத்தி ஆறு",        # 86
            "எண்பத்தி ஐந்து",       # 85
            "எண்பத்தி நான்கு",       # 84
            "எண்பத்தி மூன்று",       # 83
            "எண்பத்தி இரண்டு",       # 82
            "எண்பத்தி ஒன்று",       # 81
            "எண்பது",              # 80
            "எழுபத்தி ஒன்பது",       # 79
            "எழுபத்தி எட்டு",        # 78
            "எழுபத்தி ஏழு",         # 77
            "எழுபத்தி ஆறு",         # 76
            "எழுபத்தி ஐந்து",        # 75
            "எழுபத்தி நான்கு",        # 74
            "எழுபத்தி மூன்று",        # 73
            "எழுபத்தி இரண்டு",        # 72
            "எழுபத்தி ஒன்று",        # 71
            "எழுபது",               # 70
            "அறுபத்தி ஒன்பது",       # 69
            "அறுபத்தி எட்டு",        # 68
            "அறுபத்தி ஏழு",         # 67
            "அறுபத்தி ஆறு",         # 66
            "அறுபத்தி ஐந்து",        # 65
            "அறுபத்தி நான்கு",        # 64
            "அறுபத்தி மூன்று",        # 63
            "அறுபத்தி இரண்டு",        # 62
            "அறுபத்தி ஒன்று",        # 61
            "அறுபது",               # 60
            "ஐம்பத்தி ஒன்பது",       # 59
            "ஐம்பத்தி எட்டு",        # 58
            "ஐம்பத்தி ஏழு",         # 57
            "ஐம்பத்தி ஆறு",         # 56
            "ஐம்பத்தி ஐந்து",        # 55
            "ஐம்பத்தி நான்கு",        # 54
            "ஐம்பத்தி மூன்று",        # 53
            "ஐம்பத்தி இரண்டு",        # 52
            "ஐம்பத்தி ஒன்று",        # 51
            "ஐம்பது",               # 50
            "நாற்பத்தி ஒன்பது",       # 49
            "நாற்பத்தி எட்டு",        # 48
            "நாற்பத்தி ஏழு",         # 47
            "நாற்பத்தி ஆறு",         # 46
            "நாற்பத்தி ஐந்து",        # 45
            "நாற்பத்தி நான்கு",        # 44
            "நாற்பத்தி மூன்று",        # 43
            "நாற்பத்தி இரண்டு",        # 42
            "நாற்பத்தி ஒன்று",        # 41
            "நாற்பது",               # 40
            "முப்பத்தி ஒன்பது",       # 39
            "முப்பத்தி எட்டு",        # 38
            "முப்பத்தி ஏழு",         # 37
            "முப்பத்தி ஆறு",         # 36
            "முப்பத்தி ஐந்து",        # 35
            "முப்பத்தி நான்கு",        # 34
            "முப்பத்தி மூன்று",        # 33
            "முப்பத்தி இரண்டு",        # 32
            "முப்பத்தி ஒன்று",        # 31
            "முப்பது",               # 30
            "இருபத்தி ஒன்பது",       # 29
            "இருபத்தி எட்டு",        # 28
            "இருபத்தி ஏழு",         # 27
            "இருபத்தி ஆறு",         # 26
            "இருபத்தி ஐந்து",        # 25
            "இருபத்தி நான்கு",        # 24
            "இருபத்தி மூன்று",        # 23
            "இருபத்தி இரண்டு",        # 22
            "இருபத்தி ஒன்று",        # 21
            "இருபது",               # 20
            "பத்தொன்பது",           # 19
            "பதினெட்டு",            # 18
            "பதினேழு",             # 17
            "பதினாறு",             # 16
            "பதினைந்து",            # 15
            "பதினான்கு",            # 14
            "பதின்மூன்று",          # 13
            "பன்னிரண்டு",          # 12
            "பதினொன்று",           # 11
            "பத்து",               # 10
            "ஒன்பது",              # 9
            "எட்டு",               # 8
            "ஏழு",                # 7
            "ஆறு",                # 6
            "ஐந்து",               # 5
            "நான்கு",               # 4
            "மூன்று",               # 3
            "இரண்டு",               # 2
            "ஒன்று",               # 1
            "பூஜ்ஜியம்",            # 0
        ]

        # Hundred
        self.mid_numwords = [(100, "நூறு")]

        # Higher numbers: thousand, lakh (100k), crore (10M)
        # Using Indian numbering system
        self.high_numwords = [
            (7, "கோடி"),      # 10,000,000 (crore)
            (5, "லட்சம்"),    # 100,000 (lakh)
            (3, "ஆயிரம்"),    # 1,000 (thousand)
        ]

        # Set point word for decimal numbers
        self.pointword = "தசமம்"
        
        # Set negative word
        self.negword = "(-) "

    def set_high_numwords(self, high):
        """Set high number words (thousands, lakhs, crores)"""
        for n, word in self.high_numwords:
            self.cards[10**n] = word

    def merge(self, lpair, rpair):
        """Merge two number pairs following Tamil grammar rules"""
        ltext, lnum = lpair
        rtext, rnum = rpair
        
        # Handle special case where left number is 1 and right is less than 100
        if lnum == 1 and rnum < 100:
            return rtext, rnum
        # Handle multiplication cases (e.g., 2 x 100 = 200, 3 x 1000 = 3000)
        elif rnum > lnum:
            if rnum == 100:  # hundreds
                if lnum == 1:
                    return rtext, lnum * rnum  # "நூறு" for 100
                else:
                    # Use special combined forms for 200-900
                    hundreds_map = {
                        200: "இருநூறு", 300: "முன்னூறு", 400: "நானூறு", 
                        500: "ஐநூறு", 600: "அறுநூறு", 700: "எழுநூறு", 
                        800: "எண்ணூறு", 900: "தொள்ளாயிரம்"
                    }
                    result_num = lnum * rnum
                    if result_num in hundreds_map:
                        return hundreds_map[result_num], result_num
                    else:
                        return "%s %s" % (ltext, rtext), result_num
            elif rnum == 1000:  # thousands
                if lnum == 1:
                    return rtext, lnum * rnum  # "ஆயிரம்" for 1000
                else:
                    return "%s %s" % (ltext, rtext), lnum * rnum
            elif rnum == 100000:  # lakhs
                if lnum == 1:
                    return rtext, lnum * rnum  # "லட்சம்" for 100000
                else:
                    return "%s %s" % (ltext, rtext), lnum * rnum
            elif rnum == 10000000:  # crores
                if lnum == 1:
                    return rtext, lnum * rnum  # "கோடி" for 10000000
                else:
                    return "%s %s" % (ltext, rtext), lnum * rnum
            else:
                return "%s %s" % (ltext, rtext), lnum * rnum
        # Handle addition cases (e.g., 100 + 1 = 101, 200 + 34 = 234)
        elif lnum >= 100 > rnum:
            # Special handling for hundreds with connecting 'i' (இ)
            if lnum == 100:
                return "நூற்றி %s" % rtext, lnum + rnum
            elif ltext == "இருநூறு":  # 200
                return "இருநூற்றி %s" % rtext, lnum + rnum
            elif ltext == "முன்னூறு":  # 300
                return "முன்னூற்றி %s" % rtext, lnum + rnum
            elif ltext == "நானூறு":  # 400
                return "நானூற்றி %s" % rtext, lnum + rnum
            elif ltext == "ஐநூறு":  # 500
                return "ஐநூற்றி %s" % rtext, lnum + rnum
            elif ltext == "அறுநூறு":  # 600
                return "அறுநூற்றி %s" % rtext, lnum + rnum
            elif ltext == "எழுநூறு":  # 700
                return "எழுநூற்றி %s" % rtext, lnum + rnum
            elif ltext == "எண்ணூறு":  # 800
                return "எண்ணூற்றி %s" % rtext, lnum + rnum
            elif ltext == "தொள்ளாயிரம்":  # 900
                return "தொள்ளாயிரத்தி %s" % rtext, lnum + rnum
            elif ltext == "ஆயிரம்":  # 1000
                return "ஆயிரத்தி %s" % rtext, lnum + rnum
            elif ltext == "லட்சம்":  # 100000
                return "லட்சத்தி %s" % rtext, lnum + rnum
            elif ltext == "கோடி":  # 10000000
                return "கோடியே %s" % rtext, lnum + rnum
            elif lnum % 1000 == 0 and lnum > 1000:  # multiples of 1000
                return "%s ஆயிரத்தி %s" % (ltext, rtext), lnum + rnum
            elif lnum % 100000 == 0 and lnum > 100000:  # multiples of lakh
                return "%s லட்சத்தி %s" % (ltext, rtext), lnum + rnum
            elif lnum % 10000000 == 0 and lnum > 10000000:  # multiples of crore
                return "%s கோடியே %s" % (ltext, rtext), lnum + rnum
            else:
                return "%s %s" % (ltext, rtext), lnum + rnum
        # Handle compound thousands/lakhs/crores with remainders
        elif lnum >= 1000:
            if ltext == "ஆயிரம்":  # exact 1000
                return "ஆயிரத்தி %s" % rtext, lnum + rnum
            elif ltext == "லட்சம்":  # exact lakh
                return "லட்சத்தி %s" % rtext, lnum + rnum  
            elif ltext == "கோடி":  # exact crore
                return "கோடியே %s" % rtext, lnum + rnum
            elif lnum % 10000000 == 0:  # exact multiple of crore
                if ltext.endswith(" கோடி"):
                    base = ltext[:-5]  # remove " கோடி"
                    return "%s கோடியே %s" % (base, rtext), lnum + rnum
                else:
                    return "%s கோடியே %s" % (ltext, rtext), lnum + rnum
            elif lnum % 100000 == 0:  # exact multiple of lakh
                if ltext.endswith(" லட்சம்"):
                    base = ltext[:-7]  # remove " லட்சம்"
                    return "%s லட்சத்தி %s" % (base, rtext), lnum + rnum
                else:
                    return "%s லட்சத்தி %s" % (ltext, rtext), lnum + rnum
            elif lnum % 1000 == 0:  # exact multiple of thousand
                # Handle special case where ltext ends with "ஆயிரம்"
                if ltext.endswith(" ஆயிரம்"):
                    base = ltext[:-7]  # remove " ஆயிரம்"
                    return "%s ஆயிரத்தி %s" % (base, rtext), lnum + rnum
                else:
                    return "%s ஆயிரத்தி %s" % (ltext, rtext), lnum + rnum
            else:
                return "%s %s" % (ltext, rtext), lnum + rnum
        # Default case: add the numbers
        return "%s %s" % (ltext, rtext), lnum + rnum

    def to_ordinal(self, value):
        """Convert number to ordinal form"""
        # Check for irregular ordinals first
        if value in self._irregular_ordinals:
            return self._irregular_ordinals[value]
        
        # For regular ordinals, get cardinal and add "ஆம்" suffix
        # But we need to handle Tamil phonetic rules for joining
        cardinal = self.to_cardinal(value)
        
        # If cardinal ends with certain consonants, we need to modify the ending
        if cardinal.endswith('ு'):  # ends with 'u' sound
            return cardinal[:-1] + 'ாம்'
        else:
            return cardinal + 'ஆம்'

    def to_ordinal_num(self, value):
        """Convert number to ordinal numeric form"""
        self.verify_ordinal(value)
        return "%dம்" % value