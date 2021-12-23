_fac = lambda n: 1 if n == 0 else n* _fac(n-1)
e = sum([1/_fac(n) for n in range(20)])

def log(a, b):
    '''Logarithm of a to base b'''
    if a < 0 or b < 0:
        raise ValueError('Expected positive, got negative')
    if b == 1:
        raise ValueError('Base must not equal 1')
    def _(a, b): # written by myself
        res = 0
        counter = 0
        if a < b:
            return -_(b, a)
        if b == 1:
            return a
        if b < 1:
            return -_(a, 1/b)
        while a >= b:
            a /= b
            counter += 1
        res += counter
        if a == 1:
            return res
        return res + 1/_(b, a)
    return _(a, b)

def ln(a):
    '''Natural logarithm of a'''
    return log(a, e)

def lg(a):
    '''Base 10 logarithm of a'''
    return log(a, 10)

__all__ = ['log', 'ln', 'lg']
