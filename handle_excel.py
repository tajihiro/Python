import os
import fnmatch
import xlrd
import xlwt

FILE_PATH = './assets'

# File読み込み
def read_excel(file):
  ex_book = xlrd.open_workbook(FILE_PATH + '/' + file)
  print('----------')
  print(str(file))
  print('----------')
  sheet = ex_book.sheet_by_index(0)
  print(sheet.name)
  #Excel内容取得
  for col in range(sheet.ncols):
    for row in range(sheet.nrows):
      print(sheet.cell(row, col).value)

# File書き込み
def write_excel():
  ex_book = xlwt.Workbook()
  new_sheet = ex_book.add_sheet('sheet1')
  ex_book.save(FILE_PATH + '/' + 'new_book.xls')

if __name__ == '__main__':
  files = os.listdir('./assets')
  for file in files:
    print(file)
    if fnmatch.fnmatch(file, '*.xlsx') or fnmatch.fnmatch(file, '*.xls') :
      read_excel(file)
  write_excel()
