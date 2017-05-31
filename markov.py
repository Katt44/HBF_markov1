"""Generate markov text from text files."""


from random import choice


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
    #pseudo code
    #need a for loop that gets index and word except for the last two, using enumerate
    
    #create dict using bigram as keys and a list of ngrams as values.
    #just forming keys here
    # var = (word, word[idx+1])
    words = text_string.split()
    #print words
    for idx, word in enumerate(words[:-2]):
        #print idx, word
        bigram = (word, words[idx + 1])
        #print bigram
        if bigram not in chains:
            #print bigram
            chains[bigram] = list()
        #for 
            chains[bigram].append(words[idx + 2])
            # hey what happens when the words in the tuple are in our dictionary
        elif bigram in chains:
            chains[bigram].append(words[idx + 2])

    #print chains

    
         
    # for bigram value in chains.items():
    #     chains[bigram] = value

    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    # this needs to be in a while loop
    #need a way to check if keys have been used before
    #if not used before then we want  A random value associated with that key
    key = choice(chains.keys())
    words.append(key[0])
    words.append(key[1])
    # print key
    words.append(choice(chains[key]))
    #hey this is the initial set up for randomizes tuples by first breaking them
    # for key in chains:
    #     bigram_link = choice(key)
    #     words.append(bigram_link)
    #     for value in chains.keys():
    #         ngram_link = choice(value)
    #         print ngram_link
    #print words

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
