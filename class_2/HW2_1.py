num = int(input("輸入正整數: "))
i = 1
counter = 0
while i<=num:
    if num%i==0:
        counter += 1
    i += 1
if counter == 2:
    print(num,"是否為質數: ",True)
else:
    print(num,"是否為質數: ",False)

# Big Oh = O(n)