phrase = 'Things you wish you knew as a freshman'
upperphrase= phrase.title()
remove_space= upperphrase.replace(" ", "")
hashtag='"#' + remove_space + '"'
phrase= '"' + phrase + '"'
print('The phrase',phrase)
print('becomes the hashtag',hashtag)
