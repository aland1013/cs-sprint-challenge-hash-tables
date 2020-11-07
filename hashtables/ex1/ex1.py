def get_indices_of_item_weights(weights, length, limit):
    """
    create an empty hash table
    for each weight in weights:
        - calculate the target by subtracting weight from limit
        - if the target is stored in the hash table, return the 
          current index and the target index
        - else, store the index and weight in the hash table
    """
    ht = {}
    
    for i in range(length):
        target = limit - weights[i]
        
        if target in ht.values():
            x = i
            y = [k for k,v in ht.items() if v == target][0]
            return (x, y) if x > y else (y, x)
        
        ht[i] = weights[i]
        
    return None