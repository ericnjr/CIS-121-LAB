#Question 19  ##############
def is_acronym(s, words):
    if len(s) != len(words):   # sees if the lengths match, abc, apples bananas, carrots
        return False
    acronym = ""
    for word in words:
        if not word:   #empty string check
            return False
        acronym += word[0]
    return acronym == s   #checks if acronym built matches the string s therefor returning True
print(is_acronym("abc", ["alice", "bob", "charlie"]))
print(is_acronym("a", ["an", "apple"]))                
print(is_acronym("ngguoy", ["never", "gonna", "give", "up", "on", "you"]))  
print(is_acronym("ab", ["apple", "banana", "cat"]))     
print(is_acronym("ab", ["apple", "", "cat"])) 













#Question 17  ###########
def get_indices(lst, item):
    indices = []
    for i, value in enumerate(lst):
        if value == item:
            indices.append(i)
    return indices
print(get_indices([1, 5, 5, 2, 7], 7))    
print(get_indices([1, 5, 5, 2, 7], 5))          
print(get_indices([1, 5, 5, 2, 7], 8))         
print(get_indices(["a","a","b","a","b","a"], "a"))














#Question 14 ##################
def progress_days(miles):
    count = 0
    for i in range(1,len(miles)):
        if miles[i] > miles[i-1]:
            count += 1
    return count
print(progress_days([3, 4, 1, 2]))    
print(progress_days([10, 11, 12, 9, 10])) 
print(progress_days([6, 5, 4, 3, 2, 9]))  
print(progress_days([9, 9]))
 








#Question 15 #############
def lag_days(miles):
    count = 0
    for i in range(1,len(miles)):
        if miles[i] < miles[i-1]:
            count += 1
    return count
print(lag_days([5, 3, 2, 1]))    
print(lag_days([10, 11, 12, 9, 10])) 
print(lag_days([6, 5, 4, 3, 2, 9]))  
print(lag_days([9, 9]))









#Question 11 ###############
def add_lists(lyst1, lyst2):
    result = []
    for i in range(len(lyst1)):
        result.append(lyst1[i] + lyst2[i])
    return result
print(add_lists([1, 3, 3, 1], [4, 3, 6, 1]))      
print(add_lists([1, 8, 5, 0, -7], [0, -7, 4, 2, -6])) 
print(add_lists([1, 2], [-1, 1])) 






#Question 16 #################
def like_or_dislike(events):
    state = "nothing"
    for event in events:
        if state == event:
            state = "nothing"
        else:
            state = event
    return state
print(like_or_dislike(["dislike"]))                  
print(like_or_dislike(["like", "like"]))         
print(like_or_dislike(["dislike", "like"]))         
print(like_or_dislike(["like", "dislike", "dislike"]))

