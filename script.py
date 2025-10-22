"""
OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON - COMPREHENSIVE GUIDE
==================================================================

Object-Oriented Programming allows developers to model real-world entities
and their interactions through classes and objects. This guide covers:
1. Basic class structure and instantiation
2. Constructors and the __init__ method
3. Instance vs Static attributes
4. Encapsulation (public, protected, private)
5. Properties (getters and setters)
6. Class methods and static methods
7. Inheritance

Author: Godswill
Purpose: Learning and reference material for OOP concepts
"""

from datetime import datetime


# =============================================================================
# SECTION 1: BASIC CLASS STRUCTURE
# =============================================================================
"""
A class is a blueprint for creating objects. Think of it like an architectural
plan for a house - the plan itself isn't a house, but you can build many houses
from that same plan.
"""

class Dog:
    """
    Represents a dog with basic attributes and behaviors.
    
    This demonstrates:
    - Constructor (__init__) for initializing object state
    - Instance attributes (unique to each dog object)
    - Instance methods (behaviors that dogs can perform)
    - Object relationships (Dog has an Owner)
    """
    
    def __init__(self, name, breed, age, owner):
        """
        Constructor method - automatically called when creating a new Dog object.
        
        Args:
            name (str): The dog's name
            breed (str): The dog's breed
            age (int): The dog's age in years
            owner (Owner): Reference to the Owner object who owns this dog
        """
        # Instance attributes - each dog object will have its own unique values
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner  # Composition: Dog "has-a" Owner
    
    def bark(self):
        """Makes the dog bark. Demonstrates a simple instance method."""
        print(f"{self.name} says: Woof! Woof!")
    
    def get_info(self):
        """
        Returns formatted information about the dog.
        
        Returns:
            str: A descriptive string about the dog
        """
        return f"{self.name} is a {self.age}-year-old {self.breed}"


class Owner:
    """
    Represents a dog owner with contact information.
    
    Demonstrates:
    - Separate class for related entities
    - How objects can reference each other
    """
    
    def __init__(self, name, address, contact):
        """
        Initialize an owner with their details.
        
        Args:
            name (str): Owner's full name
            address (str): Owner's residential address
            contact (str): Owner's phone number
        """
        self.name = name
        self.address = address
        self.contact = contact
    
    def introduce(self):
        """Prints an introduction from the owner."""
        print(f"Hi, I'm {self.name} and I have a dog!")


# Example usage: Creating objects and demonstrating relationships
print("=" * 60)
print("SECTION 1: BASIC CLASSES AND OBJECT RELATIONSHIPS")
print("=" * 60)

owner1 = Owner("Godswill", "Nairobi, Kenya", "0740275539")
dog1 = Dog("Nola", "Husky", 5, owner1)

# Accessing nested object properties (dog -> owner -> name)
print(f"{dog1.owner.name} is the owner of {dog1.name}")
print(dog1.get_info())
dog1.bark()
owner1.introduce()
print()


# =============================================================================
# SECTION 2: THE 'self' PARAMETER
# =============================================================================
"""
'self' is a reference to the current instance of the class.
It allows each object to access its own attributes and methods.

Think of 'self' as saying "this particular person" when you have multiple
Person objects - it distinguishes which person you're talking about.
"""

class Person:
    """
    Simple Person class demonstrating the importance of 'self'.
    
    Key Concept: Without 'self', we couldn't distinguish between
    person1's name and person2's name.
    """
    
    def __init__(self, name, age):
        """
        Initialize a person with name and age.
        
        Args:
            name (str): Person's name
            age (int): Person's age
        
        Note: 'self' refers to the specific instance being created
        """
        self.name = name  # This instance's name
        self.age = age    # This instance's age
    
    def greet(self):
        """
        Prints a personalized greeting.
        
        'self' allows this method to access the name and age of the
        specific Person object that called this method.
        """
        print(f"Hello! My name is {self.name} and I'm {self.age} years old!")
    
    def have_birthday(self):
        """
        Increments the person's age by 1.
        Demonstrates how 'self' allows modifying instance state.
        """
        self.age += 1
        print(f"🎂 Happy Birthday {self.name}! You're now {self.age}!")


