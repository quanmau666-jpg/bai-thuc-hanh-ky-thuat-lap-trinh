
f = open('D:/a.txt', 'r', encoding='utf-8')

char_count = 0  
word_count = 0  
line_count = 0 

for line in f:
    line_count += 1                 
    char_count += len(line)          
    words = line.split()            
    word_count += len(words)         

f.close()


print("The number of characters is:", char_count)
print("The number of words is:", word_count)
print("The number of lines is:", line_count)
