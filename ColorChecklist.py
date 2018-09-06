#print("Hello World")
checklist = list()
def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]
    checklist = ['Hello', 'World']
    checklist[1] = "Cats"
    print(checklist)

def update(index, item):
    checklist[index] = item
    checklist = ['Hello', 'World']
    checklist.pop(1)
    print(checklist)

def destroy(index):
    checklist.pop(index)
#tester
