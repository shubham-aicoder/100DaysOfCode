def check_anagram(sentence_1,sentence_2):
    #write your code here
    sentence_1=sentence_1.lower().replace(" ","")
    sentence_2=sentence_2.lower().replace(" ","")
    
    
    if len(sentence_1)==0 and len(sentence_2)==0:
        return True
    for i in sentence_2:
        if sentence_1.find(i)==-1:
            return False
        else:
            sentence_1=sentence_1.replace(i,'',1)
            if len(sentence_1)==0:
                return True
            
    
    

if __name__ == "__main__":
  sentence_1 = ""
  sentence_2 = ""
  print(check_anagram(sentence_1,sentence_2))




