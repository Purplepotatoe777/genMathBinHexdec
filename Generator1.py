
max_exponant = 7 # from 1 to 7 , the greater, the bigger & more difficult the deck. Set to {4,5,6,7} for level{1_1,1_2,1_3,1_4}
deck=[]

for i in range(1, max_exponant+1) :
   for j in range (i+1):
    a = str(2**i) + '+'+  str(2**j) 
    b = str(2**i + 2**j)
    deck.append([a,b])

print(deck) # should be store in txt file
  

   
