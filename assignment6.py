

def ds(name="Prabhat",roll=5):
    l1 = [name,roll]
    t1 = (name,roll)
    s1 = {name,roll}
    d1 = {"name":name,"roll_no":roll}
    print("List: ",l1)
    print("Tuple: ",t1)
    print("Set:",s1)
    print("Dictionary: ",d1)
    print("Data Structures after changes......")
    l1.append(6)
    print("List after changes: ",l1)
    t1=("Prateek",9)
    print("Tuple after changes: ",t1)
    s1.remove("Prabhat")
    print("Set after changes:",s1)
    d1.update({"name1":"Poojary"})
    print("Dictionary after changes: ",d1)
    del l1
    del t1
    del s1
    del d1
    print("All the Data Structures are deleted.....")
ds()
