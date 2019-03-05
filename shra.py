import random
l=["rock","paper","scissor"]
us=0
cs=0
while True:
	u=input("enter your choice,press n to discontinue")
	if u=='n':
		print ("Game over")
		exit()
	c=random.choice(l)
	print("computer chooses",c)
	if u==c:
		print("tie")
	elif u=="rock" and c=="paper":
		print("comp wins")
		cs=cs+1
		print(cs)
	elif u == "rock" and c =="scissor":
		print ("user wins")
		us=us+1
		print(us)
	elif u=="scissor" and c=="rock":
		print("comp wins")
		cs=cs+1
		print(cs)
	elif u == "paper" and c=="scissor":
		print ("comp wins")
		cs=cs+1
		print(cs)
	elif u == "scissor" and c =="paper":
		print ("user wins")
		us=us+1
		print(us)
	if	us>cs:
		print(us)
		print("user wins")
	elif cs > us:
		print(cs)
		print("comp wins")
	
