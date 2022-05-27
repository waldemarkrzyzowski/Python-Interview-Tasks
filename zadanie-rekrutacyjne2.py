# simple text to reverse each word
tekst1 = "ilśeJ ycsyzsw ąlśym kat ,omas ot śotk ein ilsym elacw"
# create a list 
tekst2 = tekst1.split()
# create an empty list
tekst_odwrocony =[]

# for each element in tekst2
for i in tekst2:
    # reverse a word and append to the new list
    i = i[::-1]
    tekst_odwrocony.append(i)
    
print("Original text: ", tekst1)
print("text after reversed")
print(" ".join(tekst_odwrocony))


        


