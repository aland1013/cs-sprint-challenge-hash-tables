def intersection(arrays):
    """
    1. create a list 'hash_tables' to store a hash table for each array in arrays
    2. for each array in arrays:
       - create a hash table with a key for each number in the array
       - push the hash table into the hash_tables list
    3. compare the keys in the first two hash tables, and store all the keys
    in both of them in a list 'result'
    4. for each of the remaining hash tables, compare the keys with
    the values stored in result, eliminating any values from result 
    that are not keys in the hash table
    """
    hash_tables = []
    
    for arr in arrays:
        ht = {}
        
        for num in arr:
            ht[num] = True
        
        hash_tables.append(ht)
    
    result = [k for k in hash_tables[0] if k in hash_tables[1]]
    
    for i in range(2, len(arrays)):
        result = [k for k in result if k in hash_tables[i]]
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
