# Define Person class
class Person:

    # special function to create Person instance
    # each Person: has 2 fields: name & age

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method - Return a text that describe this Person (self)
    def description(self):
        return f"Person name={self.name}, age={self.age}"

    # Instance method - Print Hi from this person (self) to the give person name.
    def introduce_to(self, toPerson):
        print(f"Hi {toPerson}! My name is {self.name}. I am {self.age} years old.")

    # Should this person retire?
    def should_retire(self):
        return True if self.age > 60 else False

# Use Person Class

# Create Person object/instance for Loc

loc = Person("Loc", 42) ## __init__ will be called
loc.introduce_to("Luke") ## Call introduce_to with toPerson = "Luke"

# Access instance variables
print(f"{loc.name} is {loc.age}")

# Create Person object/instance for Pham

fam = Person("Pham", 41) ## __init__ will be called
fam_desc = fam.description()
print(fam_desc)

# Should Loc retire?
print(f"Should {loc.name} retires: {loc.should_retire()}")
