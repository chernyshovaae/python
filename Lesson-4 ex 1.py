import sys

print(f'з/п сотрудника: (выработка в часах * ставка в час) + премия = '
      f'{(int(sys.argv[1]) * int(sys.argv[2])) + int(sys.argv[3])}')
