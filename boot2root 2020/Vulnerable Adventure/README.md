# Vulnerable Adventure

A misc challenge which simulates kind-of a game.

We get a file **client.py** which connects to a server & starts the game.

Some things to note from the file:
1. There is a possibility that it uses **python2** because there are no paranthesis around print, so there is a possibility of command injection.
```
while(1 == 1):
  print "Welcome to game"
  print "What would you like to do?"
```

2. There is some dummyflag varible which is unset, and only sets when we guess a random value.
```
dummyflag = 0
vuln = random.randint(1,500)
choice = input("Enter your choice : ")
if choice == vuln:
  dummyflag = 1
```

When we run the program, we are greeted with options, which gives idea on how to play the game

When we choose option 1 *1. Speak to goblin in front of you(2 energy)*, it says
```
Go to position (9,9). A flag awaits for you!
```
So we have to traverse to that specific location using the options, but there is a problem that we have specific amount of energy and it is not possible to traverse to that location with the specified amount of energy.

Going back to our assumption that there is a command injection, but when we try that, the command runs on our local machine and not on the server, so that idea failed but that gave me another idea that the settings are taken from our machine, so we control the parameters.

Remember the goblin gives us the coordinates to the flag (9, 9), so we can just set the variables posx & posy both to 9 and the run the program which gives us our first flag.
```
b00t2root{p4ck3t_inj3ct}
```
# Vulnerable Adventure 2
Description: *Oh no! A vulnerability!(Use previous client)*

We have to use the same code from before.

Remembered the second assumption  *There is some dummyflag varible which is unset, and only sets when we guess a random value.*

Cause we control the varibles at the start, we can just set the dummyflag to 1 and run the program which gives out the second flag
```
b00t2root{python2_vuln}
```

Another solution could be to just change this line from this
```
vuln = random.randint(1,500)
```
to this
```
vuln = random.randint(1,1)
```
Which will always set the vuln variable to 1

And when asked for choice send 1 which will also give the flag.
