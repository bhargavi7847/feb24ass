numlist=[]
even=[]
odd=[]

number=int(input("how many elements in list:"))
for i in range(1,number+1):
    value=int(input("please enter the value of %d element:"%i))
    numlist.append(value)
for j in range(number):
    if(numlist[j]%2==0):
        even.append(numlist[j])
    else:
        odd.append(numlist[j])
print("\n elements in even list is:",even)
print("elements in odd list is:",odd)


OUTPUT:
how many elements in list:6
please enter the value of 1 element:2
please enter the value of 2 element:3
please enter the value of 3 element:4
please enter the value of 4 element:5
please enter the value of 5 element:6
please enter the value of 6 element:7

 elements in even list is: [2, 4, 6]
elements in odd list is: [3, 5, 7]

