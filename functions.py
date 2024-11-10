def get_int(prompt):
    n = ''
    while type(n) != int:
        try:
            n = int(input(prompt))
        except ValueError:
            continue

    return n


def get_float(prompt):
    f = ''
    while type(f) != float:
        try:
            f = float(input(prompt))
        except ValueError:
            continue
    
    return f


def get_these(element1, element2, prompt):
    t = None
    while t != element1.lower() and t != element2.lower():
        t = input(prompt).lower()

    return t


def get(element, prompt):
    t = None
    while t != element:
        t = input(prompt)
