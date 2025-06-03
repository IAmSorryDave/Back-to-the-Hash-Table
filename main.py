from CustomHashTables import TimeTravelHashTable

def main():
    
    tth = TimeTravelHashTable()
    tth.put("foo", 1, "car")
    tth.put("foo", 6, "jar")
    print(tth.get("foo", 3)) # 'Car'
    print(tth.get("foo", 1)) # 'Jar'
    print(tth.get("foo", 6)) # 'Car'
    print(tth.get("foo", 8)) # 'Jar'

if __name__ == "__main__":
    main()
