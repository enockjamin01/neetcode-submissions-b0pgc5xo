class Solution:
    def isValid(self, s: str) -> bool:
        dict={"}":"{","]":"[",")":"("}
        st=[]
        for c in s:
            if c in "[{(":
                st.append(c)
            else:
                if c in "]})":
                    if not st and c:
                        return False
                    if (st and not dict[c]==st.pop()):
                        return False
        if not st:
            return True
        else:
            return False