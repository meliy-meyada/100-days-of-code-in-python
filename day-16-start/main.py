import turtle

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Sqirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align["Pokemon Name"] = "l"


print(table)






