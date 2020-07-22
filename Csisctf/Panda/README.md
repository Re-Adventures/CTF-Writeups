# Panda

Panda was in the forensics category.

The files attached with it was a **panda.zip** file.

This zip was password protected, so i used [John The Ripper](https://www.openwall.com/john/) to crack it's password and used [this](https://crackstation.net/files/crackstation-human-only.txt.gz) password list.

The commands for the same is:
```
zip2john panda.zip > hash.txt
john.exe --wordlist=real_human hash.txt
```
which gives out the password **2611**

On unzipping the zip file with this password gives out two files **panda.jpg** and **panda1.jpg** which are of same size.

Both of them are similar images but on panda1, there is some manipulation done.

I wrote a python one-liner for it:
```
print(''.join([chr(i) for i, j in zip(open('panda1.jpg', 'rb').read(), open('panda.jpg', 'rb').read()) if i!= j]))
```

The above line just simply read single byte from both the files and if they are different then just print it's corresponding character

On running the one-liner it gives out the flag
```
csictf{kung_fu_p4nd4}
```
