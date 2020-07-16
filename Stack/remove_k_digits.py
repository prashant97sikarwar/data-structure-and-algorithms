class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(num)
        st = []
        st.append(num[0])
        i = 1
        while i < len(num):
            while st and k > 0 and num[i] < st[-1]:
                st.pop()
                k -= 1
            st.append(num[i])
            i += 1
        while k > 0:
            st.pop()
            k -= 1
        st = ''.join(st)
        return st.lstrip('0') if len(st) > 0  and int(st) != 0 else '0'