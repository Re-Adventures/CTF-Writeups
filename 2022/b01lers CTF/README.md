# extreme_64_part_2

* This was in `b01lers CTF` in the reversing category, but it is actually a x86_64 assembly programming challenge

## Stage 1
* Problem: *Add rdi to rsi and store the result in rax using only one instruction.*

* Solution
```asm
lea  rax, [rdi + rsi]
```

* Code: `code{some_instructions_have_many_uses}`

## Stage 2
* Problem: *Print the string 'hackerman' to stdout.*

* Solution
```asm
mov  rax, 0x6e ;n
push rax
mov  rax, 0x616d72656b636168 ;hackerma
push rax  ;storing the string on the stack

; write(1(stdout), rsp(string), 9(length))
mov  rax, 1   ;sys_write
mov  rdi, 1   ;stdout
mov  rsi, rsp ;string pointer
mov  rdx, 9   ;length
syscall
```
* Code: `code{asm_c4n_d0_anything_java_can_do}`

## Stage 3

* Problem: `Register rsi contains a pointer to the flag, but the  flag has been encoded by XOR-ing each byte with 0x82.  Decode it and print it out to complete the challenge! Hint: the flag is 32 characters long...`

* Solution
The code golfed(shortest, probably) solution, which is **24 bytes** in size. It is not obscure but still have fun reading it 
```asm
push rsi
pop  rdi
push rdi
push 32
pop  rcx
push rcx
pop  rdx
xor  eax, eax
label:
lodsb
xor  al, 0x82
stosb
loop label
push 1
pop  rax
mov  edi, eax
pop  rsi
syscall
```

* Code: `code{did_you_get_the_flag?}`

* Flag: `bctf{c0ngrats_y0u_are_a_pr0!!!!}`
