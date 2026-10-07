class Solution:
    def removeInvalidParentheses(self, s: str):
        st = set()
        n = len(s)
        maxLen = 0

        def solve(i, curr, count):
            nonlocal maxLen#bhai nonlocal katho outer ka value inner def me change kareja

            if count < 0:
                return

            if i == n:
                if count == 0:
                    if len(curr) > maxLen:
                        maxLen = len(curr)
                        st.clear()
                        st.add("".join(curr))

                    elif len(curr) == maxLen:
                        st.add("".join(curr))
                return

            if s[i] != '(' and s[i] != ')':
                curr.append(s[i])
                solve(i + 1, curr, count)
                curr.pop()
                return

            curr.append(s[i])# tree me rakh ne ke vaste 

            solve(
                i + 1,
                curr,
                count + (1 if s[i] == '(' else -1)
            )

            curr.pop()# tree me rakhiso nikal dalu

            solve(i + 1, curr, count)# use remove kar dalu

        solve(0, [], 0)

        return list(st)