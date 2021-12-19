fo = open('test1.txt','wb')
plaintext = 'copied the data in to the file'
fo.write(bytes(plaintext,'UTF-8'))
fo.close