print("=" * 60)
print("SECTION 2: UNDERSTANDING 'self'")
print("=" * 60)

person1 = Person("Godswill", 20)
person2 = Person("Alice", 35)
person3 = Person("Bob", 40)

# Each person object has its own data
person1.greet()
person2.greet()
person3.greet()

# Modifying one object doesn't affect others
person1.have_birthday()
person1.greet()  # Only person1's age changed
print()


# =============================================================================
# SECTION 3: ENCAPSULATION - PUBLIC, PROTECTED, AND PRIVATE
# =============================================================================
"""
Encapsulation is about controlling access to an object's internal state.

Python Naming Conventions:
- public: attribute (no underscore) - accessible everywhere
- _protected: _attribute (single underscore) - "don't access directly, but you can"
- __private: __attribute (double underscore) - Python mangles the name to prevent access

Why? Prevents accidental modification and allows controlled access through methods.
"""

class BankAccount:
    """
    Demonstrates encapsulation with different access levels.
    
    Real-world analogy: You can check your balance (public), but you can't
    directly modify it - you must use deposit() or withdraw() methods.
    """
    
    # Class attribute (shared by all instances)
    bank_name = "Python National Bank"
    
    def __init__(self, account_holder, initial_balance=0):
        """
        Create a new bank account.
        
        Args:
            account_holder (str): Name of account holder
            initial_balance (float): Starting balance (default: 0)
        """
        self.account_holder = account_holder  # Public
        self._account_number = self._generate_account_number()  # Protected
        self.__balance = initial_balance  # Private - can't access directly!
    
    def _generate_account_number(self):
        """
        Protected method: generates a random account number.
        Convention: single underscore means "internal use, don't call directly"
        
        Returns:
            str: Generated account number
        """
        import random
        return f"ACC-{random.randint(10000, 99999)}"
    
    def deposit(self, amount):
        """
        Public method to deposit money.
        
        Args:
            amount (float): Amount to deposit
        
        Business Rule: Amount must be positive
        """
        if amount > 0:
            self.__balance += amount
            print(f"✓ Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("✗ Invalid amount. Must be positive.")
    
    def withdraw(self, amount):
        """
        Public method to withdraw money.
        
        Args:
            amount (float): Amount to withdraw
        
        Business Rules:
        - Amount must be positive
        - Can't withdraw more than current balance
        """
        if amount <= 0:
            print("✗ Invalid amount. Must be positive.")
        elif amount > self.__balance:
            print(f"✗ Insufficient funds. Balance: ${self.__balance:.2f}")
        else:
            self.__balance -= amount
            print(f"✓ Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
    
    def get_balance(self):
        """
        Getter method for private balance.
        
        Returns:
            float: Current account balance
        
        Note: This controlled access allows us to log who's checking the balance
        """
        print(f"[LOG] Balance accessed at {datetime.now().strftime('%H:%M:%S')}")
        return self.__balance


print("=" * 60)
print("SECTION 3: ENCAPSULATION")
print("=" * 60)

account = BankAccount("Godswill", 1000)
print(f"Account holder: {account.account_holder}")  # Public - OK
print(f"Account number: {account._account_number}")  # Protected - works but discouraged

# Try to access private balance directly - won't work as expected!
# print(account.__balance)  # This would cause AttributeError

# Correct way: use the public method
print(f"Current balance: ${account.get_balance():.2f}")
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Should fail - insufficient funds
print()


# =============================================================================
# SECTION 4: PROPERTIES (@property DECORATOR)
# =============================================================================
"""
Properties allow you to use method calls like attributes.
Benefits:
- Cleaner syntax (account.balance instead of account.get_balance())
- Can add validation when setting values
- Can compute values on-the-fly
"""

class User:
    """
    Demonstrates Python properties for elegant getters and setters.
    
    Use Case: User authentication system with email and password validation
    """
    
    def __init__(self, username, email, password):
        """
        Create a new user.
        
        Args:
            username (str): Unique username
            email (str): User's email address
            password (str): User's password (will be validated)
        """
        self.username = username
        self._email = email
        self._password = password
        self._last_login = None
    
    @property
    def email(self):
        """
        Getter for email.
        
        Returns:
            str: User's email address
        
        Using @property allows: user.email instead of user.get_email()
        """
        print("[LOG] Email accessed")
        return self._email
    
    @email.setter
    def email(self, new_email):
        """
        Setter for email with validation.
        
        Args:
            new_email (str): New email address
        
        Business Rule: Email must contain '@' symbol
        """
        if "@" in new_email and "." in new_email:
            self._email = new_email.lower().strip()
            print(f"✓ Email for '{self.username}' updated at {datetime.now().strftime('%H:%M:%S')}")
        else:
            print("✗ Invalid email format. Email not changed.")
    
    @property
    def password(self):
        """
        Getter for password.
        
        Returns:
            str: Masked password for security
        
        Security Note: Never return actual passwords, even in getters!
        """
        print("[LOG] Password accessed")
        return "*" * len(self._password)  # Return masked version
    
    @password.setter
    def password(self, new_password):
        """
        Setter for password with validation.
        
        Args:
            new_password (str): New password
        
        Business Rule: Password must be at least 8 characters
        Security Enhancement: Could add more rules (uppercase, numbers, symbols)
        """
        if len(new_password) >= 8:
            self._password = new_password
            print(f"✓ Password for '{self.username}' changed at {datetime.now().strftime('%H:%M:%S')}")
        else:
            print("✗ Password too short! Must be at least 8 characters.")
    
    def login(self):
        """Records a successful login."""
        self._last_login = datetime.now()
        print(f"✓ {self.username} logged in at {self._last_login.strftime('%Y-%m-%d %H:%M:%S')}")


print("=" * 60)
print("SECTION 4: PROPERTIES")
print("=" * 60)

user1 = User("Goddy", "goddy@gmail.com", "initial123")

# Using properties like attributes (clean syntax!)
print(f"Username: {user1.username}")
print(f"Email: {user1.email}")
print(f"Password: {user1.password}")  # Shows masked version

# Setting values triggers validation
user1.password = "short"  # Too short, will fail
user1.password = "NewSecurePass123"  # Valid, will succeed

user1.email = "invalid-email"  # Missing '@', will fail
user1.email = "newemail@example.com"  # Valid, will succeed

user1.login()
print()


# =============================================================================
# SECTION 5: CLASS (STATIC) ATTRIBUTES AND METHODS
# =============================================================================
"""
Instance Attributes: Unique to each object (e.g., each user has their own email)
Class Attributes: Shared by ALL instances (e.g., all users share the same user_count)

Use Class Attributes for:
- Counters (tracking how many objects created)
- Constants (values that don't change)
- Default configurations
"""

class SystemUser:
    """
    Enhanced user system with role-based access control.
    
    Demonstrates:
    - Class attributes for tracking statistics
    - Class methods for operations on the class itself
    - Static methods for utility functions
    """
    
    # Class attributes - shared across ALL instances
    user_count = 0
    dev_count = 0
    admin_count = 0
    regular_user_count = 0
    
    # Class constant
    VALID_ROLES = ["DEVELOPER", "ADMIN", "USER"]
    
    def __init__(self, username, email, role, password):
        """
        Create a new system user.
        
        Args:
            username (str): Unique username
            email (str): User's email
            role (str): User role (DEVELOPER, ADMIN, or USER)
            password (str): User password
        
        Side Effect: Updates class-level counters
        """
        self.name = username
        self._email = email
        self._role = role.upper()
        self._password = password
        self._created_at = datetime.now()
        
        # Update class-level statistics
        SystemUser.user_count += 1
        
        # Role-based counting
        if self._role == "DEVELOPER":
            SystemUser.dev_count += 1
        elif self._role == "ADMIN":
            SystemUser.admin_count += 1
        else:
            SystemUser.regular_user_count += 1
        
        print(f"✓ USER '{self.name.upper()}' created at {self._created_at.strftime('%H:%M:%S')}")
    
    @property
    def role(self):
        """
        Getter for user role.
        
        Returns:
            str: User's role
        """
        return self._role
    
    @role.setter
    def role(self, new_role):
        """
        Setter for role with validation.
        
        Args:
            new_role (str): New role to assign
        
        Business Rule: Role must be in VALID_ROLES
        """
        new_role = new_role.upper()
        if new_role in SystemUser.VALID_ROLES:
            old_role = self._role
            self._role = new_role
            print(f"✓ Role changed from {old_role} to {new_role}")
        else:
            print(f"✗ Invalid role. Must be one of: {', '.join(SystemUser.VALID_ROLES)}")
    
    @classmethod
    def get_statistics(cls):
        """
        Class method - operates on the class itself, not instances.
        
        Returns:
            dict: Statistics about all users in the system
        
        Note: Use @classmethod when you need to work with class-level data
        The 'cls' parameter refers to the class itself
        """
        return {
            "total_users": cls.user_count,
            "developers": cls.dev_count,
            "admins": cls.admin_count,
            "regular_users": cls.regular_user_count
        }
    
    @classmethod
    def create_admin(cls, username, email, password):
        """
        Class method factory - convenient way to create admin users.
        
        Args:
            username (str): Admin username
            email (str): Admin email
            password (str): Admin password
        
        Returns:
            SystemUser: New admin user object
        
        Pattern: Factory methods for creating specific types of objects
        """
        return cls(username, email, "ADMIN", password)
    
    @staticmethod
    def validate_email(email):
        """
        Static method - utility function that doesn't need class or instance data.
        
        Args:
            email (str): Email to validate
        
        Returns:
            bool: True if email appears valid
        
        Note: Use @staticmethod for utility functions related to the class
        but that don't need access to class or instance data
        """
        return "@" in email and "." in email and len(email) > 5
    
    @staticmethod
    def hash_password(password):
        """
        Static utility for password hashing simulation.
        
        Args:
            password (str): Plain text password
        
        Returns:
            str: Simulated hashed password
        
        Real Implementation: Use libraries like bcrypt or hashlib
        """
        # Simplified simulation - in production, use proper hashing!
        return f"hashed_{len(password)}_{password[:2]}***"
    
    def __str__(self):
        """
        String representation of the user object.
        
        Returns:
            str: Human-readable description
        
        Called when: print(user) or str(user)
        """
        return f"{self.name} ({self._role})"
    
    def __repr__(self):
        """
        Developer-friendly representation.
        
        Returns:
            str: Detailed object representation
        
        Called when: repr(user) or when viewing object in console
        """
        return f"SystemUser(name='{self.name}', role='{self._role}', email='{self._email}')"


print("=" * 60)
print("SECTION 5: CLASS ATTRIBUTES AND METHODS")
print("=" * 60)

# Create various users
user1 = SystemUser("Bob", "bob@gmail.com", "DEVELOPER", "dev123456")
user2 = SystemUser("Collymore", "colly@gmail.com", "DEVELOPER", "colly123456")
user3 = SystemUser("Erick", "erick@hotmail.com", "ADMIN", "admin123456")

# Using class method factory
user4 = SystemUser.create_admin("Steven", "steven@gmail.com", "steven123456")

user5 = SystemUser("John", "john@gmail.com", "USER", "user123456")
user6 = SystemUser("Alice", "alice@gmail.com", "USER", "alice123456")
user7 = SystemUser("Patrick", "patrick@gmail.com", "USER", "patrick123456")

print()

# Access class attribute directly from the class
print(f"📊 Total users created: {SystemUser.user_count}")
print()

# Use class method to get statistics
stats = SystemUser.get_statistics()
print("📊 SYSTEM STATISTICS")
print("=" * 60)
print(f"Total Users:    {stats['total_users']}")
print(f"Developers:     {stats['developers']}")
print(f"Admins:         {stats['admins']}")
print(f"Regular Users:  {stats['regular_users']}")
print()

# Display user table
print("👥 USERS AND THEIR ROLES")
print("=" * 60)
print(f"{'Username':<15} {'Role':<15} {'Email':<30}")
print("-" * 60)
for user in [user1, user2, user3, user4, user5, user6, user7]:
    print(f"{user.name:<15} {user.role:<15} {user._email:<30}")
print()

# Using static methods
print("🔧 STATIC METHOD EXAMPLES")
print("=" * 60)
test_email = "test@example.com"
print(f"Is '{test_email}' valid? {SystemUser.validate_email(test_email)}")
print(f"Hashed password: {SystemUser.hash_password('mypassword123')}")
print()


# =============================================================================
# SECTION 6: INHERITANCE
# =============================================================================
"""
Inheritance allows a class to inherit attributes and methods from another class.

Terminology:
- Parent/Base/Super class: The class being inherited from
- Child/Derived/Sub class: The class that inherits

Use Case: When you have a "is-a" relationship
Example: A Student "is-a" Person, an Admin "is-a" User
"""

class Employee:
    """
    Base class for all employees.
    
    Demonstrates:
    - Common attributes/methods for all employee types
    - Template for child classes to extend
    """
    
    employee_count = 0
    
    def __init__(self, name, employee_id, salary):
        """
        Initialize base employee attributes.
        
        Args:
            name (str): Employee name
            employee_id (str): Unique employee identifier
            salary (float): Base salary
        """
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self._hire_date = datetime.now()
        
        Employee.employee_count += 1
    
    def work(self):
        """Base work method - can be overridden by child classes."""
        print(f"{self.name} is working...")
    
    def get_salary(self):
        """
        Returns employee salary.
        
        Returns:
            float: Employee's salary
        """
        return self.salary
    
    def __str__(self):
        return f"{self.name} (ID: {self.employee_id})"


class Developer(Employee):
    """
    Specialized employee class for developers.
    
    Inherits from: Employee
    Adds: programming_language attribute and code() method
    Overrides: work() method with developer-specific behavior
    """
    
    def __init__(self, name, employee_id, salary, programming_language):
        """
        Initialize a developer.
        
        Args:
            name (str): Developer name
            employee_id (str): Employee ID
            salary (float): Base salary
            programming_language (str): Primary programming language
        """
        # Call parent class constructor
        super().__init__(name, employee_id, salary)
        
        # Add developer-specific attribute
        self.programming_language = programming_language
    
    def code(self):
        """Developer-specific method."""
        print(f"{self.name} is coding in {self.programming_language}...")
    
    def work(self):
        """
        Override parent's work() method.
        
        Method Overriding: Child class provides specific implementation
        """
        print(f"{self.name} is developing software using {self.programming_language}...")


class Manager(Employee):
    """
    Specialized employee class for managers.
    
    Inherits from: Employee
    Adds: team list and management methods
    """
    
    def __init__(self, name, employee_id, salary, department):
        """
        Initialize a manager.
        
        Args:
            name (str): Manager name
            employee_id (str): Employee ID
            salary (float): Base salary
            department (str): Department managed
        """
        super().__init__(name, employee_id, salary)
        self.department = department
        self.team = []  # List of employees managed
    
    def add_team_member(self, employee):
        """
        Add an employee to manager's team.
        
        Args:
            employee (Employee): Employee object to add
        """
        self.team.append(employee)
        print(f"✓ {employee.name} added to {self.name}'s team")
    
    def work(self):
        """Override work method for managers."""
        print(f"{self.name} is managing the {self.department} department...")
    
    def conduct_meeting(self):
        """Manager-specific method."""
        print(f"{self.name} is conducting a team meeting with {len(self.team)} members...")


print("=" * 60)
print("SECTION 6: INHERITANCE")
print("=" * 60)

# Create different employee types
dev1 = Developer("Alice Johnson", "DEV001", 80000, "Python")
dev2 = Developer("Bob Smith", "DEV002", 75000, "JavaScript")
manager1 = Manager("Carol Williams", "MGR001", 95000, "Engineering")

# Demonstrate inheritance
print(f"\nTotal employees: {Employee.employee_count}")
print()

# Each employee type has access to base class methods
print("💼 All employees working:")
dev1.work()  # Calls overridden method
dev2.work()  # Calls overridden method
manager1.work()  # Calls overridden method
print()

# Child classes have their own specific methods
print("⚡ Specialized methods:")
dev1.code()  # Developer-specific
manager1.add_team_member(dev1)
manager1.add_team_member(dev2)
manager1.conduct_meeting()  # Manager-specific
print()

# All employees inherit get_salary() from base class
print("💰 Salaries:")
print(f"{dev1.name}: ${dev1.get_salary():,.2f}")
print(f"{dev2.name}: ${dev2.get_salary():,.2f}")
print(f"{manager1.name}: ${manager1.get_salary():,.2f}")
print()


# =============================================================================
# SECTION 7: SPECIAL METHODS (MAGIC/DUNDER METHODS)
# =============================================================================
"""
Special methods in Python start and end with double underscores (__).
They allow your objects to interact with Python's built-in operations.

Common ones:
__init__: Constructor
__str__: String representation for users
__repr__: String representation for developers
__len__: Define behavior for len(object)
__eq__: Define equality comparison (==)
__lt__: Define less than comparison (<)
"""

class Product:
    """
    Demonstrates special methods for operator overloading.
    
    Makes custom objects behave like built-in types
    """
    
    def __init__(self, name, price, quantity):
        """Initialize a product."""
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        """User-friendly string representation."""
        return f"{self.name} - ${self.price:.2f} ({self.quantity} in stock)"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
    
    def __eq__(self, other):
        """
        Define equality based on name and price.
        
        Args:
            other (Product): Another product to compare
        
        Returns:
            bool: True if products are equal
        """
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price
    
    def __lt__(self, other):
        """
        Define "less than" based on price.
        
        Args:
            other (Product): Another product to compare
        
        Returns:
            bool: True if this product is cheaper
        """
        return self.price < other.price
    
    def __add__(self, other):
        """
        Define addition - combines quantities of same product.
        
        Args:
            other (Product): Another product
        
        Returns:
            Product: New product with combined quantity
        """
        if self.name == other.name and self.price == other.price:
            return Product(self.name, self.price, self.quantity + other.quantity)
        else:
            raise ValueError("Can only add same products")


print("=" * 60)
print("SECTION 7: SPECIAL METHODS")
print("=" * 60)

laptop1 = Product("Laptop", 999.99, 5)
laptop2 = Product("Laptop", 999.99, 3)
phone = Product("Phone", 599.99, 10)

print("📦 Products:")
print(laptop1)  # Uses __str__
print(phone)
print()

print("🔍 Comparisons:")
print(f"Laptop == Phone? {laptop1 == phone}")  # Uses __eq__
print(f"Phone < Laptop? {phone < laptop1}")  # Uses __lt__
print()

print("➕ Combining same products:")
combined = laptop1 + laptop2  # Uses __add__
print(f"Combined laptops: {combined}")
print()


# =============================================================================
# KEY TAKEAWAYS AND BEST PRACTICES
# =============================================================================
'''

🎯 KEY OOP PRINCIPLES:

1. ENCAPSULATION: Keep data private, expose through methods
   - Use _protected for internal use
   - Use __private for truly sensitive data
   - Use @property for elegant getters/setters

2. INHERITANCE: Reuse code through parent-child relationships
   - Use when there's an "is-a" relationship
   - Override methods for specialized behavior
   - Use super() to call parent methods

3. POLYMORPHISM: Different classes with same method names
   - work() means different things for Developer vs Manager
   - Allows treating different objects uniformly

4. ABSTRACTION: Hide complex implementation details
   - Users call deposit(), don't need to know how balance updates

🔧 BEST PRACTICES:

1. Use descriptive class names (PascalCase)
2. Use descriptive method names (snake_case)
3. Document with docstrings
4. Keep classes focused (single responsibility)
5. Use class attributes for shared data
6. Use instance attributes for unique data
7. Prefer composition over inheritance when appropriate
8. Make methods do one thing well

📚 WHEN TO USE WHAT:

- Instance Methods: Most common, work with instance data
- Class Methods: Factory methods, working with class-level data
- Static
'''