import queue

class FactoryConveyor:
    def __init__(self):
        self.conveyorBelt = queue.Queue()

    def add_item(self, item):
        self.conveyorBelt.put(item)

    def remove_item(self):
        self.conveyorBelt.get(self)

if __name__ == "__main__":
    belt = FactoryConveyor()

    belt.add_item("pink shoes")
    belt.add_item("red shoes")
    belt.add_item("green shoes")
    belt.add_item("black shoes")

    print(belt)

    print (f"removing item {belt.remove_item()}")
    print (f"removing item {belt.remove_item()}")



    
    # create a programe that changes from degrees celius to degress franheit.
    
    def conventor():
        celius_temp = float(input("Enter a the temperature: "))
        temp = celius_temp * 9/5 +32
        print({temp})
    
    conventor()


