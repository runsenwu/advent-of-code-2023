def parse_this_shit(line):
  dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

  first = ""
  last = ""

  first_seen = False

  for i in range(len(line)):
    if line[i].isdigit():
      if not first_seen:
        first_seen = True
        first = line[i]
        last = line[i]
      else:
        last = line[i]
    else:
        parse_word = line[i:]
        temp_hold = ""
        if len(parse_word) > 3:
          if parse_word[0: 3] in dict:
            temp_hold = dict[parse_word[0: 3]]
        if len(parse_word) > 4:
          if parse_word[0: 4] in dict:
            temp_hold = dict[parse_word[0: 4]]
        if len(parse_word) > 5:
          if parse_word[0: 5] in dict:
            temp_hold = dict[parse_word[0: 5]]

        if temp_hold != "":
          if not first_seen:
            first = temp_hold
            last = temp_hold
            first_seen = True
          else:
            last = temp_hold

  return first + last


def main():

  ret = 0
  with open('input.txt', 'r') as f:
    for line in f:
      ret += int(parse_this_shit(line))

  print(ret)


if __name__ == "__main__":
  main()