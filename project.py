num=int(input("Enter number to be checked:"))
sum=0
temp= num
while temp>0:
     digit=temp % 10
     sum+=digit ** 3
     temp//=10
if num==sum:
        print(num,"is an Armstrong number")
else:
        print(num,"is Not Armstrong number")