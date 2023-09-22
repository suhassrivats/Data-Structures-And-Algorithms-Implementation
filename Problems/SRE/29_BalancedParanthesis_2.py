def balanced_paranthesis(s):

    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '[',
        '>': '<'
    }
    # Open brackets stack
    stack = []

    for char in s:
        # Open brackets
        if char in bracket_map.values():
            stack.append(char)
        # Closed brackets
        elif char in bracket_map.keys():
            # Value of bracket_map[char] is an open bracket. Compare it
            # with popped open_bracket from the stack
            if not stack or bracket_map[char] != stack.pop():
                print('False')
                return False
    print(stack == [])
    return stack == []

# Input
# True
s = "[abc(def)gh{i}j]"
balanced_paranthesis(s)
# False
s = "[abcdef"
balanced_paranthesis(s)