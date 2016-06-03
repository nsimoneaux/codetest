#I gathered my solution from the following web page: https://rosettacode.org/wiki/Equilibrium_index

#Import the default dictonary subclass for missing values
from collections import defaultdict


#define method and approriate argument
def eqindex(data):
    
    #instantiate l and h=0, and instantiate the default dictionary values in the to '0'
    l, h = 0, defaultdict(list)
    
    #for each index 'i' and value 'c' in list 'data'...
    for i, c in enumerate(data): 
        
        #add the value 'c' to l (the total sum of the list so far)
        l += c
        
        #append the index 'i' to the array 'h', at the index of array 'h' where double the value of 'l' subtracting c
        #for values of l and c where c is half of l, this will accumlate all positions of i
        h[l * 2 - c].append(i)
        
    #return the value of array 'h' at the index 'l', calculated in the previous step to have accumulated all positions ('i') of the list where 'l', doubled, subtracting 'c' are equal to 'l' (equilibrium cases) 
    return h[l]
    