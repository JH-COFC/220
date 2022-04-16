"""
Name: Jordan Herder
This assignment is entirely my own work.

Creates the class SalesPerson, which contains:
an integer employee id
a string employee name
a list of employee sales

Also contains methods to get name, id, and sales,
to set name, add a sale, and return the sum of sales,
and to compare total sales to another SalesPerson.

Also contains str() integration.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if quota > sum(self.sales):
            return False
        return True

    def compare_to(self, other):
        if other.total_sales() < sum(self.sales):
            return 1
        elif other.total_sales() == sum(self.sales):
            return 0
        return -1

    def __str__(self):
        return '{}-{}:{}'.format(self.employee_id, self.name, self.sales)
