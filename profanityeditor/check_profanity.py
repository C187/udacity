def read_text():
    #NOTE path is local to my machine
    quotes = open("C:\Users\c187r\OneDrive\Documents\GitHub\udacity\profanityeditor\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

def check_profanity(text_to_check):
    connection = urllib.urlopen(" http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
read_text()
