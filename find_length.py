def rec_len(x):
    if x == []:
        return 0
    else:
        return 1 + rec_len(x[1:])
    
    
print(rec_len([1, 2, 3, 4,6,7,8,2]))
    