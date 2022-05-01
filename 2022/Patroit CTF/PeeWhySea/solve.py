arg = bytes.fromhex('110117023e3273237a157f133d372c2d')
key = b'ABCDEFGHIJKLMNOP'

flag = ''.join([format(f'{a ^ b:02x}') for a, b in zip(arg, key)])

print(bytes.fromhex(flag))
