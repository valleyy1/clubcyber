
def word_counter(file_path, amount_n):  # efines a function to count n words in a file
    words_dict = read_file_to_dict(file_path)
    sorted_dict = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True)[:amount_n]) #sorts the dict by number of appearances, takes the n, and turns it back to a dict
    for key, value in sorted_dict.items():
        print("Word: " + key + " Appears " + str(value) + " times") #prints word and how many times each word appears 

    
def read_file_to_dict(file_path): #reading the file
    new_dict = {} #creates an empty dict to count words
    with open(file_path) as file: #opens the file
        for line in file: #goes over each line
            words = line.split() #splits the line into words
            for word in words: #goes over each word
                if word in new_dict: 
                    new_dict[word] += 1
                else:                      
                    new_dict[word] = 1
    return new_dict #returns the dictionary of word counts

file_path = "words.txt"
amount_n = 3
word_counter(file_path, amount_n)