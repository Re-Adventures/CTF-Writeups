xorKey = 'S'
length = len(inpString)
for i in range(length):
  inpString = inpString[None:i] + chr(ord(inpString[i]) ^ ord(xorKey)) + inpString[i+1:None]
return inpString
