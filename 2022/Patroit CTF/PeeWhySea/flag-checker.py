import sys

if len(sys.argv) != 2:
  print('One argument required')
  sys.exit()

arg = sys.argv[1]
key = 'ABCDEFGHIJKLMNOP'

encode = ''.join([format(f'{ord(a) ^ ord(b):02x}') for a, b in zip(arg, key)])

if encode == '110117023e3273237a157f133d372c2d':
  print('You have the correct flag!')
else:
  print('Wrong flag')

