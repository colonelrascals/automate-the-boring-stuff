import os

filePath = 'C:\\Users\\mkhir\\Desktop\\hello.txt'

helloFile = open(filePath)

content = helloFile.read()
print(content)
helloFile.close()

helloFile = open(filePath)
print(helloFile.readlines())
helloFile.close()

# w'rite' will overwrite contents of existing file or create new file with contents
helloFile = open('C:\\Users\\mkhir\\Desktop\\hello2.txt', 'w')
helloFile.write('Howdy!')
helloFile.close()

baconFile = open('C:\\Users\\mkhir\\Desktop\\bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()

# a'ppend' will add onto contents of existing file
baconFile = open('C:\\Users\\mkhir\\Desktop\\bacon.txt', 'a')
baconFile.write('\n\nBacon is delicious.')
baconFile.close()