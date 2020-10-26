string = 'HackerRank.com presents "Pythonist 2"'

def swap_case_long(s):
  final = ''
  for letter in string:
    swapped = ''
    if(letter.isupper()):
      swapped = letter.lower()
    elif(letter.islower):
      swapped = letter.upper()
    else:
      swapped = letter
    final += swapped
  return final

def swap_case(s):
  final_arr = ''.join([ letter.lower() if(letter.isupper()) else letter.upper() if(letter.islower) else letter for letter in string])
  return final_arr  

#The ternary form of the if/else operator doesn't have an 'elif' built in, but you can simulate it in the 'else' condition:
# ['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in l]

result = swap_case(string)
print(result)
