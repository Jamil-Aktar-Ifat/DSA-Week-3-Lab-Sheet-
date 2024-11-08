def rec_min(x):
    head = x[0]
    tail = x[1:]
    if tail == []:
        return head
    else:
        all_tails = rec_min(tail)
        if head < all_tails:
            return head
        else:
            return all_tails
            
            
    
print(rec_min([10 , 30, 40, 4, 2, 54]))