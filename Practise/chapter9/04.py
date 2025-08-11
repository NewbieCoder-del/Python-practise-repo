word='donkey'
with open('file.txt','r') as f:
    content=f.read().lower()
contentnew=content.replace(word,'######')
with open('file.txt','w') as file:
    file.write(contentnew)



'''
#this is to find not just donkey but donkeys

    words = ['donkey', 'donkeys']  # list of words to replace

with open('file.txt', 'r') as f:
    content = f.read().lower()

for word in words:  # replace each word separately
    content = content.replace(word, '######')

with open('file.txt', 'w') as file:
    file.write(content)
'''