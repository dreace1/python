def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return c < a + b and a < b + c and b < c + a 
    return False