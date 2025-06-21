#Traffic Light
signal=input("Shown signal:")

match signal:
  case "Red":
    print("Stop")
  case "Yellow":
    print("Wait")
  case "Green":
    pritnt("Walk")
