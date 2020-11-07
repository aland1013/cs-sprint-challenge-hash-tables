def has_negatives(a):
    """
    1. initialize an empty hash table
    2. initialize an empty list 'result'
    3. loop through the list 'a'
       - if the value is negative, store the positive as a key in the hash table
    4. push all of the keys in the hash table to result if they're also in the list 'a' 
    """
    ht = {}
    result = []
    
    for num in a:
        if num < 0:
            ht[-num] = num
    
    result = [num for num in a if num in ht]
    
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
