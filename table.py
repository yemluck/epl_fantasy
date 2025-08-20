from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Age", "City", "Salary"]

table.add_row(["Alice", 25, "New York", 50000])
table.add_row(["Bob", 30, "London", 60000])
table.add_row(["Charlie", 35, "Paris", 55000])

print(table)