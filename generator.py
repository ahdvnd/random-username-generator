import random, string
# read lists
with open('animals.txt', 'r') as infile:
    animals = infile.read().strip(' \n').split('\n')
with open('adjectives.txt', 'r') as infile:
    adjectives = infile.read().strip(' \n').split('\n')
with open('colors.txt', 'r') as infile:
    colors = infile.read().strip(' \n').split('\n')
# construct username
word1 = random.choice(colors)
word2 = random.choice(adjectives)
word3 = random.choice(animals)
#check if word2 is censored
#captilaize first letter
word1 =word1.title()
word2 =word2.title()
word3 =word3.title()
word4 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
username = '{}{}{}{}'.format(word1, word2, word3, word4)
print(username)
