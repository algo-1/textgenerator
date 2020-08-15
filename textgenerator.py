# Aim: To Generate Text From Song Lyrics Using Markov Chains

# Algorithm
# Takes in the name of a music artist, analyzes the lyrics from the specified person and 
# generates text from a seed word using markov chains

from random import randrange
import string

# Get text
from genius import return_lyrics, access_token
def get_generated_text_list(name_of_artist):
    lyrics = return_lyrics(name_of_artist, access_token)

    lyrics = lyrics.replace("(","")
    lyrics = lyrics.replace(")", "")
    lyrics = lyrics.replace('"', '')
    lyrics = lyrics.replace("\n", " ")

    text = [ele for ele in lyrics.split()]
    # to avoid error due to zero probability when the last word is unique
    text.append(text[0])

    unique_text = set(text)
    n = len(unique_text)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    dict1 = {}
    dict2 = {}
    i = 0
    while unique_text:
        val = unique_text.pop()
        dict1[i] = val
        dict2[val] = i
        i += 1

    v = len(text) - 1 # - 1 avoids IndexError 
    for i in range(v):
        text_id = dict2[text[i]]
        next_id = dict2[text[i+1]]

        matrix[text_id][next_id] += 1

    def markov(seed, dict1, dict2, matrix):
        len_of_line = 10 
        try:
            val = dict2[seed]
        except KeyError:
            seed = text[0]
            val = dict2[seed]
        
        res = []
        print(seed.upper(), end=" ")
        for i in range(14):
            count = len_of_line
            line = []
            if i == 0:
                line.append(seed.upper())
            while count > 0:
                next_word_i = random_index(matrix[val])
                print(dict1[next_word_i].upper(), end=" ")
                line.append(dict1[next_word_i].upper())
                val = next_word_i
                count -= 1
            res.append(line)
            print()
        return res


    def random_index(List):
        # returns an index based on the probability of the lyric coming after the previos word
        n = len(List)
        rand_list = []
    
        for i in range(n):
            for _ in range(List[i]):
                rand_list.append(i)

        length = len(rand_list)
        rand = randrange(0, length)
        return rand_list[rand]

    generated_text_list = markov("I'm", dict1, dict2, matrix)

    return generated_text_list
