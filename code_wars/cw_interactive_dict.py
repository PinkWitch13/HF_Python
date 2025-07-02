"""In this kata, your job is to create a class Dictionary 
    which you can add words to and their entries. """


class Dictionary():

    def __init__(self):
        self.dict = {}
          
    def newentry(self, word, definition):
        self.key = self.word = word
        self.value = self.definition = definition
        if word not in self.dict:
            self.dict = {word : definition}
            return self.dict
        else:
            return "Word and definition allredy in"
        
    def look(self, key):
        defi = self.dict.get(key)
        if defi in self.dict:
            print(defi)
        else:
            print("Can't find such value")
        
        
    #     pass

d = Dictionary()

d.newentry('Apple', 'A fruit that grows on trees')

print(d)