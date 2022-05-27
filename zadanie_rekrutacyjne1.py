# create tuple nr 1
krotka1 = (3,4,5)
#create tuple nr 2
krotka2 = (1,2,3,4,5,6,7,8,9)

# create a function with two parameters tuple1 and tuple2
def fun(kr1,kr2):
    # for each element in tuple1
    for i in kr1:
        # check element is in tuple2 
        if i in kr2:
            continue
        else:
            print("Elements tuple1 aren't in tuple2")
            break
    else:
        print("Elements tuple1 are in tuple2")

fun(krotka1,krotka2)
