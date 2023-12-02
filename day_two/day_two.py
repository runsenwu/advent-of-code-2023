# given 12 red, 13 gree, 14 blue




def main():
  with open('input.txt', 'r') as f:
    for line in f:
      ret += int(parse_this_shit(line))

if __name__ == "__main__":
  main()