"""When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:

PDF-highighting.png

There is a list of  character heights aligned by index to their letters. For example, 'a' is at index  and 'z' is at index . There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in  assuming all letters are  wide.

Example
 

The heights are  and . The tallest letter is  high and there are  letters. The hightlighted area will be  so the answer is .

Function Description

Complete the designerPdfViewer function in the editor below.

designerPdfViewer has the following parameter(s):

int h[26]: the heights of each letter
string word: a string
Returns

int: the size of the highlighted area"""

from string import ascii_lowercase as ascl
def designerPdfViewer(h:list, word:str)-> int:
    # created a new word variable to ensure a pure function
    my_word = list(word)
    # sorted my list
    my_word.sort()
    word_count = len(word)
    longest_height = 0
    #iterated over the alphabet order and the list
    for a,b in zip(h, ascl):
        if b in my_word:
            if a > longest_height:
                longest_height = a      
    return word_count * 1 * longest_height
    # longest_height = my_word[-1].lower()
    # long_alpha_index = (ascl.index(longest_height))
    # val_for_long_height = (h[long_alpha_index])
    

word = "zaba"
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
print(designerPdfViewer(h,word))