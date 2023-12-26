# comparisons_with_operators

age = 21
has_invitation = False
son_of_the_owner = True
print((age >= 21) and (has_invitation == True))
print((age >= 21) or (has_invitation == True))
# over 21 and has an invitation or is the son of the owner
print((age > 21 and has_invitation == True) or (son_of_the_owner == True))

# Exercise

of_legal_age = True
has_work_card = True
is_currently_working = True
has_own_vehicle = False
# you can only work here if you are of legal age and have a work card
print((of_legal_age == True) and (has_work_card == True))
print((of_legal_age and has_work_card))
# we want to hire people who do not yet have their own vehicle, but already have a work card
print((has_own_vehicle == False) and (
    has_work_card == True))
