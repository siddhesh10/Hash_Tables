#hash table are same as dictionary in python

class hash_tables(object):

    def __init__(self):
        self.hash_table=dict()

    def add_to_table(self,key,value):
        self.hash_table[str(key)]=str(value)

    def show(self):
        print(self.hash_table)

    def remove(self,key):
        try : del self.hash_table[str(key)]
        except: print("Key not present")
