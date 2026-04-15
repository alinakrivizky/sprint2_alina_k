class EmployeeSalary:
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    hourly_payment = 400
    def get_hours(self):
        if self.hours is None:
            self.hours = (7 - self.rest_days) * 8
        return self.hours
    def get_email(self):
        if self.email is None:
            self.email = f"{self.name}@email.com"
        return self.email
    def set_hourly_payment(self, payment):
        EmployeeSalary.hourly_payment = payment
    def calculate_salary(self):
        return self.get_hours() * self.hourly_payment
    
employee1 = EmployeeSalary('Evan', None, 2, None)
print(employee1.get_hours())
print(employee1.get_email())
print(employee1.calculate_salary())
employee2 = EmployeeSalary('Maria', 160, None, 'maria@email.com')
print(employee2.get_hours())
print(employee2.get_email())
print(employee2.calculate_salary())