class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        cnt = 0
        for d in data:
            if cnt == 0:
                if (d >> 5) == 0b110:
                    cnt = 1
                elif (d >> 4) == 0b1110:
                    cnt = 2
                elif (d >> 3) == 0b11110:
                    cnt = 3
                elif (d >> 7) == 1:
                    return False
            else:
                if (d >> 6) != 0b10:
                    return False
                cnt -= 1
        return cnt == 0
