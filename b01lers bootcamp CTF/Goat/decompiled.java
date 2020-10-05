// This code is modified a little while reversing it
import java.util.Random;
import java.util.Scanner;

public class CrackMe {
   public static void main(String[] var0) {
      Scanner var1 = new Scanner(System.in); // var1= input
      System.out.println("What is the flag?");
      String var2 = var1.nextLine();           // copying input into var2
      if (var2.length() != 22) {
         System.out.println("Not the flag :(");
      } else {
         char[] var3 = new char[var2.length()];

         int var4;
         for(var4 = 0; var4 < 22; ++var4) {
            var3[var4] = var2.charAt(var4);            //copying input into var3
         }

         for(var4 = 0; var4 < 11; ++var4) {           // swapping array elements
            char temp = var3[22 - var4 - 1];           
            var3[22 - var4 - 1] = var3[var4];
            var3[var4] = temp;
         }

         int[] var10 = new int[]{19, 17, 15, 6, 9, 4, 18, 8, 16, 13, 21, 11, 7, 0, 12, 3, 5, 2, 20, 14, 10, 1};  //mappings
         int[] var11 = new int[22];

         for(int var6 = 22 - 1; var6 >= 0; --var6) {  // shuffle
            var11[var6] = var3[var10[var6]];
         }              //flag[mapping[iterator]]

         Random var12 = new Random();
         var12.setSeed(431289L);
         int[] var7 = new int[22];

         for(int var8 = 0; var8 < 22; ++var8) {
            var7[var8] = var11[var8] ^ var12.nextInt(var8 + 1);   // xor with random values
         }                             //returns random value between 0 and passed argument

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
