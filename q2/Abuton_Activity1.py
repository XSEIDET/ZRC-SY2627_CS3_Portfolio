
# ACTIVITY 1: Access Modifiers

# Situation 1:
# A GameCharacter class has a username that can be displayed and accessed by anyone.
# Access Modifier: Public (No underscore prefix)
class GameCharacter:
    def __init__(self, username):
        self.username = username  # Public attribute


# Situation 2:
# A BankAccount class has a balance that should NOT be accessed directly outside the class.
# Access Modifier: Private (Double underscore prefix)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute


# Situation 3:
# A Vehicle class has an engineCode that should only be accessed within the class and its subclasses.
# Access Modifier: Protected (Single underscore prefix)
class Vehicle:
    def __init__(self, engineCode):
        self._engineCode = engineCode  # Protected attribute


# Situation 4:
# A Student class has a schoolName that is safe for everyone to view and modify.
# Access Modifier: Public (No underscore prefix)
class Student:
    def __init__(self, schoolName):
        self.schoolName = schoolName  # Public attribute


# Situation 5:
# A VotingSystem class has a voterID that must be hidden for security reasons.
# Access Modifier: Private (Double underscore prefix)
class VotingSystem:
    def __init__(self, voterID):
        self.__voterID = voterID  # Private attribute