class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print('The name of the Restaurant is {} and it makes {}'.format(self.name, self.cuisine_type))
    
    def open_restaurant(self):
        print('The Restaurant is open')
        

restaurant = Restaurant('Wills Wings', 'Hot Wings')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

class Restaurant:

    def __init__(self, name, cuisine_type):
        
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):

        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()

class User:

    def __init__(self, first_name, last_name, username, email, location):
    
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
    
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):

        print(f"\nWelcome back, {self.username}!")

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()

class Restaurant:

    def __init__(self, name, cuisine_type):
        
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        
        self.number_served += additional_served


restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 500
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1000)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(250)
print(f"Number served: {restaurant.number_served}")

class User:
    

    def __init__(self, first_name, last_name, username, email, location):
        
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        
        self.login_attempts += 1

    def reset_login_attempts(self):
        
        self.login_attempts = 0

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(f"  Login attempts: {eric.login_attempts}")

print("Resetting login attempts...")
eric.reset_login_attempts()
print(f"  Login attempts: {eric.login_attempts}")

class Restaurant:

    def __init__(self, name, cuisine_type):
        
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    

    def __init__(self, name, cuisine_type='ice cream'):
        
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()

class User:

    def __init__(self, first_name, last_name, username, email, location):
        
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        
        self.login_attempts += 1

    def reset_login_attempts(self):
        
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

eric.show_privileges()

class User:

    def __init__(self, first_name, last_name, username, email, location):
        
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        
        self.login_attempts += 1

    def reset_login_attempts(self):
        
        self.login_attempts = 0


class Admin(User):
    

    def __init__(self, first_name, last_name, username, email, location):
        
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()


class Privileges:
    

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()
