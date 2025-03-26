
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine 
if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
"""
def validparentheses(s):
    stk = []
    mapping = {
        '(':')',
        '{':'}',
        '[':']'
    }

    for i in s:
        if i in mapping.keys():
            stk.append(i)
        elif i in mapping.values() and stk:
            prev = stk.pop()
            if mapping[prev]!=i:
                return False
            else:
                return True
        else:
            return False

s = "{}"
print(validparentheses(s))
s1 = "[]()"
print(validparentheses(s1))
s2 = "[{(})]"
print(validparentheses(s2))