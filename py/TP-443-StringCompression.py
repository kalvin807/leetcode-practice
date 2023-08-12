class Solution:
    def compress(self, chars: List[str]) -> int:
        write_at = 0
        read_at = 0
        while read_at < len(chars):
            c, cnt = chars[read_at], 1
            while read_at + 1 < len(chars) and chars[read_at] == chars[read_at + 1]:
                cnt += 1
                read_at += 1

            chars[write_at] = c
            if cnt > 1:
                for n_c in str(cnt):
                    write_at += 1
                    chars[write_at] = n_c
            read_at += 1
            write_at += 1
        return write_at


# Time complexity = O(n)
# Space complexity = O(1)
