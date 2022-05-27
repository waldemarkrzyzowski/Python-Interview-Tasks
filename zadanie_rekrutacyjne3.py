# create example list 
list = [1,2,0,0,5,0,1,-1,-10]

# create a zero_to_right function
def zero_to_right(list):
    # for loop is executed exactly the number of times number 0 is in the list
    for i in range(list.count(0)):
        # remove value 0
        list.remove(0)
        # append value 0 to the end of list
        list.append(0)
    # return list   
    return list

# call function
print(zero_to_right(list))
        
