class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    @classmethod
    def get_hours(cls, employee):
        if employee.hours is None:
            employee.hours = (7 - employee.rest_days) * 8
        return employee
    
    @classmethod
    def get_email(cls, employee):
        if employee.email is None:
            employee.email = f"{employee.name}@email.com"
        return employee
    
    @classmethod
    def set_hourly_payment(cls, payment):
        cls.hourly_payment = payment
        return cls
    
    @classmethod
    def calculate_salary(cls, employee):
        employee = cls.get_hours(employee)
        employee.salary = employee.hours * cls.hourly_payment
        return employee

employee1 = EmployeeSalary('Evan', None, 2, None)

employee1 = EmployeeSalary.get_hours(employee1)
employee1 = EmployeeSalary.get_email(employee1)
employee1 = EmployeeSalary.calculate_salary(employee1)

print(employee1.hours)
print(employee1.email)
print(employee1.salary)