l=[1,2,10,30,33,99,101,200,301,402]
def binary_search(l,num):
    print(l)
    mid_index=len(l) // 2
    if num > l[mid_index]:
        binary_search(l[mid_index+1:],num)
    elif num < l[mid_index]:
        binary_search(l[0:mid_index],num)
    else:
        print('find it')
binary_search(l,301)