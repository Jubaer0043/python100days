num_of_passengers=int(input("please enter the number of passengers: "))

total_seats=50

if(num_of_passengers>total_seats):
  print('''The number is exceeded.\nPlease those whoose tickets are from 51, wait for the next bus.\nThe bus will be starting in next 5 minutes. ''')
elif(num_of_passengers< total_seats):
  print('''\nPlease, wait for the passengers. The supervisier is calling for the passengers.\nThe bus will be boarding in 15 minutes.''')
  print("\n")
  min=int(input("please insert the time: "))
  if(min>15):
    print("\nDriver er gaaye jhuta maar.")
  else:
    print("\nThikmoton bus chala.")
    
else:
  print("The bus engine is staring. Hold tight.")

print("\n\nThank you for journeing with us")
