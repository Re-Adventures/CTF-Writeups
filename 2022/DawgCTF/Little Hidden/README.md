# Little Hidden

* A 250 point reversing challenge from DawgCTF

## Basic Recon

* After decompressing the file, & running it through `rabin2` we found out that it is a 32bit PE file
```
arch     x86
bintype  pe
bits     32
```

## Analyzing the binary

* Opening the file in ida & jumping to main @ 0x04014E0 we dont see much, but two instructions, which I initially thought were regular instructions.

```asm
push    offset stru_403590
push    offset SEH_4014E0
```

* So first it pushes the address of some structure & then pushes the address to some SEH (Structured Exception Handling)

* I dont have much idea about SEH but basically it is used for exception handling purposes, the `try-catch` block in c++. 

* Looking at the structure, which IDA has nicely parsed
```asm
.rdata:00403590 stru_403590     dd 0FFFFFFFEh           ; GSCookieOffset
.rdata:00403590                                         ; DATA XREF: sub_4014E0+5↑o
.rdata:00403590                 dd 0                    ; GSCookieXOROffset ; SEH scope table for function 4014E0
.rdata:00403590                 dd 0FFFFFFD8h           ; EHCookieOffset
.rdata:00403590                 dd 0                    ; EHCookieXOROffset
.rdata:00403590                 dd 0FFFFFFFEh           ; ScopeRecord.EnclosingLevel
.rdata:00403590                 dd offset loc_401557    ; ScopeRecord.FilterFunc
.rdata:00403590                 dd offset loc_40155D    ; ScopeRecord.HandlerFunc
```

* After reading about SEH, I found out that **ScopeRecord.HandlerFunc** is called when an execption occurs.


* Getting back to main & analysing it more, we some peculiar set of instructions
```asm
xor     ecx, ecx
div     ecx
```

* It is basically a division by zero, which will obviously call the execption hander **loc_40155D** which just calls the **sub_401410**.

* The sub_401410 does a lot of SSE operations to zero out an array & passes that array into a function
```asm
lea     eax, [ebp-30h]
movaps  xmmword ptr [ebp-30h], xmm0
push    esi
push    eax
movq    qword ptr [ebp-20h], xmm0
mov     dword ptr [ebp-18h], 0
mov     byte ptr [ebp-14h], 0
call    sub_4013C0
```

* Analysing **sub_4013C0**, we see that it internally calls 5 functions with the array as argument & all of the functions were just performing some basic arithmetic operations & places the result at specifix indices of the array.

* From here we can extract the values by hand, but I just used the `binary ninja's` decompiler to do that work for me, but we have to adjust some parameters

* The deompilation of one of function looks like the following:

*Before*
```c
*(int8_t*)((char*)arg1 + 0xb) = 0x98;
*(int8_t*)((char*)arg1 + 0x1b) = 0x98;
*(int8_t*)((char*)arg1 + 0x11) = 0xa0;
*(int8_t*)((char*)arg1 + 0x11) = (*(int8_t*)((char*)arg1 + 0x11) - 1);
*(int8_t*)((char*)arg1 + 0x12) = 0x99;
*(int8_t*)((char*)arg1 + 0x12) = (*(int8_t*)((char*)arg1 + 0x12) + 2);
return ((char*)arg1 + 0x11);
```

* It is ok, but we can improve it by setting the type of array to be an `uint8_t*`

*After*
```c
arg1[0xb] = 0x98;
arg1[0x1b] = 0x98;
arg1[0x11] = 0xa0;
arg1[0x11] = (arg1[0x11] - 1);
arg1[0x12] = 0x99;
arg1[0x12] = (arg1[0x12] + 2);
return &arg1[0x11];
```

* After initializing the array, it does memset & some other stuff, but one instruction caught my attention which was inside of a loop, & eax is also pointing to the buffer
```asm
xor     byte [eax], 0xab
```

## Solution

* Now we know that all the function is doing is initialize the array & xor it with `0xab`, so we can just copy all the expressions from binary ninja & xor them with 0xab to get the flag

```js
'use strict';
var buf = new Array();

buf[0x15] = 0xe6;
buf[0x17] = 0xe7;
buf[4] = 0xe8;
buf[3] = 0xec;
buf[1] = 0xea;
buf[0x16] = (buf[1] + 1);
buf[6] = 0xed;
buf[0] = 0xf0-1;

buf[0x14] = 0xf4;
buf[0xf] = 0xf4;
buf[0xd] = 0xf9;
buf[5] = 0xff;
buf[9] = 0xf4;
buf[2] = 0xfc;

buf[7] = 0xd0;
buf[0x18] = 0xdc;
buf[0x1a] = 0xd9;
buf[0x1c] = 0xd8;
buf[0x1c] = (buf[0x1c] - 2);

buf[8] = 0xc2;
buf[0xa] = 0xc7;
buf[0xc] = 0xca;
buf[0xe] = (buf[0xc] - 5);
buf[0x10] = 0xcd;
buf[0x13] = 0xc6;
buf[0x19] = 0xca;

buf[0xb] = 0x98;
buf[0x1b] = 0x98;
buf[0x11] = 0xa0;
buf[0x11] = (buf[0x11] - 1);
buf[0x12] = 0x99;
buf[0x12] = (buf[0x12] + 2);

var s = "";
buf.forEach(v => {
  s += String.fromCharCode(v ^ 0xab);
})

console.log(s);
```

* Flag: `DAWGCTF{i_l3aRn_f40m_M@Lwar3}`


