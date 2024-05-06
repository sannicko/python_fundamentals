# this is an example of class Has-a relationship

from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
  def __init__(self):
    self.employees = []
    
  def add_employee(self, new_employee):
    self.employees.append(new_employee)
    
  def display_employees(self):
    print("Current Employees: ")
    for i in self.employees:
      print(i.first_name, i.last_name)
    print("_________________")
  
  def pay_employees(self): # define a method with no paremeters
    print("Paying Employees: ")
    for i in self.employees:
      print("Paycheck for: ", i.first_name, i.last_name)  
      print(f"Amount: ${i.calculate_paycheck():,.2f}")  #f string allows you to add variables to a string with the float and 2 decimals, add brackets .2f decimals
      print("______________")

def main():
  my_company = Company()
  
  employee1 = SalaryEmployee("Peter", "Pan", 50000)
  my_company.add_employee(employee1)
  employee2 = HourlyEmployee("Tynker", "Bell", 25, 50)
  my_company.add_employee(employee2)
  employee3 = HourlyEmployee("Jack", "Sparrow", 40, 15)
  my_company.add_employee(employee3)
  employee4 = CommissionEmployee("Candy", "Super", 30000, 5, 0.10)
  my_company.add_employee(employee4)
  my_company.display_employees()
  my_company.pay_employees() # calling the method


main()