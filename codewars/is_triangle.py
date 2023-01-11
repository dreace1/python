def is_triangle(a, b, c):
    if a > 0 & b > 0 & c > 0:
        return c < a + b and a < b + c and b < c + a 
    return False