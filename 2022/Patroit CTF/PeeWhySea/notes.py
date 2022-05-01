import dis
import marshal

with open('flag-checker.pyc', 'rb') as fp:
  data = fp.read()

M = marshal.loads(data[16:])

dis.dis(M)

