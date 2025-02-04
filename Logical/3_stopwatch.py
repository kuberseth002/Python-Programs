import time

def watch():
  input("Enter time:")
  start_time=time.time()
  
  input("enter to stop:")
  end_time=time.time()
  time_left = end_time-start_time
  print(f"Elapsed time: {time_left:2f} seconds")  
watch()  