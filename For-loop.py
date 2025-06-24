#basic syntax of for loop
#Example1: loop through a list

distrcits =["Barishal","Dhaka","Rajshahi","Rangpur"]

for district in distrcits:
    print(district)
    for alpha in district:
        print(alpha)
else:
    print("Loop completed")#auto print

#ex-2 loop through a string
# word="hello"
# for letter in word:
#     print(letter)

#Ex-3: using rang() func
# for i in range(5):
#  print(i)

# print("\n\n")

# for j in range(2,19):
#  print(j)

# print("\n\n")

# for k in range(4,90,10):#(start,end,difference)
#  print(k)

##Ex-5: Nested for loop
# for i in range(10,33):
#  print(i)
#  for j in range(1,3):
#   print(j)

##Ex-6: for with if condition
# numbers=[1,2,3,4,5]

# for num in numbers:
#     if(num%2==0):
#         print(num)

## we can also use break and continue, enumerate,revered,zip,
