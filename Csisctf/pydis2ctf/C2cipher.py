3           0 LOAD_CONST               1 ('S')
              2 STORE_FAST               1 (xorKey)       # xorKey = 'S'

  4           4 LOAD_GLOBAL              0 (len)
              6 LOAD_FAST                0 (inpString)
              8 CALL_FUNCTION            1
             10 STORE_FAST               2 (length)       # length = len(inpString)

  5          12 LOAD_GLOBAL              1 (range)
             14 LOAD_FAST                2 (length)
             16 CALL_FUNCTION            1                 ## range(length)
             18 GET_ITER
        >>   20 FOR_ITER                56 (to 78)
             22 STORE_FAST               3 (i)             # for i in range(length)

  6          24 LOAD_FAST                0 (inpString)
             26 LOAD_CONST               0 (None)
             28 LOAD_FAST                3 (i)
             30 BUILD_SLICE              2                 
             32 BINARY_SUBSCR                              ## inpString[None:i] ??? maybe
             34 LOAD_GLOBAL              2 (chr)
             36 LOAD_GLOBAL              3 (ord)
             38 LOAD_FAST                0 (inpString)
             40 LOAD_FAST                3 (i)
             42 BINARY_SUBSCR                              
             44 CALL_FUNCTION            1                 ## ord(inpString[i])
             46 LOAD_GLOBAL              3 (ord)
             48 LOAD_FAST                1 (xorKey)
             50 CALL_FUNCTION            1                 ## ord(xorKey)
             52 BINARY_XOR                                 ## ord(inpString[i]) ^ ord(xorKey)
             54 CALL_FUNCTION            1                 ## chr(ord(inpString[i]) ^ ord(xorKey))
             56 BINARY_ADD                                 ## inpString[None:i] + chr(ord(inpString[i]) ^ ord(xorKey))
             58 LOAD_FAST                0 (inpString)     
             60 LOAD_FAST                3 (i)
             62 LOAD_CONST               2 (1)
             64 BINARY_ADD                                 ## i+1
             66 LOAD_CONST               0 (None)
             68 BUILD_SLICE              2                 
             70 BINARY_SUBSCR                              ## inpString[i+1:None]
             72 BINARY_ADD                                 ## inpString[None:i] + chr(ord(inpString[i]) ^ ord(xorKey)) + inpString[i+1:None]
             74 STORE_FAST               0 (inpString)     # inpString = inpString[None:i] + chr(ord(inpString[i]) ^ ord(xorKey)) + inpString[i+1:None]
             76 JUMP_ABSOLUTE           20

  9     >>   78 LOAD_FAST                0 (inpString)
             80 RETURN_VALUE
