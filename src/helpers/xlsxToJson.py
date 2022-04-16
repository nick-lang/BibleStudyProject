import openpyxl
import json


wb = openpyxl.load_workbook('pathTo/brb.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

bibleDictionary = {}

for row in range(4, sheet.max_row + 1):
    bookChapter = sheet['A' + str(row)].value
    verseText = sheet['C' + str(row)].value

    if bookChapter is not None:
        book = bookChapter.split()[-2]
        chapter = int(bookChapter.split()[-1])
        verseNum = 1
    else:
        verseNum += 1

    if book not in bibleDictionary:
        bibleDictionary[book] = {}
    if chapter not in bibleDictionary[book]:
        bibleDictionary[book][chapter] = {}
    if verseNum not in bibleDictionary[book][chapter]:
        bibleDictionary[book][chapter][verseNum] = verseText


# json_string = json.dumps(bibleDictionary)
# # print(bibleDictionary['Genesis'])
# print(json_string)
with open('json_data.json', 'w') as outfile:
    json.dump(bibleDictionary, outfile)


