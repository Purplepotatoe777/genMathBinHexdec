from os import makedirs

answer_base = 'decimal answers'
level = 1
sublevel = 1
# max_exponant goes from 1 to 7 , the greater, the bigger & more difficult the deck. Set to {4,5,6,7} for level{1_1,1_2,1_3,1_4}
max_exponant = 4
deck = []

for i in range(1 , max_exponant + 1) :
    for j in range(i + 1):
        question = str(2**i)  + '+' + str(2**j)
        answer = str(2**i + 2**j)
        deck.append([question , answer])

try:
    deckfile = open(f'decks/level{level}/sublevel{sublevel}.txt','a') 
except:
    makedirs(f'decks/level{level}')    
    deckfile = open(f'decks/level{level}/sublevel{sublevel}.txt','a') 
line = answer_base + '\n'
deckfile.write(line)
for card in deck:
   line = str(card[0]) +' -> '+ str(card[1])+ '\n'
   deckfile.write(line)  
deckfile.close

  

   

