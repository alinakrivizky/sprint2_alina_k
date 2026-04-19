class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours, rest_days, email, salary=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
        self.salary = salary
    @classmethod
    def get_hours(cls,name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, payment):
        cls.hourly_payment = payment
    
    def calculate_salary(self):
        self.hours = self.hours or (7 - self.rest_days) * 8
        self.salary = self.hours * self.hourly_payment
        return self
    
employee1 = EmployeeSalary('Evan', None, 2, None)

employee1 = EmployeeSalary.get_hours(
    employee1.name,
    employee1.hours,
    employee1.rest_days,
    employee1.email
)

employee1 = EmployeeSalary.get_email(
    employee1.name,
    employee1.hours,
    employee1.rest_days,
    employee1.email
)
employee1 = employee1.calculate_salary()

print(employee1.hours)
print(employee1.email)
print(employee1.salary)