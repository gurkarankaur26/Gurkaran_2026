           
'''Write a function find_anagrams(text) that:

    Splits the given text into words.

    Uses a dictionary to group words that are anagrams of each other.

    Returns a dictionary where:

    The key is the sorted letters (like "eilnst").
    The value is a list of words that are anagrams.'''

def find_anagrams(text):
    result = {}
    text_lst = text.split(" ")
    for key in text_lst: 
         sorted_key = "".join(sorted(key))
         if  sorted_key in result.keys(): 
              result[sorted_key] =  result[sorted_key]+", "+key 
         else:
            result[sorted_key] =  key
    return result            