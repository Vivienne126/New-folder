class Employee:
    def __init__(self):
        print("Employee created")
    def _del_(self):
        print("Destructor called")
def create_object():
    print("Making object")
    obg=Employee()
    print("Fuction Ends")
    return obg
obg=create_object()