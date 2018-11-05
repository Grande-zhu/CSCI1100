""" Find all words containing three consecutive pairs of double letters
in a file of all English words located at:

        http://www.greenteapress.com/thinkpython/code/words.txt

**Modules used:**  :py:mod:`urllib`

**Author**: Sibel Adali <adalis@rpi.edu>, Chuck Stewart <cvstewart@gmail.com>

**Returns:** All words matching condition and the count of found words

**Pseudo Code**::

   open the file from the web with all the words in English

   for each word in the file:
       for all positions l in the word until there are not enough letters left
           if the letters at positions (l and l+1) are the same
              and the letters at positions (l+2 and l+3) are the same
              and the letters at positions  (l+4 and l+5) are the same then
               output word and increment the count

"""

import urllib.request

def has_three_double(word):
    """
    Returns True if the word contains three consecutive pairs of
    double letters and False otherwise.
    """
    for l in range(len(word) - 5):
        if word[l] == word[l + 1] and \
                word[l + 2] == word[l + 3] and \
                word[l + 4] == word[l + 5]:
            return True
    return False

# Comments that fit in a single line can be put in this format.

# The main body of the program starts here

# Assign the location of the words file and go get it.

word_url = 'http://www.greenteapress.com/thinkpython/code/words.txt'
word_file = urllib.request.urlopen(word_url)

# Process each word in the file one by one, testing to see if it has
# three consecutive doubles.  Print it and count it if it does.

count = 0
for entry in word_file:
    entry = entry.decode().strip()
    if has_three_double(entry):
        print(entry)
        count = count + 1

# After we've gone through all the words, output a final message based
# on the number of words that were counted.

if count == 0:
    print('No words found')
elif count == 1:
    print("1 word found")
else:
    print(count, 'words were found')
