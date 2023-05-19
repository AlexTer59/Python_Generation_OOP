class QuadraticPolynomial:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        if self.b ** 2 - 4 * self.a * self.c < 0:
            return None
        else:
            return (-self.b - (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)

    @property
    def x2(self):
        if self.b ** 2 - 4 * self.a * self.c < 0:
            return None
        else:
            return (-self.b + (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)

    @property
    def view(self):
        res = []
        for i in (self.b, self.c):
            if i >= 0:
                res.append(f'+ {i}')
            else:
                res.append(f'- {abs(i)}')
        if self.a >= 0:
            return '{}x^2 {}x {}'.format(self.a, *res)
        else:
            return '{}x^2 {}x {}'.format(self.a, *res)

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, coefficients):
        self.a, self.b, self.c = coefficients

polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

# 500 -601 101
# 0.202
# 1.0
# (500, -601, 101)
# 500x^2 - 601x + 101
#
# -1000 1202 -202
# 1.0
# 0.202
# (-1000, 1202, -202)
# -1000x^2 + 1202x - 202

