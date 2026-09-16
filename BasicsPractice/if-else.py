"""Classify a person's age."""

a = int(input("enter your age :"))

if a <= 12:
  print("you are a child")
elif a <= 19:
  print("you are a teenager")
elif a <= 30:
  print("you are a young adult")
elif a <= 50:
  print("you are an adult")
elif a <= 60:
  print("you are a senior citizen")
else:
  print("you are too old")
