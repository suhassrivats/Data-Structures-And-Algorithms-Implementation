"""
Assume there is a REST API available at "http://www.linkedin.corp/api" for
accessing employee information The employee information endpoint is
"/employee/<id>" Each employee record you retrieve will be a JSON object with
the following keys:

    'name'  refers to a String that contains the employee's first and last name
    'title' refers to a String that contains the employee's job title
    'reports' refers to an Array of Strings containing the IDs of the employee''s direct reports

Write a function that will take an employee ID and print out the hierarchy of
employees under that employee.

-----------Begin Sample Output--------------
Flynn Mackie - Senior VP of Engineering
  Wesley Thomas - VP of Design
    Randall Cosmo - Director of Design
      Brenda Plager - Senior Designer
  Nina Chiswick - VP of Engineering
    Tommy Quinn - Director of Engineering
      Jake Farmer - Frontend Manager
        Liam Freeman - Junior Code Monkey
      Sheila Dunbar - Backend Manager
        Peter Young - Senior Code Cowboy
-----------End Sample Output--------------
"""


import requests


# Recursive
def print_hierachy(employee_id, t=0):  # t stands for number of tabs
    url = 'https://my-json-server.typicode.com/khaledyousry/api/employee/' + str(employee_id)
    employee = requests.get(url)
    if employee.status_code == 200:
        employee_data = employee.json()
        print('  '*t, '%s - %s' % (employee_data['name'],
                                   employee_data['title']))
        t += 1
        for report_id in employee_data['report']:
            print_hierachy(report_id, t)


# Iterative
def print_hierachy_iterative(employee_id):
    employee = get_json_response(employee_id)
    if employee:
        stack = [(employee, 0)]
        while stack:
            employee_data, depth = stack.pop()
            print('  '*depth, '%s - %s' % (employee_data['name'],
                                           employee_data['title']))
            if employee_data['report']:
                for report_id in employee_data['report']:
                    stack.append((get_json_response(report_id), depth+1))


def get_json_response(employee_id):
    url = 'https://my-json-server.typicode.com/khaledyousry/api/employee/' + str(employee_id)
    employee = requests.get(url)
    if employee.status_code == 200:
        return employee.json()


# Recursive
# print_hierachy(4343)
# print_hierachy(6324)
# print_hierachy(4224)
# print_hierachy(9889)
# print_hierachy(1234)
# print_hierachy(6353)
# print_hierachy(3524)
# print_hierachy(7474)

# print('#' * 10)

# Iterative
print_hierachy_iterative(4343)
# print_hierachy_iterative(6324)
# print_hierachy_iterative(4224)
# print_hierachy_iterative(9889)
# print_hierachy_iterative(1234)
# print_hierachy_iterative(6353)
# print_hierachy_iterative(3524)
# print_hierachy_iterative(7474)
