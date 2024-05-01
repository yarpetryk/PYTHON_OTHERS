from decimal import Decimal

value = 10.500000
x = str(value)
y = f"{value: .2f}"

without_trailing_zeros = x.rstrip(
    '0').rstrip('.') if '.' in x else x

z = Decimal(without_trailing_zeros)
print(x, y, z)
