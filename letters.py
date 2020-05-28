sentence = input("Enter a sentence without space: ")
letters_in_dict = {}
for i in sentence:
  if i in letters_in_dict:
    letters_in_dict[i] += 1
  else :
    letters_in_dict[i] = 1

print(letters_in_dict)