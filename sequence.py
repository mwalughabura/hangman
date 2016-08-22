import random

choose = "yes"
while choose == "yes":
	trys = 0
	while trys < 7:
		words = ["the", "quick", "brown", "fox", "jumped", "over", "lazy", "dogs"]
		raw_input()
		removed = random.choice(words)
		print removed
		words.remove(removed)
		trys += 1
	choose = raw_input("Do you want to play again?")
	if choose != "yes":
		print "Bye"
