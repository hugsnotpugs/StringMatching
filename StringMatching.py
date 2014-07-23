''' A Python implementation of the DiffLib SequenceMatcher 
   method, otherwise known as the Ratcliffe/Obershelp pattern matching algorithm '''

class StringCompare:
    
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2
    
    ### Step 2: Calculate the match ratio between two strings when they are entered as lists
    def string_calc(self, letter_list1, start1, end1, letter_list2, start2, end2):
        pos1 = 0
        pos2 = 0
        new_start1 = 0
        new_start2 = 0
        score = 0
    
        if start1 >= end1 or start2 >= end2 or start1 < 0 or start2 < 0:
            return score
        
        for pos1 in range(start1, end1):
            for pos2 in range (start2, end2):   
                        
                k = 0
                
                while letter_list1[pos1+k] == letter_list2[pos2+k]:
                    k += 1
                    if k > score:
                        new_start1 = pos1
                        new_start2 = pos2
                        score = k
                    if (pos1 + k) >= end1 or (pos2 + k) >= end2:
                        break
                        
        
        if score != 0:
            score += self.string_calc(letter_list1, new_start1 + score, end1, letter_list2, new_start2 + score, end2)
            score += self.string_calc(letter_list1, start1, new_start1 - 1, letter_list2, start2, new_start2 - 1)
        
        return score
    
    ### Step 1: Separates strings into lists and then calls the recursive string_calc method
    def string_ratio(self):
        letter_list1 = []
        letter_list2 = []
        
        if self.string1.upper() == self.string2.upper():
            result = 1
        else:
            length1 = len(self.string1)
            length2 = len(self.string2)
            if length1 == 0 or length2 == 0:
                result = 0
            else:
                letter_list1 = list((self.string1).upper())
                letter_list2 = list((self.string2).upper())
            
                result = (self.string_calc(letter_list1, 0, length1, letter_list2, 0, length2) * 2) / float(length1 + length2)

        return result
