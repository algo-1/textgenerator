# import string
# # lyrics changed to return_lyrics no need to update here site already working as intended 
# from genius import lyrics

# lyrics = lyrics.replace("(","")
# lyrics = lyrics.replace(")", "")
# lyrics = lyrics.replace('"', '')
# lyrics = lyrics.replace("\n", " ")

# text = [ele for ele in lyrics.split()]
# # to avoid error due to zero probability when the last word is unique
# text.append(text[0])

# len_of_lines = []
# # with open("text.txt") as file:
# #     for line in file.readlines():
# #         line = line.replace("(","")
# #         line = line.replace(")", "")
# #         line = line.replace('"', '')
# #         list_per_line = line.split()
# #         for word in list_per_line:
# #             text.append(word)
# # text.append(text[0])

# with open("text.txt") as f:
#     for line in f.readlines():
#         len_of_lines.append(len(line.split()))

# # text = ["yes", "no", "yes", "no", "damn", "no", "dog", "yes", "boy", "with", "a", "gun", "animals", "a", "better", "no"]
# unique_text = set(text)
# n = len(unique_text)
# matrix = [[0 for _ in range(n)] for _ in range(n)]
# # vector = [0 for _ in range(n)]
# dict1 = {}
# dict2 = {}
# i = 0
# while unique_text:
#     val = unique_text.pop()
#     dict1[i] = val
#     dict2[val] = i
#     i += 1

# # print(dict1)
# # print(dict2)

# v = len(text) - 1 # - 1 avoids IndexError 
# for i in range(v):
#     text_id = dict2[text[i]]
#     next_id = dict2[text[i+1]]

#     matrix[text_id][next_id] += 1


# # print(matrix)
# # print()
# from random import randrange
# def markov(seed, dict1, dict2, matrix, len_of_lines):
#     # size = len(len_of_lines)
#     # rand = randrange(0, size)
#     len_of_line = 10 # len_of_lines[rand] 

#     val = dict2[seed]
#     print(seed.upper(), end=" ")
#     for _ in range(14):
#         count = len_of_line
#         while count > 0:
#             next_word_i = random_index(matrix[val])
#             print(dict1[next_word_i].upper(), end=" ")
#             val = next_word_i
#             count -= 1
#         print()


# def random_index(List):
#     n = len(List)
#     rand_list = []
   
#     for i in range(n):
#         for _ in range(List[i]):
#             rand_list.append(i)

#     length = len(rand_list)
#     rand = randrange(0, length)
#     return rand_list[rand]

# # text = []
# # words =[]
# # with open("text.txt") as f:
# #     for line in f.readlines():
# #         text.append(line.split())

# # with open("text.txt") as file:
# #     for w in file.readlines():
# #         list_per_line = w.split()
# #         for word in list_per_line:
# #             words.append(word)

# # def random(text, words, num_lines):
# #     from random import randrange

# #     len_of_lines = []
# #     for line in text:
# #         len_of_lines.append(len(line)) 

# #     count = 0
# #     len_words = len(words)
# #     size = len(len_of_lines)
# #     while count < num_lines:
# #         # print a line of random length based on lengths in the text
# #         rand = randrange(0, size)
# #         val = len_of_lines[rand]
# #         to_print = []
# #         for _ in range(val):
# #             rand2 = randrange(0, len_words)
# #             to_print.append(words[rand2])
# #         print(" ".join(to_print))
# #         count += 1


# # def markov_chain(text, words, num_lines): #KeyboardInterrupt ?
# #     pass 


# # if __name__ == "__main__":
# #     for _ in range(3):
# #         random(text, words, num_lines = 20)
# #         print()

# if __name__ == "__main__":
#     for i in range(1):
#         # text[i * 10]
#         markov("I'm", dict1, dict2, matrix, len_of_lines)
#         # print(text)
#         print()