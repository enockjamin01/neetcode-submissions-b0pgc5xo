class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for token in tokens:
            if token in "/-+*":
                a=st.pop()
                b=st.pop()
                a,b=b,a
                if token=="+":
                    st.append(a+b)
                elif token=="-":
                    st.append(a-b)
                elif token=="*":
                    st.append(a*b)
                elif token=="/":
                    st.append(int(a/b))
            else:
                st.append(int(token))
        return st.pop()