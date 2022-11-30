#3 insert 20 in index 3 in the list:

#using insert and append mehtod
def insert_item(listadd,n,position,value):
    print ("original list:", listadd)
    if n>=position:
        listadd.insert(position,value)
    else:
        listadd.append(value)
    print("Add item \"{}\": {}".format(value, listadd))


#insert using slice
def insert_item_slice(listaddSlice,n,position,value):
    z=[value]
    if position<n and position>=0:
        z=listaddSlice[0:position]+z+listaddSlice[position:]
    else:
        z=listaddSlice+z
    print("Add item using slice: ", z)
            
#add item using loop
def insert_item_loop(listaddLoop,n,position,value):
    if position<n and position>=0:
        list2=listaddLoop.copy() + [0]
        for i in range(len(list2)):
            if i>=position:
                list2[i]=listaddLoop[i-1]
        list2[position]=value
        print ("Add item using loop: ", list2)
    else:
        list3=[value]
        print ("Add item using loop: ", listaddLoop+list3)


#taking input
list1=[i for i in input("Give list Elements:").split()]
n= len(list1)
position= int(input("Enter the postion to add element:"))
value = input("Give value have to add:")

print("\nIf position invalid then item will add the end of the list \n")

#using insert and append mehtod
listadd = list1.copy()
insert_item(listadd,n,position,value)

#insert using slice
listaddSlice=list1.copy()
insert_item_slice(listaddSlice,n,position,value)

#add item using loop
listaddLoop=list1.copy()
insert_item_loop(listaddLoop,n,position,value)
