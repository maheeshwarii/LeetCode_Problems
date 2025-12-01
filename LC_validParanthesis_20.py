def validParanthesis(s):
    st = []
    mapi = {')':'(', ']':'[', '}':'{'}
    for i in s:
        if i in mapi:
            if st: top = st.pop()
            else: top ='#'
            if mapi[i] !=top: return False
        else: st.append(i)
    return not st

#main
s = input("Enter string of paranthesis:")
print(validParanthesis(s))