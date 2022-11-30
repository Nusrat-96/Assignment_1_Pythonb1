#4 Remove specific item form the list
remove_list = [i for i in input("Enter list value: ").split()]
remove_item= input("Enter element thats have to remove from the list: ")
n=remove_list.count(remove_item)
if n==0:
    print("This item is not in the list")
else:
    for i in range(n):
        remove_list.remove(remove_item)
    print ("Item removed:",remove_list)
