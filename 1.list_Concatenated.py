#1. Take input of two integer lists and Concatenate two lists index-wise
# code will also execute if we enter two list with different length
def list_solution(list1, list2):
    conc_list=[]
    max_len = max (len(list1),len(list2))
    min_len = min (len(list1),len(list2))
    max_list = []
    min_list = []
    if len(list1)> len(list2):          #find the large list 
        max_list = list1
        min_list = list2
    else:
        max_list = list2
        min_list = list1

    for i in range (0,max_len):
        if i<min_len:
            conc_list.append(max_list[i]+min_list[i])
        elif i>= min_len:
            conc_list.append(max_list[i])
    print ("Concatenated list is: ", conc_list)
list1 = list(map(int,input("Enter values for first list: ").split()))
list2 = list(map(int,input("Enter values for second list: ").split()))
list_solution(list1, list2)