import random

d = 0
p = 0

while True :
	r = input("Press r to roll, q to quit : ")

	if r == 'r':
	  d = random.randint(1,6)
	  print("You got :",d)
	  if d ==6:
	       print("Congratulations,you can play now.")
	       break
	  else:
	       print("ROLL AGAIN, TILL YOU GET 6.")

while true:
	r = input("Press r to roll, q to quit :")

	if r =='r':
		d = random.randint(1,6)
		print("You got :",d)

	p =p+d
	if p>100:
		p= p-d
	print("wait till you get",100 p)

	print("Your new position is :",p)

	if p ==100;
	print("You won!")
	exit()
	if p =8:
	p =37
	print("Wow,a ladder.Go to ",p)

	if p =13:
	p =34
	print("Wow,a ladder.Go to",p)

	if p =40:
	p = 68
	print("WOW,a ladder.Go to",p)

	if p =52:
	p = 81
	print("Wow,a ladder.Go to",p)

	if p = 76:
		p =97

elif r =='q':
	print("bye!")
	exit()