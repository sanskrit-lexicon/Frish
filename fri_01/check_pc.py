"""
 check_pc.py
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

class PC:
 def __init__(self,iline,line,L,pc,k1,k2):
  self.iline = iline
  self.meta = line
  self.L = L
  self.pc = pc
  self.k1 = k1
  self.k2 = k2
  pcparts = self.pc.split('-')
  assert len(pcparts) in (1,2)
  self.pc1 = pcparts[0]
  if len(pcparts) == 2:
   self.pc2 = pcparts[1]
  else:
   self.pc2 = None
  self.ipage = int(self.pc1)
 
def make_pcrecs(lines):
 recs = []
 for iline,line in enumerate(lines):
  if not line.startswith('<L>'):
   continue
  m = re.search(r'^<L>([^<]*?)<pc>([^<]*?)<k1>([^<]*?)<k2>([^<]*)$',line)
  if m == None:
   print('meta error: line=\n',line)
   exit(1)
  L = m.group(1)
  pc = m.group(2)
  k1 = m.group(3)
  k2 = m.group(4)
  rec = PC(iline,line,L,pc,k1,k2)
  recs.append(rec)
 return recs
                  
def extract_first(pcrecs):
 # a generator
 for i,pcrec in enumerate(pcrecs):
  ipage = pcrec.ipage
  if i == 0:
   assert ipage == 11
   yield pcrec
   iprev = ipage
  elif ipage == iprev:
   pass
  else: # new ipage
   yield pcrec
   iprev = ipage

def check_sequence(pcrecs):
 nprob = 0
 for i,pcrec in enumerate(pcrecs):
  ipage = pcrec.ipage
  if i == 0:
   assert ipage == 11
   iprev = ipage
  elif ipage == (iprev + 1):
   # expected
   iprev = ipage
  else:
   nprob = nprob + 1
   print('sequence problem %s:' % nprob)
   pcrec_prev = pcrecs[i-1]
   print('prev : %s' % pcrec_prev.meta)
   print(' cur : %s' % pcrec.meta)
   iprev = ipage
   # exit(1)
 print('check_sequence finds no problems')
if __name__ == "__main__":
 filein = sys.argv[1] # fri_02.txt
 fileout = sys.argv[2] # 
 # read the lines from filein
 lines = read_lines(filein)
 pcrecs = make_pcrecs(lines)
 pcrecs1 = list(extract_first(pcrecs))
 print('%s distinct pc numbers in %s' %(len(pcrecs1),filein))
 check_sequence(pcrecs1)
 exit(1)
 print(len(oldrecs),'records')
 newrecs = make_newrecs(oldrecs)
 write_recs(fileout,newrecs)

 
