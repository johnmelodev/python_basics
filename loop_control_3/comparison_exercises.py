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

has_passport = False
ticket_purchased = False
underage = False

print((has_passport == True) and (underage == False))
print((has_passport and ticket_purchased) and not underage)

print((has_passport == True) or (
    underage == False and ticket_purchased == True))

print((not has_passport or ticket_purchased) and not underage)

print((has_passport == False) or (
    ticket_purchased == True and underage == False))
print((has_passport == True) and (
    ticket_purchased == True) and (underage == False))
