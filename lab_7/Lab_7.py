class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    def get_info(self):
        return f"{self.name}, ID: {self.emp_id}"

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department
    def manage_project(self):
        return f"{self.name} управляет проектом в отделе {self.department}."

class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization
    def perform_maintenance(self):
        return f"{self.name} выполняет техническое обслуживание ({self.specialization})."

class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []
    def add_employee(self, employee):
        self.team.append(employee)
    def get_team_info(self):
        print("Команда тех-менеджера:")
        for emp in self.team:
            print(" -", emp.get_info())
tm = TechManager("Kristian", 1, "IT", "Network")
emp1 = Employee("Joseph", 2)
emp2 = Technician("Eric", 3, "Electronics")
emp3 = Manager("Kenny", 4, "HR")
tm.add_employee(emp1)
tm.add_employee(emp2)
tm.add_employee(emp3)
print(tm.manage_project())
print(tm.perform_maintenance())
tm.get_team_info()
