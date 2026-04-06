x = (int)(input("enter a number"))

if x % 5 == 0 and x != 0 :
    if x % 2 == 0:
        print(f" {x} is an even and also multiple of 5")
    else : 
        print(f"{x} is not Multiple of 5 and odd number : ",x)
elif x < 0 or x == 0:
    print("negative or  0 not allowed") 
else :
    print("Not a multiple of 5")

for i in range(5):
    print(i)

for i in range(1,5,2):
    print(i)


# Print multiplication table for any number using while
i = 1
while(i<=10):
    print(f"5 * {i} = ", 5*i )
    #i = i+1
    i+=1

# Print odd numbers from 1 to 10, using continue and while
n = 1
while(n<=10):
    if n % 2 == 0:
        n+=1
        continue
    print(n)
    n+=1

# Count vowels in a word using for loop.
strng = "education"
vowels = "aieouAEIOU"
count = 0
for ch in strng:
    if ch in vowels:
        count+=1
print(count)

# Sum of first n natural numbers using for loop.
sum = 0
for x in range(1,5):
    sum = sum+x
print(sum)

