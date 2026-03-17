from functions.run_python_file import run_python_file

def test():

  result = run_python_file("calculator", "main.py")
  print("Test 1")
  print(result)

  result = run_python_file("calculator", "main.py", ["3 + 5"])
  print("Test 2")
  print(result)

  result = run_python_file("calculator", "tests.py")
  print("Test 3")
  print(result)

  result = run_python_file("calculator", "../main.py")
  print("Test 4")
  print(result)

  result = run_python_file("calculator", "nonexistent.py")
  print("Test 5")
  print(result)

  result = run_python_file("calculator", "lorem.txt")
  print("Test 6")
  print(result)

if __name__ == "__main__":
  test()