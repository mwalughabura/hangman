import random
prompt = ">> "
poll = """
  ______
 |
 |
 |
 |
 |
"""
rope = """
  ______
 |      |
 |
 |
 |
 |
"""
head = """
  ______
 |      |
 |      0
 |
 |
 |
"""
frontLimbs = """
  ______
 |      |
 |      0
 |     / \\
 |
 |
"""
body= """
  ______
 |      |
 |      0
 |     /|\\
 |
 |
"""
full = """ 
 ______
|      |      
|      0 
|     /|\\ 
|     / \\ 
|
"""

def choose_random_word():
	words = [line.strip() for line in open("words.txt")]
	return  random.choice(words)

#myword = choose_random_word()

def print_dashes(myword):
	# print myword
	dashes = "_" * len(myword)
	print dashes
	return dashes

def play_again():
	play = raw_input("Do you want to play again?(yes or no)\n")
	if play == "no":
		print "see you next time"
	elif play == "yes":
		pass
	else:
		play = raw_input("Enter either 'yes' or 'no'.\n")
	return play


def prompt_and_check_input():
#answer = None
	play = "yes"
	while play == "yes":
		myword = choose_random_word()
		dashes = print_dashes(myword)
		myWordInList = list(myword)
		listDashes = list("_" * len(myword))
		trials = 0
		print_dashes(myword)
		while trials <= 5:
			print "Hey buddy guess a letter in the word"
			answer = raw_input(prompt)

			if answer in myWordInList:
				i = len(myWordInList) - 1
				while i >= 0:
					if myWordInList[i] == answer:
						listDashes[i] = answer
					i-=1
				print "".join(listDashes)
				if listDashes == myWordInList:
					print "That was great"
					play = play_again()
					trials = 6

			else:
				if trials == 0:
					print poll
				elif trials == 1:
					print rope
				elif trials == 2:
					print head
				elif trials == 3:
					print frontLimbs
				elif trials == 4:
					print body
				else:
					print "The answer was", myword
					print "Try again"
					print full
					play = play_again()
				trials += 1


if __name__ == "__main__":
	prompt_and_check_input()