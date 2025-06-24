def validate_bracket(n):
    br_form = {")": "(", "]": "[", "}": "{"}
    op_br = [] # [{]
    for i in n:
        if i in br_form.values():
            op_br.append(i)
        elif i in br_form.keys():
            if not op_br or op_br.pop() != br_form[i]:
                return False
    
    return len(op_br) == 0



print(validate_bracket("()"))
print(validate_bracket("()[]{}"))
print(validate_bracket("{}[]()"))
print(validate_bracket("{{[([])]}}"))
print(validate_bracket("{{}()})[[]}"))
print(validate_bracket("[{)(}]}"))
print(validate_bracket("{[(])}"))
print(validate_bracket("{[}"))
