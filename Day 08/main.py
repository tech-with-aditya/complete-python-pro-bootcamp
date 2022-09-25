def greet():
  print("Hello, there!")
  print("How are you?")
  print("Isn't the weather nice today!")
  
greet()

# Function with input
def greet_with_name(name):
  print(f"Hello, I'm {name}")
  
greet_with_name("Aditya")

# Function with more than one input

# This function is by default having positional arguments 
def greet_with(name, location):
  print(f"Hello! {name}")
  print(f"What is it like in {location}")
  
greet_with("Aditya", "Dehradun")

# same above function with keyword arguments
def greet_with(name, location):
  print(f"Hello! {name}")
  print(f"What is it like in {location}")
  
greet_with(location = "Dehradun", name = "Aditya")
