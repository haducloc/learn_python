# Define Person class
class Person:

    # Static members (or static variables)
    TOTAL_PERSON_CREATED = 0

    # special function to create Person instance
    # each Person: has 2 instance members: name & age (or instance variables)

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # If this function called -> A new person created -> Increase TOTAL_PERSON_CREATED
        Person.TOTAL_PERSON_CREATED += 1

    @classmethod
    def get_total_persons_created(cls):
        # cls references to Person type
        return cls.TOTAL_PERSON_CREATED

# Create Persons

loc = Person("Loc", 42) ## __init__ will be called
fam = Person("Pham", 41) ## __init__ will be called

# Access Static Variables
print(f"Total of persons created: {Person.TOTAL_PERSON_CREATED}")

# Access Static Methods
print(f"Total of persons created: {Person.get_total_persons_created()}")

## Access Static Members:   ClassName.StaticMember
