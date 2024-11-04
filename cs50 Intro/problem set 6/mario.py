from cs50 import get_int


def main():
  size = get_height()
  for row in range(size):
    for spaces in range((size - row - 1), 0, -1):
      print(" ", end="")
    for i in range(row + 1):
      print("#", end="")
    print()

def get_height():
  while True:
      try:
          height = get_int("Select a height from 1 to 8: ")
          if (height >= 1) and (height <= 8):
              break
      except:
          print("Please select a valid height from 1 to 8")
  return height


main()