"""Generate markov text from text files."""


from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """


    with open(file_path) as text_file:

        text = text_file.read()
        #print text
        return text

def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """

    chains = {}
 
    words = text_string.split()
    
    for idx, word in enumerate(words[:-3]):
      
        # bigram = (word, words[idx + 1])
        trigram = (word, words[idx + 1], words[idx +2])
        if trigram not in chains:

            chains[trigram] = list()
            chains[trigram].append(words[idx + 3])


        
        elif trigram in chains:

            chains[trigram].append(words[idx + 3])

   

    
         

    #print chains
    return chains


def make_text(chains):
    """Returns text from chains."""

    
    key = choice(chains.keys()) #this is the random start tuple
    words = list(key)
    # words.append(key[0]) # adding to a list where the tuples already exists
    # words.append(key[1])# this will put duplicates at the beginning
  
    while key in chains:
        words.append(choice(chains[key]))
        key = (words[-3], words[-2], words[-1]) # this creates the new key to continue the chain
       



    return " ".join(words)


#input_path = "hobbit.txt"
input_path = sys.argv[1]
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
