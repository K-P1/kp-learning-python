from openpyxl import Workbook

wkbk = Workbook()

sheet = wkbk.active

sheet["A1"] = "Hello"
sheet["B1"] = "World"

wkbk.save(filename = "hw.xlsx")
print("Done")
