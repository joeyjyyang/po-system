from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Hong Infinity Insulated Glass"
sheet["C1"] = "Purchase Order"

workbook.save(filename="po_template.xlsx")
