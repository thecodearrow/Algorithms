#https://www.spoj.com/problems/MCARDS/
from itertools import permutations

c,n=[int(x) for x in raw_input().split()] 
total_cards=int(n*c)
given_cards=[]
for i in range(c*n):
    color,number=[int(x) for x in raw_input().split()]
    given_cards.append([color,number])

colors=[i+1 for i in range(c)]
color_permutations=list(permutations(colors))
card_permutations=[] #all possible sorted color combinations that are acceptable
for c in color_permutations:
    current_card_permutation=[]
    for color in c:
        for i in range(1,n+1):
            current_card_permutation.append([color,i])
    card_permutations.append(current_card_permutation)

moves_count=[]

for current_card_permutation in card_permutations:
    order={}
    itr=1
    for card in current_card_permutation:
        if(card[0] not in order):
            order[card[0]]=itr
            itr+=1
    lis=[1 for i in range(total_cards)]
    for i in range(1,total_cards):
        for j in range(i):
            if(order[given_cards[j][0]]<order[given_cards[i][0]]):
                lis[i]=max(lis[i],lis[j]+1)
            else:
                if(order[given_cards[j][0]]==order[given_cards[i][0]]):
                    if(given_cards[j][1]<given_cards[i][1]):
                        lis[i]=max(lis[i],lis[j]+1)

    moves=total_cards-max(lis)
    moves_count.append(moves)
    
print(min(moves_count))







