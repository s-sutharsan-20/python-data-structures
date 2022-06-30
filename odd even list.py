even_num=[i for i in range(51) if i%2==0]
odd_num=[i for i in range(51) if i%2!=0]
print("Even Numbers less than 50 :\n",even_num)
print("Odd Numbers less than 50 :\n",odd_num)
print(even_num in odd_num)
print(5 in even_num)
print(5 in odd_num)
print(4 in even_num)
print(4 in odd_num)
