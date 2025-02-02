"""
 recreate_01.py
"""
import csv
import sys, codecs, re

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
   for line in lines:
    f.write(line+'\n')
 print('%s lines written to %s' % (len(lines),fileout))

def write_recs(fileout,recs):
 # each rec is a list of strings
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   for line in rec:
    f.write(line+'\n')
 print('%s records written to %s' % (len(recs),fileout))

def read_lines(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def test1(filein,fileout):
 """
return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 4: charac
ter maps to <undefined>
"""
 # Open the TSV file and read its contents
 with open(filein, newline='') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
     print(row)
     exit(1)

def test2(filein,fileout):
 # read the lines
 lines = read_lines(filein)
 #
 reader = csv.reader(lines, delimiter='\t')
  
 rows = []
 for irow,row in enumerate(reader):
  print(row)
  if irow > 2:
   print('debug exit')
   exit(1)
  
def test3_rowcheck_1(rows):
 i0 = 0
 i1 = 2312
 i2 = 2313
 rownums = (0,2312,2313)
 rownums = (0,2312)
 trows = [rows[rownum] for rownum in rownums]
 lens = [len(row) for row in trows]
 m = max(lens)
 #print(m)
 #exit(1)
 NOVAL = 'NOVAL'
 for col in range(m):
  cvals = []
  cvals.append(str(col))
  for i in range(0,len(rownums)):
   row = trows[i]
   n = len(row)
   if col < n:
    val = row[col]
   else:
    val = NOVAL
   cvals.append(val)
  out = '  ::  '.join(cvals)
  print(out)

def test3_rowcheck(rows):
 """
8155 rows of length 17
1 rows of length 16

row 2314 has length 16
"""
 
 # rows is a list of lists
 d = {}
 for i,row in enumerate(rows):
  n = len(row)
  if n not in d:
   d[n] = 0
   print('row %s has length %s' % (i+1,n))
   print(row)
   print()
  d[n] = d[n] + 1
 # summary
 for n in d:
  count = d[n]
  print('%s rows of length %s' %(count,n))
 # what's wrong with line 2314?
 test3_rowcheck_1(rows)
 
def test3(filein,fileout):
 # read the lines
 lines = read_lines(filein)
 reader = csv.reader(lines, delimiter='\t')
  
 rows = []
 for irow,row in enumerate(reader):
  #print(row)
  #print('type of row=',type(row))  # a list
  rows.append(row)
 test3_rowcheck(rows)
 
def tsvread(lines):
 """  csv.reader handles quotation marks in some odd way.
  see readme_python_csv_quotationmarks.txt
  Thus, this function not used.
 """
 reader = csv.reader(lines, delimiter='\t') 
 rows = []
 for irow,row in enumerate(reader):
  #print(row)
  #print('type of row=',type(row))  # a list
  rows.append(row)
 return rows

def manual_tsvread(lines):
 """  csv.reader handles quotation marks in some odd way.
  see readme_python_csv_quotationmarks.txt
  Thus, this function not used.
 """
 rows = []
 ncols = None
 for iline,line in enumerate(lines):
  row = line.split('\t')
  if iline == 0:
   ncols = len(row)
  else:
   assert ncols == len(row)
   rows.append(row)
 return rows

def make_outlines(rows):
 recs = []
 for row in rows:
  # each row is a list of strings.
  # 1. concatenate
  line = ''.join(row)
  # 2. split on '@'
  rec = line.split('@')
  recs.append(rec)
 return recs
if __name__ == "__main__":
 filein = sys.argv[1] # a tsv file
 fileout = sys.argv[2]
 #test1(tsvfile,fileout)
 #test2(tsvfile,fileout)
 # test3(tsvfile,fileout)
 # read the lines from filein
 lines = read_lines(filein)
 # parse with csv.reader
 # rows = tsvread(lines)  
 rows = manual_tsvread(lines)
 outrecs = make_outlines(rows)
 write_recs(fileout,outrecs)

 
