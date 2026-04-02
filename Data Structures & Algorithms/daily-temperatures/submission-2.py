class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        st=[]
        for i in range(len(temperatures)):
            while st and temperatures[st[-1]]<temperatures[i]:
                temp_index=st.pop()
                result[temp_index]=i-temp_index
            st.append(i)
        return result



        