def rule (input):
    key=input.split()
    alphabet=False
    for c in key:
        if c.isalpha():
            alphabet = True
        else:
            alphabet = False
    return alphabet
