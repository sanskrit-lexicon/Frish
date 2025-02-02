"""
 make_pdffiles.py for FRI
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

def generate_oldrecs(lines):
 group = None
 for iline,line in enumerate(lines):
  if line.startswith('<LEND>'):
   group.append(line)
   yield group
   group = None
  elif line.startswith('<L>'):
   group = [line]
  elif group == None:
   print('skipping line # %s: %s' %(iline+1,line))
  else:
   group.append(line)

def make_02_meta(oldmeta):
 # <L>1<pc>11<K1>a</K1><K2>a</K2>
 m = re.search('<L>([^<]+)<pc>([^<]+)<K1>([^<]+)</K1><K2>([^<]+)</K2>$',oldmeta)
 if m == None:
  print('make_02_meta ERROR',oldmeta)
  exit(1)
 L = m.group(1)
 pc = m.group(2)
 k1 = m.group(3)
 k2 = m.group(4)
 newmeta = '<L>%s<pc>%s<k1>%s<k2>%s' %(L,pc,k1,k2)
 return newmeta

def make_02_lend(oldlend):
 assert oldlend == '<LEND>'
 newlend = oldlend
 return newlend

"""
body_regex_raw = r'^<K2>([^<]+)</K2>' +\
    r'<p><LANG n = "RUSSIAN">([^<]*)</LANG>' +\
    r'<p><LANG n = "ENGLISH">([^<]*)</LANG>' +\
    r'<p><LANG n = "CZECH">([^<]*)<p>$'
"""

body_regex_raw = r'^<K2>(.*?)</K2>' +\
    r'<p><LANG n = "RUSSIAN">(.*?)</LANG>' +\
    r'<p><LANG n = "ENGLISH">(.*?)</LANG>' +\
    r'<p><LANG n = "CZECH">(.*?)<p>$'

body_regex = re.compile(body_regex_raw)
print(body_regex_raw)

def check_body_1(a,b,c,meta):
 abc = a + b + c # string concat
 if abc == '':
  return False # no language definitions
 if not ((a != '') and (b != '') and (c != '')):
  print('check_body_1 WARNING at %s' % meta)
  print('a= "%s"\nb= "%s"\nc= "%s"' %(a,b,c))
 return True
  
def make_02_body(oldbody0,meta):
 # Replace ' < ' with ' ≺ '  # PRECEDS (math symbol)
 oldbody = oldbody0.replace(r' < ', ' ≺ ')
 m = re.search(body_regex,oldbody)
 if m == None:
  print('make_02_body ERROR',oldbody0)
  exit(1)
 iast = m.group(1)  
 russian = m.group(2).strip()
 english = m.group(3).strip()
 czech   = m.group(4).strip()
 newbody = []
 newbody.append(iast)
 if check_body_1(russian,english,czech,meta):
  newbody.append('<div n="1"/>1 <lang n="czech">%s</lang>' % czech)
  newbody.append('<div n="1"/>2 <lang n="russian">%s</lang>' % russian)
  newbody.append('<div n="1"/>3 <lang n="english">%s</lang>' % english)
 return newbody

def make_02_rec(oldrec):
 assert len(oldrec) == 3
 oldmeta = oldrec[0]
 oldbody = oldrec[1]
 oldlend = oldrec[2]
 newmeta = make_02_meta(oldmeta)
 newbodylines = make_02_body(oldbody,newmeta)
 newlend = make_02_lend(oldlend)
 newrec = []
 newrec.append(newmeta)
 for line in newbodylines:
  newrec.append(line)
 newrec.append(newlend)
 return newrec

def make_lines():
 """
  pc = 11  <--> 0013.png
  pc = 349 <--> 0351.png
 """
 lines = []
 for pc in range(11,350):
  n = pc+2
  filename = '%04d.png' % n
  pcstr = '%03d' % pc
  line = '%s:%s' %(pcstr,filename)
  lines.append(line)
 return lines
if __name__ == "__main__":
 fileout = sys.argv[1] # pdffiles.txt
 lines = make_lines()
 write_lines(fileout,lines)
 
 
