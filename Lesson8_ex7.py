"""  Способ I """


class Complex1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

    def __mul__(self, other):
        return self.val * other.val


objComplex_1 = Complex1(2 + 11j)
objComplex_2 = Complex1(4 - 1j)
print(objComplex_1 + objComplex_2)
print(objComplex_1 * objComplex_2)

""" Способ II  """


class Complex2:
    def __init__(self, Rez, Imz):
        self.Rez = Rez
        self.Imz = Imz

    @staticmethod
    def comp(num):
        Rez1 = '-' if num[0] == '-' else ''
        num = num[1:] if num[0] in ['-', '+'] else num
        for i in range(len(num)):
            if num[i] in '0123456789':
                Rez1 += num[i]
            else:
                num = num[i:]
                break
        return Rez1, num

    def __str__(self):
        return f'{self.Rez}{self.Imz}i'

    def __add__(self, other):
        return Complex2(self.Rez + other.Rez, self.Imz + other.Imz)

    def __mul__(self, other):
        return Complex2(self.Rez * other.Rez - self.Imz * other.Imz, self.Rez * other.Imz + self.Imz * other.Rez)


num1 = '-4-11i'
num2 = '2+5i'

objComplex1 = Complex2(int(Complex2.comp(num1)[0]), int(Complex2.comp(Complex2.comp(num1)[1])[0]))
objComplex2 = Complex2(int(Complex2.comp(num2)[0]), int(Complex2.comp(Complex2.comp(num2)[1])[0]))
print(objComplex1 + objComplex2)
print(objComplex1 * objComplex2)
