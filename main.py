import re # import the regular expression library

outputList = [] # List to old all of our line to write to the out file

# Function will determine what error exists in the given line
def determineFail(line):
  # No semi-colon test
  if not (line.endswith(';')):
    outputList.append("Fail: No semi-colon! | " + str(line))
  else:
    outputList.append("Fail: Still working on other fail cases")


# Tests if the line matches the specified grammar and passes to error handling function if it does not
def grammar(line):
  pattern = re.compile("^([a-zA-Z_])(\s)([=])(\s)((([a-zA-Z_])(\w)+)(\s)([+|-|*|/|%])(\s)([a-zA-Z_])(\w)+)+([;])$")
  if (pattern.match(line)):
    outputList.append("Pass: " + str(line))
  else:
    determineFail(line)

# Writes out all of the pass/fails to the out.txt file
def writeOutFile():
  with open("out.txt", 'a') as outFile:
    for item in outputList:
      outFile.write(item)

# Reads the file
def readFile():
  with open('sample.txt') as file:
    for line in file:
      grammar(line)
  writeOutFile()

# Erases the 
def eraseOutFile():
  with open("out.txt", 'w'):
    pass

def main():
  eraseOutFile()
  readFile()

if __name__ == '__main__':
  main()