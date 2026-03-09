'''Write a function word_count(text) that:
    Takes a string text as input.
    Splits the text into words (you can use split()).
    Counts how many times each word appears using a dictionary.
    Returns the dictionary of word counts.'''
   
def word_count(text):
    result = {}
    text_lst = text.split(" ")
    for key in text_lst:
        if  key in result.keys(): 
                result[key] = int(result[key])+1
        else:
            result[key] ="1"
    return result