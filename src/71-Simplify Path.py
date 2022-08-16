class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        ans = []
        for file in parts:
            if not file:
                continue
            elif file == ".":
                continue
            elif file == "..":
                if ans:
                    ans.pop()
            else:
                ans.append(file)

        return "/" + "/".join(ans)
