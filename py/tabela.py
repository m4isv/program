from prettytable import PrettyTable
x = PrettyTable()



print('\n\n\n')
print(F"""\033[7;38m\t\tVERBO BE\033[m""")


x.field_names = ["PRONOME", "PRESENTE", "PASSADO","FUTURO"]

x.add_row(["I", "AM", "WAS", "WILL"])

x.add_row(["YOU", "ARE", "WERE", "WILL"])

x.add_row(["HE", "IS", "WAS", "WILL"])

x.add_row(["SHE", "IS", "WAS", "WILL"])

x.add_row(["IT", "IS", "WAS", "WILL"])

x.add_row(["WE", "ARE", "WERE", "WILL"])

x.add_row(["THEY", "ARE", "WERE", "WILL"])



print(F"\033[1;38m{x}\033[m")

