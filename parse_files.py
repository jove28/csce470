import sys
import os
from subprocess import call


def to_text(mainFolder):
  for folder in os.listdir(mainFolder):
    for file in os.listdir(mainFolder + "/" + folder):
      call('pdftotext -layout ' + file + ' Output/'+file)


def parse_files(mainFolder):
  for folder in os.listdir(mainFolder):
    outputFile = open(os.path.join(mainFolder, folder), 'w')
    for file in os.listdir(mainFolder + "/" + folder):
      openedFile = open(os.path.join(mainFolder + '/' + folder, file), "r")
      for line in openedFile:
        if(line.isspace()):
          continue
        else:
          outputFile.write(line)
      openedFile.close()
    outputFile.close()


# def parse_files(mainFolder):
#   for folder in os.listdir(mainFolder):
#     f = open(os.path.join(mainFolder, folder), "r")
#     outputFile = open(os.path.join(f, f), 'w')
#     for file in f:
#       openedFile = open(os.path.join(f, file), "r")
#       for line in openedFile:
#         if(line.isspace()):
#           continue
#         else:
#           outputFile.write(line)
#       openedFile.close()  
#     outputFile.close()
#     f.close()
  
def parse_file(fileName):
  inputFile = open(os.path.join("Texts", fileName), 'r')
  outputFile = open(os.path.join("Texts", "C" + fileName), 'w')
  
  for line in inputFile:
    if(line.isspace()):
      continue
    else:
      outputFile.write(line)
  inputFile.close()
  outputFile.close()
  
  
  
  
def main():
  if len(sys.argv) != 3:
    print 'usage: ./parse_file.py {-folder} file'
    sys.exit(1)
  option = sys.argv[1]
  mainFolder = sys.argv[2]
  
  if option == '-folder':
    parse_files(mainFolder)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()