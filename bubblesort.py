def bubblesort(a):
    s=len(a)
    for i in range(s-2):
        for j in range(s-2-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
x=[20,53,87,57,41,45,21,70]
print("before sorting:",x)
bubblesort(x)
print("after sorting:",x)