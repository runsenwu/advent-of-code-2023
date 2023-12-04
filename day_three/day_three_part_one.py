# to find all things that are adjacent, we can represet all symbols with a n * m
# 2d array

def gear_ratios(matrix) -> int:
  ret_sum = 0

  # represent the numbers in the following way:
  # numbers = [(row, start_column, end_column_inclusive)]
  numbers = []


  for i in range(len(matrix)):

    start = 0
    end = 0
    first_seen = False

    for j in range(len(matrix[0])):
      if matrix[i][j].isdigit():
        if not first_seen:
          start = j
          end = j
          first_seen = True
        else:
          end = j

      elif first_seen:
        numbers.append((i, start, end))
        first_seen = False

    if first_seen:
      numbers.append((i, start, end))
      first_seen = False

  for number in numbers:
    print(number)
    # find number first
    string = ""

    for i in range(number[1], number[2] + 1):

      string += matrix[number[0]][i]

    print(int(string))
    if symbol_around(matrix, number):

      ret_sum += int(string)

  return ret_sum


def is_symbol(char) -> bool:
  if not char.isnumeric() and char != ".":
    return True

  return False


def symbol_around(matrix, index) -> bool:
  for i in range(index[1], index[2] + 1):
    # row above
    if index[0] - 1 >= 0:
      if i - 1 >= 0:
        if is_symbol(matrix[index[0] - 1][i - 1]):
          return True

      if is_symbol(matrix[index[0] - 1][i]):
        return True

      if i + 1 < len(matrix[0]):
        if is_symbol(matrix[index[0] - 1][i + 1]):
          return True

    # curr row
    if i - 1 >= 0:
      if is_symbol(matrix[index[0]][i - 1]):
        return True
    if i + 1 < len(matrix[0]):
      if is_symbol(matrix[index[0]][i + 1]):
        return True

    # row below
    if index[0] + 1 < len(matrix):
      if i - 1 >= 0:
        if is_symbol(matrix[index[0] + 1][i - 1]):
          return True

      if is_symbol(matrix[index[0] + 1][i]):
        return True


      if i + 1 < len(matrix[0]):
        if is_symbol(matrix[index[0] + 1][i + 1]):
          return True

  return False


def main():
  matrix = []

  with open("input.txt", 'r') as f:
    for line in f:
      # add all symbol of this line into the list of matrix
      curr_list = []
      for char in line.strip():
        curr_list.append(char)
      matrix.append(curr_list)

  print(gear_ratios(matrix))



if __name__ == "__main__":
  main()

  # 515 + 357 + 313 + 444 + 7 + 935