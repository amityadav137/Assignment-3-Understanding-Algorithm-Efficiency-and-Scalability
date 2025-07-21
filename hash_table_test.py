from hash_table import HashTable

def test_hash_table():
    ht = HashTable()

    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("orange", 30)

    print("Search apple:", ht.search("apple"))
    print("Search banana:", ht.search("banana"))

    ht.delete("apple")
    print("Search apple after delete:", ht.search("apple"))

if __name__ == "__main__":
    test_hash_table()
