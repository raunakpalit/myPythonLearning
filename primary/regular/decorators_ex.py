def make_it_lower(func):
    def inner2(*args):
        b = func(*args)
        return b.lower()
    return inner2


def make_it_upper(func):
    def inner1(*args):
        a = func(*args)
        return a.upper()
    return inner1

@make_it_lower
@make_it_upper
def print_a_string(ustr, ustr2):
    return ustr + " "+ ustr2

print(print_a_string('raunak', 'palit'))
