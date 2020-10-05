# Goat (200)

Goat was in the Revering category for 200 points.

In this challenge we got only one file named **CrackMe.class**, which is a java class (compiled) file.

The first step would be to use some type of decompiler. I used [JD-GUI](https://java-decompiler.github.io/) to decompile it, but it failed to decompile without giving any errors.

Then I looked online for another decompiler and [Decompiler.com](http://www.decompiler.com/) popped up which was really good as we can just view the decompiled code online.

I copied the decompiled code in the [decompiled.java](https://github.com/DaBaddest/CTF-Writeups/blob/master/b01lers%20bootcamp%20CTF/Goat/decompiled.java) file.

The decompiled code is as follows
```
import java.util.Random;
import java.util.Scanner;

public class CrackMe {
   public static void main(String[] var0) {
      Scanner var1 = new Scanner(System.in);
      System.out.println("What is the flag?");
      String var2 = var1.nextLine();
      if (var2.length() != 22) {
         System.out.println("Not the flag :(");
      } else {
         char[] var3 = new char[var2.length()];

         int var4;
         for(var4 = 0; var4 < var2.length(); ++var4) {
            var3[var4] = var2.charAt(var4);
         }

         for(var4 = 0; var4 < var2.length() / 2; ++var4) {
            char var5 = var3[var2.length() - var4 - 1];
            var3[var2.length() - var4 - 1] = var3[var4];
            var3[var4] = var5;
         }

         int[] var10 = new int[]{19, 17, 15, 6, 9, 4, 18, 8, 16, 13, 21, 11, 7, 0, 12, 3, 5, 2, 20, 14, 10, 1};
         int[] var11 = new int[var3.length];

         for(int var6 = var10.length - 1; var6 >= 0; --var6) {
            var11[var6] = var3[var10[var6]];
         }

         Random var12 = new Random();
         var12.setSeed(431289L);
         int[] var7 = new int[var2.length()];

         for(int var8 = 0; var8 < var2.length(); ++var8) {
            var7[var8] = var11[var8] ^ var12.nextInt(var8 + 1);
         }

         String var13 = "";

         for(int var9 = 0; var9 < var7.length; ++var9) {
            var13 = var13 + var7[var9] + ".";
         }

         if (var13.equals("97.122.54.50.93.66.99.117.75.51.101.78.104.119.90.53.94.36.102.84.40.69.")) {
            System.out.println("Congrats! You got the flag!");
         } else {
            System.out.println("Not the flag :(");
         }

      }
   }
}
```

Lets reverse it step-by-step because the code is a little obfuscated.

1. First in this part of code, it initializes a input variable **var1** and asks for the flag & then checks if the lenght of input is equal to 22 else it exits.

```
Scanner var1 = new Scanner(System.in);
System.out.println("What is the flag?");
String var2 = var1.nextLine();
if (var2.length() != 22) {
   System.out.println("Not the flag :(");
```


2. In this part it is creating a new array **var3** of length as same as lenght of input (22) and just copies our input into **var3**
```
char[] var3 = new char[var2.length()];

int var4;
for(var4 = 0; var4 < var2.length(); ++var4) {
   var3[var4] = var2.charAt(var4);
}
```


3. This part is rather simple. It just reverses the array, in **python** we just do it with the slicing operator ```[::-1]```

```
for(var4 = 0; var4 < var2.length() / 2; ++var4) {
   char var5 = var3[var2.length() - var4 - 1];
   var3[var2.length() - var4 - 1] = var3[var4];
   var3[var4] = var5;
}
```


4. Now we have an array **var10** which contains some constants ranging from 0 to 21, which is the length of the flag, then it creates a new array **var11** of size 22 and then according to the constants in var10 it maps var3 into var11, i.e. it just transposes the string.
```
int[] var10 = new int[]{19, 17, 15, 6, 9, 4, 18, 8, 16, 13, 21, 11, 7, 0, 12, 3, 5, 2, 20, 14, 10, 1};
int[] var11 = new int[var3.length];

for(int var6 = var10.length - 1; var6 >= 0; --var6) {
   var11[var6] = var3[var10[var6]];
}
```


5. In the next step it initializes a constant seed for PRNG (pseudo-random number generator)
and generates 22 random integers and does XOR with elements of var11 and stores it into new array **var7**.
```
Random var12 = new Random();
var12.setSeed(431289L);
int[] var7 = new int[var2.length()];

for(int var8 = 0; var8 < var2.length(); ++var8) {
   var7[var8] = var11[var8] ^ var12.nextInt(var8 + 1);
}
```


6. Finally it then adds a dot(.) after each of the array elements and checks the **var13** with the string ```97.122.54.50.93.66.99.117.75.51.101.78.104.119.90.53.94.36.102.84.40.69.``` & if its equal it says correct or now
```
String var13 = "";

for(int var9 = 0; var9 < var7.length; ++var9) {
   var13 = var13 + var7[var9] + ".";
}

if (var13.equals("97.122.54.50.93.66.99.117.75.51.101.78.104.119.90.53.94.36.102.84.40.69.")) {
   System.out.println("Congrats! You got the flag!");
} else {
   System.out.println("Not the flag :(");
}
```

---

Now we have understood the whole program now we have to do all the thing but in reverse order.

I generally program in python, because of its simplicity, but lets reverse it in Javascript just for a change.

The steps we would perform are:

* Remove the dots(.) and store the values in the array
* Write a java program and set the seed to the constant value given and get the random numbers
* XORing the final values with the randoms we just got
* Performing the mapping in reverse order
* Reversing the array
* Printing the char values based on the ascii values we got after doing all these operations

The whole solution js script is given below
```
//1. Remove the dots(.) and store the values in the array
final = [97,122,54,50,93,66,99,117,75,51,101,78,104,119,90,53,94,36,102,84,40,69];

//2. Write a java program and set the seed to the constant value given and get the random numbers
randoms = [0,1,2,1,2,5,4,1,1,7,3,7,0,10,5,5,1,16,10,2,12,17];

//3. XORing the final values with the randoms we just got
ll=[];
for(i=0;i<final.length;++i){
  ll.push(final[i]^randoms[i]);
}

//4. Performing the mapping in reverse order
mappings = [19, 17, 15, 6, 9, 4, 18, 8, 16, 13, 21, 11, 7, 0, 12, 3, 5, 2, 20, 14, 10, 1];

l = [];
for(i=0;i<mappings.length;++i){
  l[mappings[i]] = ll[i];
}

//5. Reversing the array
l.reverse()

//6. Printing the char values based on the ascii values we got after doing all these operations
b = ''
for(x of l){
  b += String.fromCharCode(x);
}
console.log(b)
```

And there we have the flag
```
flag{J4V4_I$_th3_G04T}
```
