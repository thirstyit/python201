# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list_):
  # define the function here
  max_list = max(list_)
  min_list = min(list_)
  avg_list = sum(list_) / len(list_)
  
  print(f"THe list max is {max_list}, the list min is {min_list} and the average is {avg_list}.")
# call the function below here

stats(example_list)
