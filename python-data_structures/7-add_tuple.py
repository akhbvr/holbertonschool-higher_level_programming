#!/usr/bin/python3
def add_tuple(a: tuple, b: tuple) -> tuple:
    a1 = a[0] if len(a) > 0 else 0
    a2 = a[1] if len(a) > 1 else 0
    b1 = b[0] if len(b) > 0 else 0
    b2 = b[1] if len(b) > 1 else 0
    return (a1 + b1, a2 + b2)
