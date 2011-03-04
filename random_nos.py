#! usr/bin/python
# This program is used to generate the random numbers. There are two input parameter- (n,N)
# This program will return the set of n different numbers in (0,N). The generated output is intergers only.

from tempfile import TemporaryFile
from xlwt import Workbook
book = Workbook()
sheet1 = book.add_sheet('Sheet 1')
sheet1.write(0,0,1)
sheet1.write(0,1,1)
#row1 = sheet1.row(1)
#row1.write(0,2)
#row1.write(1,2)
#sheet1.col(0).width = 10000
book.save('simple.xls')
book.save(TemporaryFile())
