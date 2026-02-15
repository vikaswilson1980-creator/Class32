class RomanNumeral:
    def __init__(self, number: int):
        if not (1 <= number <= 3999):
            raise ValueError("Number must be between 1 and 3999")
        self.number = number

    def to_roman(self) -> str:
        value_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (8, "VIII"),
            (7, "VII"),
            (6, "VI"),
            (5, "V"),
            (4, "IV"),
            (3, "III"),
            (2, "II"),
            (1, "I"),
        ]

        num = self.number
        roman = ""

        for value, symbol in value_map:
            while num >= value:
                roman += symbol
                num -= value

        return roman
converter = RomanNumeral(1994)
print(converter.to_roman())  
