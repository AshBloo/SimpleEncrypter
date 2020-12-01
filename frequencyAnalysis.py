#Setup
import matplotlib.pyplot as plt
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generateLetterCount(text):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for letter in text:
        if letter in alphabet:
            letterCount[letter] += 1
    return letterCount

def plotLetterCount(count):
    plt.bar(*zip(*count.items()))
    plt.show()

def comparison(count):
    key = alphabet.find("E")
    mostCommon = max(count, key=count.get)
    countKey = alphabet.find(mostCommon)
    trueKey = countKey - key
    return trueKey

text = '''This is the tale of an old man who lived high on a mountain top.
He spent day after day, watching the people of the world below through a magical telescope.
Everyday, he would descend from the mountain and return with a new friend.
Of these friends, most were just fleeting visits, there for only a moment. 
But sometimes they chose to linger a while, fearful of leaving the old mans side.
Scared as they might have been, the old man always managed to soothe them and convinced them to leave.

Expanding his circle of friends consumed the old man for many years, until one day a beautiful woman arrived at the mountain.
Seeing her set the old mans heart ablaze, with her eyes of desert sands and hair of forest leaves.
Vainly, she felt no fear of the old man, and in fact seemed to love him.
After confessing their love to each other, they lived happily atop the mountain for many years.
Then one day, while the old man was finding a new friend, the beautiful woman decided to try out his telescope.
Obsessively she gazed down at the people of the world, seeing their deepest secrets and shames.
Riotous laughter burst from her as she mocked those she deemed beneath her.

Yet when the old man returned, he finally saw the ugliness beneath her apparent beauty, and deemed her beneath him.
With sadness, the old man mourned this revelation, for he thought he had found someone to join him in his lonely role.
And with great regret, he told the woman that she must leave the mountain.
Instead of going quietly, she tried to take the old mans place, tried forcing him down the mountain instead.
This left him no choice, and he used his hidden might to send her away for all eternity.
Some say he continues to gaze upon her with his telescope to this day, with a single tear tracing his bony cheeks.'''

count = generateLetterCount(text.upper())
cipherKey = comparison(count)




#plotLetterCount(count)
#mostCommon = max(count, key=count.get)
#print(mostCommon)