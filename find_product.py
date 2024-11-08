def rec_prod(x):
    # incremental way 
    # product = 1
    # for i in range(1, len(x)):
    #     product *= x[i]
    # return product
     
    # recursive way
    if x == []:
        return 1
    else:
        head = x[0]
        tail = x[1:]
        product = rec_prod(tail) 
        return head * product
    
    
print(rec_prod([1,2,3,4,5,6,7,8]))