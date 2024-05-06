
class Employee:  # general employee class
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name


class SalaryEmployee(Employee): # derive from employee
  def __init__(self, first_name, last_name, year_salary):
    super().__init__(first_name, last_name) # call the general employee's init method and then pass in first name and last name with super().__init__ and passing (first_name, last_name) in parenthesis
    self.year_salary = year_salary
  
  def calculate_paycheck(self): # function to return the salary amount divided by 52 weeks
    return self.year_salary/52
  
# add hourly employee class

class HourlyEmployee(Employee): # this class enherit from general Employee clas
    def __init__(self, first_name, last_name, weekly_hours, hourly_rate):
        super().__init__(first_name, last_name)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate
    
    def calculate_paycheck(self):
      return self.weekly_hours*self.hourly_rate
    


# add comission employee class

class CommissionEmployee(SalaryEmployee):
  def __init__(self, first_name, last_name, year_salary, sales_num, commission_rate): # method add two more parms sales and commission
    super().__init__(first_name, last_name, year_salary)
    self.sales_num = sales_num   # initialize
    self.commission_rate = commission_rate   # initialize
    
  def calculate_paycheck(self):
    regular_salary = super().calculate_paycheck()
    total_commission = self.sales_num*self.commission_rate
    return regular_salary + total_commission
    