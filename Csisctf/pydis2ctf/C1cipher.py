  2           0 LOAD_CONST               1 ('')
              2 STORE_FAST               1 (ret_text)     # ret_text = ''

  3           4 LOAD_GLOBAL              0 (list)
              6 LOAD_FAST                0 (text)         ## list(text)
              8 CALL_FUNCTION            1
             10 GET_ITER
        >>   12 FOR_ITER                42 (to 56)
             14 STORE_FAST               2 (i)            # for i in list(text):

  4          16 LOAD_FAST                0 (text)
             18 LOAD_METHOD              1 (count)
             20 LOAD_FAST                2 (i)
             22 CALL_METHOD              1
             24 STORE_FAST               3 (counter)      # counter = count(i)

  5          26 LOAD_FAST                1 (ret_text)
             28 LOAD_GLOBAL              2 (chr)
             30 LOAD_CONST               2 (2)           
             32 LOAD_GLOBAL              3 (ord)
             34 LOAD_FAST                2 (i)
             36 CALL_FUNCTION            1                ## ord(i) * 2
             38 BINARY_MULTIPLY
             40 LOAD_GLOBAL              4 (len)
             42 LOAD_FAST                0 (text)
             44 CALL_FUNCTION            1                ## len(text)
             46 BINARY_SUBTRACT                           ## (ord(i) * 2) - len(text)
             48 CALL_FUNCTION            1                ## chr((ord(i) * 2) - len(text))
             50 INPLACE_ADD
             52 STORE_FAST               1 (ret_text)     # ret_text += chr((ord(i) * 2) - len(text))
             54 JUMP_ABSOLUTE           12

  6     >>   56 LOAD_FAST                1 (ret_text)
             58 RETURN_VALUE
