from openpyxl import Workbook
from openpyxl.styles import Alignment

def generatePO():
    workbook = Workbook()
    sheet = workbook.active

    sheet["A1"] = "Hong Infinity Insulated Glass Inc."
    sheet["C1"] = "Purchase Order"

    wrapText(sheet)
    
    workbook.save(filename="po_template.xlsx")

def wrapText(sheet):
    for row in sheet.iter_rows():
        for cell in row:
            cell.alignment = Alignment(wrap_text=True)
    

