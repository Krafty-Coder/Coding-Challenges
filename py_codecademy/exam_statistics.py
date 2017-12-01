grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  summ = 0
  for score in scores:
    summ += score
  print summ
  return summ

grades_sum(grades)

def grades_average(grades_input):
  total = grades_sum(grades_input)
  average = total/float(len(grades_input))
  return average

print grades_average(grades)
