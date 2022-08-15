class Solution:
    def intToRoman(self, num: int) -> str:
        roman_rank = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        size_rank = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanised = ""
        for roman, size in zip(roman_rank, size_rank):
            while num >= size:
                num -= size
                romanised += roman
        return romanised
