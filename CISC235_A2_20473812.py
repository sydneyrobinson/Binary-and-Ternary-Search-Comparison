'''
Sydney Robinson
20472812

I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity
'''

# 1: implement binary and ternary search
# 2: modify the algorithms so that they count the number of values are compared to target

'''
Here are alternative versions of the search algorithms that adds to the counter after the else statements as well. 
It seems more logically correct, but mathematically it seems that the other algorithms below are more accurate. 
I'm not sure why this is.

def bin_search(A, target):
        # returns index of target in A, if present
        # returns -1 if target is not present in A
        counter = 0

        done = False
        location = -1
        first = 0
        last = len(A) -1
        while not done:
            if first > last:
                    done = True
            else:
                mid = (first+last)//2
                if A[mid] == target: #COMPARISON
                    counter+=1

                    location = mid
                    done = True
                elif A[mid] > target: #COMPARISON
                    counter+=2

                    last = mid-1
                else:           
                    counter+=2 #carry forth two previous comparisons

                    first = mid+1

        print("The number of comparisons to target in BINARY: "+str(counter))
        return location
        

def trin_search(A, target):
    # returns index of target in A, if present 
    # returns -1 if target is not present in A 
    counter = 0

    done = False
    location = -1
    first = 0
    last = len(A)-1
    while not done:
        if first > last:
            done = True
        else:
            one_third = first + (last-first)//3
            if A[one_third] == target: #COMPARISON
                counter+=1

                location = one_third 
                done = True
            elif A[one_third] > target: #COMPARISON
                counter+=2
                 # search the left-hand third
                last = one_third-1
            else:
                two_thirds = first + 2*(last-first)//3
                if A[two_thirds] == target:  #COMPARISON
                    counter+=3 # carry forth previous comparisons plus the new one

                    location = two_thirds
                    done = True
                elif A[two_thirds] > target: #COMPARISON
                    counter+=4
                    # search the middle third
                    first = one_third + 1
                    last = two_thirds - 1
                    
                else:
                    counter+=4 #carry forth previous comparisons
                    # search the right-hand third
                    first = two_thirds + 1
    print("The number of comparisons to target in TRINARY: "+ str(counter))
    return location
'''

'''
Binary search reduces the number of possible locations for the target value by 
(about) half each time, which makes it quite efficient. 
But we could eliminate more locations by looking at two values in the
range A[first ... last] : If we look at the value 1/3 of the way from first
to last, and the value 2/3 of the way from first to last, 
we can eliminate about 2/3 of the locations each time. 

We can call this algorithm Trinary Search.
''' 
#-----------SEARCH ALGORITHMSSS THAT RETURN COMPARISONS-------------
def bin_search_counter(A, target):
        # returns index of target in A, if present
        # returns -1 if target is not present in A
        counter = 0

        done = False
        location = -1
        first = 0
        last = len(A) -1
        while not done:
            if first > last:
                    done = True
            else:
                mid = (first+last)//2
                if A[mid] == target: #COMPARISON
                    counter+=1

                    location = mid
                    done = True
                elif A[mid] > target: #COMPARISON
                    counter+=2

                    last = mid-1
                else:
                    first = mid+1

        return counter
        
def trin_search_counter(A, target):
    # returns index of target in A, if present 
    # returns -1 if target is not present in A 
    counter = 0

    done = False
    location = -1
    first = 0
    last = len(A)-1
    while not done:
        if first > last:
            done = True
        else:
            one_third = first + (last-first)//3
            if A[one_third] == target: #COMPARISON
                counter+=1

                location = one_third 
                done = True
            elif A[one_third] > target: #COMPARISON
                counter+=2
                 # search the left-hand third
                last = one_third-1
            else:
                two_thirds = first + 2*(last-first)//3
                if A[two_thirds] == target:  #COMPARISON
                    counter+=3

                    location = two_thirds
                    done = True
                elif A[two_thirds] > target: #COMPARISON
                    counter+=4
                    # search the middle third
                    first = one_third + 1
                    last = two_thirds - 1
                    
                else:
                    # search the right-hand third
                    first = two_thirds + 1
    return counter

'''
Experiment 1: 
1. generate a list of n integers in ascending order
2. use binary search to search the array for each of the values IN the array.
   Record the average number of "comparisons to target"
3. same thing as 2 but with trinary search

Tip: fill array with consecuitve even numbers
'''
def create_evens_list(n): # includes zero
    evens_list = list(range(0, n*2, 2))
    return evens_list

def bin_avg_comparisons(list_input): #searches for all the elements in the list and computes an average
    sum = 0
    for i in range(0, len(list_input)-1):
        value = list_input[i]
        comparisons = bin_search_counter(list_input,value)
        sum += comparisons
        i+=1   
    return sum/len(list_input)

def trin_avg_comparisons(list_input): #searches for all the elements in the list and computes an average
    sum = 0
    for i in range(0, len(list_input)-1):
        value = list_input[i]
        comparisons = trin_search_counter(list_input,value)
        sum += comparisons
        i+=1   
    return sum/len(list_input)

'''
Experiment 2:
Repeat experiment 1 but only for values that are not in the array
1. search for a value that is too small
2. search for a value that is too large
3. search for one value that falls between each pair of consecutive values in the array
    (total of n+1) search values
Tip: search for odd numbers

'''
def create_not_list(input_list): # includes zero
    not_in_list = list(range(-1, input_list[-1]+2, 2))
    return not_in_list

def bin_not_comparisons(list_input, not_list): #searches for all the elements in the list and computes an average
    sum = 0
    for i in range(0, len(not_list)-1):
        value = not_list[i]
        comparisons = bin_search_counter(list_input, value)
        sum += comparisons
        i+=1   
    return sum/len(not_list)

def trin_not_comparisons(list_input, not_list): #searches for all the elements in the list and computes an average
    sum = 0
    for i in range(0, len(not_list)-1):
        value = not_list[i]
        comparisons = trin_search_counter(list_input, value)
        sum += comparisons
        i+=1   
    return sum/len(not_list)

#--------------MAIN---------------
l = create_evens_list(16000) #ADJUST N HERE



# -----> Experiment 1:
# Search for all values inside the array, and compute average comparison number per search
print("\n(EVEN) The average BINary comparisons to target: "+str(bin_avg_comparisons(l)))
print("(EVEN) The average TRInary comparisons to target: "+str(trin_avg_comparisons(l)))

# -----> Experiment 2:
# Search only for values that aren't in the array
not_l = create_not_list(l)

print("\n(ODD) The average BINary comparisons to target: "+str(bin_not_comparisons(l,not_l)))
print("(ODD) The average TRInary comparisons to target: "+str(trin_not_comparisons(l,not_l)))
