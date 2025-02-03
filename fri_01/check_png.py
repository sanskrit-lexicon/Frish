"""
 check_png.py
"""
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

class PNG:
 def __init__(self,iline,line,ipng):
  self.iline = iline
  self.filename = line
  self.ipng = ipng
  
def make_pngrecs(lines):
 recs = []
 for iline,line in enumerate(lines):
  m = re.search(r'^([0-9][0-9][0-9][0-9])\.png$' , line)
  if m == None:
   print('UNEXPECTED=%s' % line)
   exit(1)
  ipng = int(m.group(1))
  rec = PNG(iline,line,ipng)
  recs.append(rec)
 return recs
                  
def check_sequence(pngrecs):
 nprob = 0
 for i,pngrec in enumerate(pngrecs):
  ipng = pngrec.ipng
  if i == 0:
   assert ipng == 3
   iprev = ipng
  elif ipng == (iprev + 1):
   # expected
   iprev = ipng
  else:
   nprob = nprob + 1
   print('sequence problem %s:' % nprob)
   pngrec_prev = pngrecs[i-1]
   print('prev : %s' % pngrec_prev.filename)
   print(' cur : %s' % pngrec.filename)
   iprev = ipng
   # exit(1)
 print('check_sequence finds %s problems' % nprob)
if __name__ == "__main__":
 filein = sys.argv[1] # pngfiles.txt
 fileout = sys.argv[2] # 
 # read the lines from filein
 lines = read_lines(filein)
 print('%s png files' % len(lines))
 pngrecs = make_pngrecs(lines)
 check_sequence(pngrecs)
 exit(1)
 print(len(oldrecs),'records')
 newrecs = make_newrecs(oldrecs)
 write_recs(fileout,newrecs)

 
