# Multiple Inheritance
class Person:
    name = 'I am a person'

    def invite(self):
        print('Hello, I am a person. Shall we go to the event?')


class Professional:
    name = 'I am a professional'

    def invite(self):
        print('Hello, I am a professional. Shall we go to the event?')


class ProfessionalActor(Person, Professional):
    pass


# Usage example
professional_actor = ProfessionalActor()
professional_actor.invite()

# Check the method resolution order (MRO)
print(ProfessionalActor.mro())
