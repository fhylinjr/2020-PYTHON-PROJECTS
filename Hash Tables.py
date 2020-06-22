class HashTables:
    def __init__(self, size):  # constructor which initializes object.
        self.size = size  # set number of buckets you want in your hashmap
        self.hashtable = self.create_buckets()  # creates hashtable with createbucket method.

    def create_buckets(self):
        return [[] for i in range(self.size)]  # return a mega list of smaller specified buckets.

    # Function to add or update items in hashmap.
    def set_value(self, key, value):
        hashed_index = hash(key) % self.size  # hash(key)%self.size uses modulo to bring the index stored in memory from
        # a larger number to an index contained in your bucket size.
        bucket = self.hashtable[hashed_index]  # this index is used to locate your bucket/ sub list in hash table
        found_key = False
        for index, record in enumerate(bucket):  # to loop through multiple items and index in a single sublist/ bucket
            record_key, record_value = record
            if key == record_key: # checks if key input equals key in bucket
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value)  # if found updates the item at current index
        else:
            bucket.append((key, value))  # if not appends item to bucket/ sublist in entire hashmap.

    # Function to retrieve value of a specified key in hashmap.
    def get_value(self, key):
        hashed_index = hash(key) % self.size
        bucket = self.hashtable[hashed_index]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if key == record_key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record value associated with specified email."

    # Function to remove item of specified key from hashmap
    def delete_value(self, key):
        hashed_index = hash(key) % self.size
        bucket = self.hashtable[hashed_index]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if key == record_key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
            return "Item deleted from bucket"
        else:
            return "No record value associated with specified email."

    def __str__(self):
        return "".join(str(item) for item in self.hashtable)  # removes commas separating sublists and joins them and
    #outputs hashmap as a string.


hashtable1 = HashTables(100)
print(hashtable1)
hashtable1.set_value('philip.boakye@minerva.kgi.edu', {'first_name': 'Philip', 'last_name': 'Boakye'})
hashtable1.set_value('evgeny@example.com', {'first_name': 'Evgeny', 'last_name': 'CoderElite'})
hashtable1.set_value('nwayoe@gmail.com', {'first_name': 'Nicholas', 'last_name': 'Wayoe'})
print(hashtable1)
print(hashtable1.get_value('nwayoe@gmail.com'))
print(hashtable1.delete_value('evgeny@example.com'))


