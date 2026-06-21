class Solution:

    def break_down_into_forms(self, num: int) -> list[int]:
        """
        Break down the given 4 digit int into thousands, hundreds, tens and unit form.
        """
        forms = []
        for i in range(4, 0, -1):
            mod_reduce_factor = pow(10, i)
            divisor_factor = mod_reduce_factor / 10
            forms.append([
                int((num % mod_reduce_factor) // divisor_factor),
                i
            ])

        return forms

    def convert_form_to_roman(self, num: int, factor: int) -> str:
        """
        Given a number and the factor - convert it into roman form.
        num: the int which is to be converted.
        factor: the power of 10, eg. for thousands, hundreds, tens, units, this will be 4, 3, 2, 1
        """
        conversion_map = {
            4: {
                1: 'M',
                2: 'MM',
                3: 'MMM',
                0: ''
            },
            3: {
                1: 'C',
                2: 'CC',
                3: 'CCC',
                4: 'CD',
                5: 'D',
                6: 'DC',
                7: 'DCC',
                8: 'DCCC',
                9: 'CM',
                0: ''
            },
            2: {
                1: 'X',
                2: 'XX',
                3: 'XXX',
                4: 'XL',
                5: 'L',
                6: 'LX',
                7: 'LXX',
                8: 'LXXX',
                9: 'XC',
                0: ''
            },
            1: {
                1: 'I',
                2: 'II',
                3: 'III',
                4: 'IV',
                5: 'V',
                6: 'VI',
                7: 'VII',
                8: 'VIII',
                9: 'IX',
                0: ''
            }
        }
        try:
            return conversion_map[factor][num]
        except Exception as e:
            print(f"Num: {num}, factor: {factor}")


    def intToRoman(self, num: int) -> str:
        """
        Constraint: numbers are less than 3999
        Strategy:
          - Divide into thousands, hundreds, tens and units
          - Convert each and append
        """
        forms = self.break_down_into_forms(num)
        roman_forms = []
        for n, f in forms:
            roman_forms.append(self.convert_form_to_roman(n, f))

        return ''.join(roman_forms)
