class Solution:
    def isValid(self, s: str) -> bool:
        open_b =  "({[" 
        closed_b = "]})"
        st = []
        for i in s:
            # open brackets go into the stack
            if i in open_b:
                st.append(i)
            else:    # when a close bracket is encountered
                if not st: #if stack is empty, sequence is invalid
                    return False
                else:
                    # check if stack top is corresponding open bracket for this close bracket
                    if  i == ")"  and st[-1] == "(" or i == "]" and st[-1] == "[" or i == "}" and st[-1] == "{":
                        st.pop()
                    else:
                        return False
        return not st