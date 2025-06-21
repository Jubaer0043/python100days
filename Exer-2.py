import time

Hour=int(time.strftime('%H'))
print(Hour)


#Morning->6 to 12.....6,7,8,9,10,11.59
#Afternoon-> 12 to 18.....12,13,14,15,16,17.59
#Evenning->18 to 22.....18,19,20,
#night->22 to 6
if(Hour >= 6 and Hour<12):
  print("Good Morning Sir")
elif(Hour>=12 and Hour<18):
  print("Good Afternoon Sir")
elif(Hour>=18 and Hour < 20):
  print("Good evenning Sir")    
elif(Hour>=20 and Hour < 6):
  print("Good Night Sir")
#short cut hoye gese, need to add min and second also...
