list_reverse = [i for i in input("Enter list value:").split() ]
print("list:", list_reverse)

#list reversed using slicing
final_list_slice = list_reverse[::-1]                   
print ("List Reversed: ", final_list_slice)

#list reverse using loop
final_list = []
for element in list_reverse:
    final_list = [element]+final_list
print ("List reversed using loop: {}".format(final_list))

#list reverse using recursion
list_reverse_copy=list_reverse.copy()
def list_reversed_fuction(list_reverse_copy ):
    if len(list_reverse_copy)==1:         #or len(list_reverse)==0
        return list_reverse_copy
    else:
        element=[]
        element.append(list_reverse_copy[0])
        return list_reversed_fuction(list_reverse_copy[1:])+element
print("List reversed using recursion: ", list_reversed_fuction(list_reverse_copy))


#list reverse using pop() and append() method
final_list_pop = []
for i in range (0,len(list_reverse_copy)):
    final_list_pop.append(list_reverse_copy.pop())   #pop method with no argument remove last item of the list
print ("list reversed using pop: ", final_list_pop)


#using insert()method
list_reverse_copy2=list_reverse.copy()
final_list_ins = []
i=(len(list_reverse_copy2)-1)
while i>(-1):
    position= len(final_list_ins)+1
    final_list_ins.insert(position, list_reverse_copy2[i])
    i=i-1
print("list reversed using insert: ", final_list_ins)

