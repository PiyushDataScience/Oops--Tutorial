# Initiate a class
class employee:
    def __init__(self, id, salary, designation):
        self.id = id
        self.salary = salary
        self.designation = designation

    def travel(self, destination):
        print(f"Employeee is travel to {destination}")


# create an object of the class
sam = employee(id="123", salary=30000, designation="manager")

sam.salary

sam.travel("London")
