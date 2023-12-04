
# this time we are going to find the max of every single number

def find_max(line: str) -> int:
  red = 0
  green = 0
  blue = 0

  # take the second part without the game
  curr_line = line.split(':')[1]

  # parse the inputs
  curr_game = curr_line.split(';')

  for game in curr_game:
      curr_red = 0
      curr_green = 0
      curr_blue = 0

      for curr in game.split(","):
        curr = curr.strip()
        count, color = curr.split(" ")
        count = int(count)
        
        if color[0] == 'r':
          curr_red += count

        if color[0] == 'g':
          curr_green += count

        if color[0] == 'b':
          curr_blue += count

      red = max(curr_red, red)
      green = max(curr_green, green)
      blue = max(curr_blue, blue)

  return red * blue * green

def main():
  ret = 0
  with open('input.txt', 'r') as f:
    for line in f:
      ret += find_max(line)

  print(ret)

if __name__ == "__main__":
  main()