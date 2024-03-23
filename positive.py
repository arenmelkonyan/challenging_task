from challenging_task.person import Person

class Positive(Person):
    def greet(self,other_person):
        return f"Hello, {other_person.name}"