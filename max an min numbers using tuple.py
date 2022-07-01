def min_max(n):
    a=max(n)
    b=min(n)
    return(a,b)
numbers=(5,8,6,3,0,1,7,6,2)
(max_num,min_num)=min_max(numbers)
print("Maximum value =",max_num)
print("Minimum value =",min_num)
