from string import ascii_lowercase

TEXT = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""


def slice_and_dice(text: str = TEXT) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    results = []
    text = text.strip() #removes empty spaces on the left and right of the whole string
    text = text.splitlines() #creates a list where each line is a new element in the list

    results=[]
    for line in text:
        line = line.strip()
        #print(line)
        if line[0] in ascii_lowercase:
            words = line.split() #splits a string (each word) into a list.
            last_words = words[-1]
            last_words = last_words.strip('.!')
            results.append(last_words)
    return results
        
