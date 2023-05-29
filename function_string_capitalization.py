# this function takes a string as input and capitalizes the first letter of each sentence in that string. If the input string contains multiple sentences, each sentence should be separated by ". " (period followed by a space) to ensure proper splitting and capitalization.


def string_capital(string):
  sentences = string[0].split(". ")
  caps_sentences = [sentence.capitalize() for sentence in sentences]
  return '. ' .join(caps_sentences)

cap_string = ["to watch his woods fill up with snow. my little horse must think it queer. to stop without a farmhouse near"]
print(string_capital(cap_string))