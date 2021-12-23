import math as m

def log(a, b):
    '''Logarythm of a to base b'''
    if a < 0 or b < 0:
        raise ValueError('Expected positive, got negative')
    return m.log(a, b)

def ln(a):
    '''Natural logarythm of a'''
    return log(a, m.e)

def lg(a):
    '''Base 10 logarythm of a'''
    return log(a, 10)

__all__ = ['log', 'ln', 'lg']