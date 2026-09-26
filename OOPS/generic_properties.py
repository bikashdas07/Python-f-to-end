class Human:
    hand = 2
    leg = 2
    head = 1
man = Human()
woman = Human()
#Accessing properties of a class using object reference.
print(man.hand, man.leg, man.head)
print(woman.hand,woman.leg,woman.head)

#Accessing properties of a class using class reference.
print(Human.hand, Human.leg, Human.head)
print(Human.hand,Human.leg,Human.head)

#Modifying properties of a class using object reference.
woman.hand=1
woman.leg=1
print(man.hand, man.leg, man.head)
print(woman.hand,woman.leg,woman.head)

#Modifying properties of a class using class reference.
Human.head = 2
print(man.hand, man.leg, man.head)
print(woman.hand,woman.leg,woman.head)
