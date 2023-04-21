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
    

word = "zaba"
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
print(designerPdfViewer(h,word))
