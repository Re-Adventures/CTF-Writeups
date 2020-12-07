# endless_wait

Reverse engineering challenge

We got a file named endless_wait which is 64-bit ELF file, and it is stripped
```
endless_wait; ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 3.2.0, stripped
```

Opening the file on binary ninja and performing static analysis

In the main function, clearly we see something intresting
```
mov     ecx, 0x0
mov     edx, 0x1
mov     esi, 0x0
mov     edi, 0x0
mov     eax, 0x0
call    ptrace
test    rax, rax
jns     0x173c
```
which is **ptrace**

According to man
*The ptrace() system call provides a means by which one process (the "tracer") may observe and control the execution of another process (the "tracee")*

Basically, ptrace is a syscall, which is used for debugging of processes. GDB uses ptrace internally to debug programs. This is a basic Anti-RE technique

Which means that if we do dynamic analysis, the program takes a different path, instead of the intended one.

One can simply patch out the bytes to make it go in the intended path, but we are doing static analysis so no need.

Following the intended path

Then the following part takes string upto a \n
```
mov     rax, qword [rbp-0xc8 {var_d0}]
lea     rsi, [rel data_2004]          ; 0A 00
mov     rdi, rax
mov     eax, 0x0
call    strtok
```

We see some more strings
```
"bqz0wm0qctdn2gbrdmoazosbtsc{jmpgzadbtjc1amenzngbcnceam_gn1dzsab_ccnhm0nntlx_ackebehmyvn_lzhabencrhmevn}azqazwsxedc"
```

Then a loop for 35 times, which can be a hint that the flag is of length 34.

It loads every third byte from the above string and calls strcmp, compares it with our input.

So we can just grab every third character from that string and it might be our flag.

I wrote a short python script to do that
```
ss = "bqz0wm0qctdn2gbrdmoazosbtsc{jmpgzadbtjc1amenzngbcnceam_gn1dzsab_ccnhm0nntlx_ackebehmyvn_lzhabencrhmevn}azqazwsxedc"
o = ''
for i in range(35):
  o += ss[3*i]
print(o)
```
And indeed it gives out the flag
```
b00t2root{pat1ence_1s_n0t_key_here}
```
P.S. I got First Blood on it 🩸
