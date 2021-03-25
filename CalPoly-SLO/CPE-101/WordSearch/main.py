def main():
    line_puzzle = str(raw_input()) # puzzle data is being read in here
    search_words = str(raw_input())
    list_of_words = search_words.split()
  
    print 'Puzzle:'
   
    for i in range(0,len(line_puzzle),10): # puzzle data is turned into 10x10
        print line_puzzle[i:i+10] # outputting puzzle data

    forward = find_forward(line_puzzle,list_of_words)
    backward = find_backward(line_puzzle,list_of_words)
    upward = find_upward(line_puzzle,list_of_words)
    downward = find_downward(line_puzzle,list_of_words)
        
    for i in range(len(list_of_words)):
        if list_of_words[i] in forward:
            location = forward.index(list_of_words[i])
            print '{}: (FORWARD) row: {} column: {}'.format(list_of_words[i],forward[location+1],forward[location+2])
       
        elif list_of_words[i] in backward: 
            location = backward.index(list_of_words[i])
            print '{}: (BACKWARD) row: {} column: {}'.format(list_of_words[i],backward[location+1],backward[location+2])
    
        elif list_of_words[i] in upward:  
            location = upward.index(list_of_words[i])
            print '{}: (UP) row: {} column: {}'.format(list_of_words[i],upward[location+1],upward[location+2])
       
        elif list_of_words[i] in downward:  
            location = downward.index(list_of_words[i])
            print '{}: (DOWN) row: {} column: {}'.format(list_of_words[i],downward[location+1],downward[location+2])
             
        else:
            print '{}: word not found'.format(list_of_words[i])




#    print 'FORWARD:{}'.format(find_forward(line_puzzle,list_of_words))
#    print 'BACKWARD:{}'.format(find_backward(line_puzzle,list_of_words))
#    print 'UPWARD:{}'.format(find_upward(line_puzzle,list_of_words))
#    print 'DOWNWARD:{}'.format(find_downward(line_puzzle,list_of_words))

def find_forward(puzzle,words_list): #puzzle is a string. words_list is a list
    forward_list = []
    for i in range(0,len(puzzle),10): # here we are creating a list of the forward puzzle lines
        forward_line = puzzle[i:i+10]
        forward_list.append(forward_line)
    
    words_found = []
    for a in range(len(forward_list)): # we are creating a nested loop where a is the row it is searching
        for b in range(len(words_list)): # and b is the current word it is looking for
            find_column = forward_list[a].find(words_list[b]) #trying to find string b in string a
            if find_column >= 0:
                found_word = [words_list[b],a,find_column] # (word,row,column)
                words_found.append(found_word)
    return [item for sublist in words_found for item in sublist] # turning list of lists into 1 list

def find_backward(puzzle,words_list):
    backward_list = []
    puzzle = puzzle[::-1] # reverse the puzzle
     
    for i in range(0,len(puzzle),10): # rewrite the list with the reversed strings
        backward_line = puzzle[i:i+10]
        backward_list.append(backward_line)
    
    words_found = [] # same operation as with forward
    for a in range(len(backward_list)): 
        for b in range(len(words_list)): 
            find_column = backward_list[a].find(words_list[b]) 
            if find_column >= 0:
                found_word = [words_list[b],(9-a),(10-find_column)] # (word,row,column)
                words_found.append(found_word)
    return [item for sublist in words_found for item in sublist]

def find_upward(puzzle,words_list):
    upward_list = []
    
    backward_list = []
    puzzle = puzzle[::-1] # reverse the puzzle
     
    for i in range(0,len(puzzle),10): # going to reuse the backwards list
        backward_line = puzzle[i:i+10]
        backward_list.append(backward_line)

    for x in range(len(backward_list)-1): # -1 because backward_list returns a \r        
        upward_string = ''                 
        for y in range(len(backward_list)-1):
            current_row = backward_list[y]
            upward_string += current_row[x]
        upward_list.append(upward_string)
        

    words_found = [] # same operation as with forward
    for a in range(len(upward_list)): 
        for b in range(len(words_list)): 
            find_column = upward_list[a].find(words_list[b]) 
            if find_column >= 0:
                found_word = [words_list[b],(9-find_column),(10-a)] # (word,row,column)
                words_found.append(found_word)
    return [item for sublist in words_found for item in sublist]

def find_downward(puzzle,words_list):
    
    downward_list = []
    
    forward_list = [] # Going to reuse the forward list to index the downwards one
    for i in range(0,len(puzzle),10):  
        forward_line = puzzle[i:i+10]
        forward_list.append(forward_line)
    
    for x in range(len(forward_list)-1): # -1 because forward_list returns a \r at the end...       
        downward_string = ''
        for y in range(len(forward_list)-1):
            current_row = forward_list[y]
            downward_string += current_row[x]
        downward_list.append(downward_string)
    

    words_found = [] # same operation as with forward
    for a in range(len(downward_list)): 
        for b in range(len(words_list)): 
            find_column = downward_list[a].find(words_list[b]) 
            if find_column >= 0:
                found_word = [words_list[b],find_column,a] # (word,row,column)
                words_found.append(found_word)
    return [item for sublist in words_found for item in sublist]


if __name__ == "__main__":
    main()
