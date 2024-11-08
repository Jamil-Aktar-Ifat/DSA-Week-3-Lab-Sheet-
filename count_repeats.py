def rec_reps(x):
    if x == []:
        return 0 
    else: 
        head = x[0]
        tail = x[1:]
        all_tails = rec_reps(tail)
        if tail !=[] and head == tail[0]:
            return all_tails + 1
        else:
            return all_tails
    
    
print(rec_reps([1,6,3,4,6,6,6,6,9]))