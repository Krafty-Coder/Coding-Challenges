def hotel_cost(nights):
  """Returns hotel cost in the number of nights"""
  return 140 * nights

def plane_ride_cost(city):
  """Returns cost depending on destination chosen"""
  #city = str(input(""))
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  else:
    return 475
  
def rental_car_cost(days):
"""Returns total cost of renting a car"""
  cost = 40 * days
  if days >= 7:
    cost -= 50
    return cost
  elif days >= 3:
    cost -= 20
    return cost
  else:
    return cost
  
def trip_cost(city, days, spending_money):
"""Returns the total cost odf the trip"""
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
  
  
print(trip_cost("Los Angeles", 5, 600))
