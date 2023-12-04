def gambling(line: str) -> bool:

  # parse for blue red or green

  # take the second part without the game
  curr_line = line.split(':')[1]

  # parse the inputs
  curr_game = curr_line.split(';')

  for game in curr_game:
    red = 0
    green = 0
    blue = 0
    for curr in game.split(","):
      curr = curr.strip()
      count, color = curr.split(" ")
      count = int(count)

      if color[0] == 'r':
        red += count

      if color[0] == 'g':
        green += count

      if color[0] == 'b':
        blue += count

  # given red max is 12, green max is 13, blue max is 14
      if red > 12 or green > 13 or blue > 14:
        return False

  return True

def main():
  ret = 0
  count = 0
  with open('input.txt', 'r') as f:
    for line in f:
      count += 1
      if gambling(line) == True:
        ret += count

  print(ret)

if __name__ == "__main__":
  main()