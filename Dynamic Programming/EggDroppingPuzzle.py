"""
Given 100 floors and 2 eggs, find the  MINIMUM NUMBER OF ATTEMPTS to identify the threshold floor
 at which the egg breaks.

i.e. if the threshold floor is at 100 or 1st, your number of attempts should be safe! 


MATHEMATICAL WAY OF SOLVING THIS

https://www.geeksforgeeks.org/puzzle-set-35-2-eggs-and-100-floors/

Let us make our first attempt on x'th floor. 

If it breaks, we try remaining (x-1) floors one by one. 
So in worst case, we make x trials.

If it doesn’t break, we jump (x-1) floors (Because we have
already made one attempt and we don't want to go beyond 
x attempts.  Therefore (x-1) attempts are available),
    Next floor we try is floor x + (x-1)

Similarly, if this drop does not break, next need to jump 
up to floor x + (x-1) + (x-2), then x + (x-1) + (x-2) + (x-3)
and so on.

Since the last floor to be tired is 100'th floor, sum of
series should be 100 for optimal value of x.

 x + (x-1) + (x-2) + (x-3) + .... + 1  = 100

 x(x+1)/2  = 100
         x = 13.651

Therefore, we start trying from 14'th floor. If Egg breaks
we one by one try remaining 13 floors.  If egg doesn't break
we go to 27th floor.
If egg breaks on 27'th floor, we try floors form 15 to 26.
If egg doesn't break on 27'th floor, we go to 39'th floor.

An so on...

"""
import math

floors=100
eggs=2
#x^2+x-(2*floor)=0 quadratic equation

x=(-1+(math.sqrt(1+4*2*floors)))/2
x=math.ceil(x)


print(x)


#This can also be solved using Dynamic Programming! (TO BE SOLVED LATER)