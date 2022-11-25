def show_table(hashtable):
    for i in range(len(hashtable)):
        print(i, end = " ")
        for j in hashtable[i]:
            print('-->', end = " " )
            print(j, end = '')
        print()
HashTable = [[] for _ in range(10)]
def Hashing(keyvalue):
    return keyvalue % len(HashTable)
def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)
def delete(Hashtable,keyvalue):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].pop()
def find(Hashtable, value):
    for i in range(len(Hashtable)):
        for j in Hashtable[i]:
            if value == j:
                for k in Hashtable[i]:
                    print('-->', end=" ")
                    print(k, end='')
insert(HashTable, 7, 'Allahabad')
insert(HashTable, 25, 'Mumbai')
insert(HashTable, 20, 'Mathura')
insert(HashTable, 9, 'Delhi')
insert(HashTable, 20, 'Punjab')
#show_table(HashTable)
find(HashTable, 'Punjab')
#delete(HashTable, 9)
#show_table(HashTable)
