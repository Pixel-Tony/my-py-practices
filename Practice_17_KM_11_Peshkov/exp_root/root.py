def root2(x):
    if x < 0:
        raise ValueError(f'Expected positive, got negative {x}')
    else:
        return x**(0.5)

def root3(x):
    return x**(1/3)

__all__ = ['root2', 'root3']