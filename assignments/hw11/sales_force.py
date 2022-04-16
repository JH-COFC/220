"""
Name: Jordan Herder
This assignment is entirely my own work.

Creates the SalesForce object class, a list of SalesPeople, which contains methods for:
Adding data to the object from a file
Providing information on if employees have beaten a sales quota
Returning the top seller(s)
Returning the employee with a given employee id
Returning the frequency of particular sale amounts

"""


from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, 'r').readlines()
        for line in file:
            split_line = line.split(', ')
            sales_list = split_line[2].split()
            for i in range(len(sales_list)):
                sales_list[i] = eval(sales_list[i])
            new_sales_person = SalesPerson(int(split_line[0]), split_line[1])
            for j in sales_list:
                new_sales_person.enter_sale(j)
            self.sales_people.append(new_sales_person)

    def quota_report(self, quota):
        report = []
        for seller in self.sales_people:
            individual = []
            individual.append(seller.get_id())
            individual.append(seller.get_name())
            individual.append(seller.total_sales())
            if seller.total_sales() >= quota:
                individual.append(True)
            else:
                individual.append(False)
            report.append(individual)
        return report

    def top_seller(self):
        top_sales = []
        for seller in self.sales_people:
            if not top_sales:
                top_sales.append(seller)
            elif seller.total_sales() > top_sales[0].total_sales():
                top_sales[0] = seller
            elif seller.total_sales() == top_sales[0].total_sales():
                top_sales.append(seller)

        return top_sales

    def individual_sales(self, employee_id):
        for seller in self.sales_people:
            if employee_id == seller.get_id():
                return seller
        return None

    def get_sale_frequencies(self):
        sales = {}
        for seller in self.sales_people:
            for sale in seller.get_sales():
                sales[sale] = sales.get(sale, 0) + 1
        return sales
