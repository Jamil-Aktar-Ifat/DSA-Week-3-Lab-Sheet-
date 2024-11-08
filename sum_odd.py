def rec_oddsum(x):
    if x == []:
        return 0
    else:
        head = x[0]
        tail = x[1:]
        tails = rec_oddsum(tail)
        if head % 2 == 1:
            return head+tails
        else:
            return tails
           
    
    
print(rec_oddsum([2,3,4,5,6,7,8,9]))