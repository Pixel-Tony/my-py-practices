def fact(x):
    if int(x) != x:
        raise ValueError('Expected \'int\', got \'float\'')
    if x < 0:
        raise ValueError('Expected positive, got negative')
    if x == 0:
        return 1
    else:
        return x*fact(x-1)

__all__ = ['fact']