#https://www.codechef.com/FLPAST01/problems/RADGEE/
t=int(input())
from collections import deque
while t!=0:
    t-=1
    n,m=[int(x) for x in input().split()]
    radhesh=[int(x) for x in input().split()]
    geeta=[int(x) for x in input().split()]
    extra=[int(x) for x in input().split()]
    radhesh=deque(radhesh[::-1])
    geeta=deque(geeta[::-1])
    extra=extra[::-1]
    cards_left=n
    count_r=0
    count_g=0
    extra_cards_left=m
    while cards_left>0:
        r=radhesh.pop()
        g=geeta.pop()
        
        if(r>g):
            count_r+=1
        else:
            count_g+=1
        if(extra_cards_left>0):
            card1=extra.pop()
            card2=extra.pop()
            if(r>g):
                radhesh.appendleft(card1)
                geeta.appendleft(card2)
            else:
                geeta.appendleft(card1)
                radhesh.appendleft(card2)
            cards_left+=1
            extra_cards_left-=2
        cards_left-=1
    
    if(count_g>count_r):
        print("Geethakoomaree wins")
    elif(count_r>count_g):
        print("Radhesh wins")
    else:
        print("Tie")

