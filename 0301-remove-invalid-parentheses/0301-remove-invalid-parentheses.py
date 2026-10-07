class Solution:
    def removeInvalidParentheses(self, s: str):
        ans = set()
        maxLen = 0

        def solve(i, count, cur):
            nonlocal maxLen

            # Invalid prefix
            if count < 0:
                return

            # End of string
            if i == len(s):
                if count == 0:
                    if len(cur) > maxLen:
                        ans.clear()
                        maxLen = len(cur)
                        ans.add(cur)

                    elif len(cur) == maxLen:
                        ans.add(cur)
                return

            # Current character is '('
            if s[i] == "(":
                # Remove
                solve(i + 1, count, cur)

                # Keep
                solve(i + 1, count + 1, cur + "(")

            # Current character is ')'
            elif s[i] == ")":
                # Remove
                solve(i + 1, count, cur)

                # Keep
                solve(i + 1, count - 1, cur + ")")

            # Normal character
            else:
                solve(i + 1, count, cur + s[i])

        solve(0, 0, "")

        return list(ans)