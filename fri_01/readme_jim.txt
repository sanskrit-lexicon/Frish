01-31-2025

Ref: https://github.com/sanskrit-lexicon/frish/issues/3

@artanat provides links to 3 files:
1. fri_01.txt
2. readme.txt : renamed fri_01_readme.txt in this folder
3. Frish_Cologne.xlsx  : renamed fri_01_Frish_Cologne.xlsx in this folder
   Jim uploaded fri_01_Frish_Cologne.xlsx to Google docs.
     This is actually an spreadsheet.
     downloaded as 'tsv' (tab-separated-values) file: fri_01.tsv

------------------------------------------------------------
Jim thinks that fri_01.txt was created from the docx spreadsheet.
Attempt to write a Python program to reproduce (a copy of) fri_01.txt
from fri_01.tsv

python recreate_01.py fri_01.tsv temp_fri_01.txt
# The goal is that temp_fri_01.txt should be the same as fri_01.txt
# change to fri_01.tsv
  at line 2315, replace '' with "  -- otherwise, this line shows as 16 cols.


diff fri_01.txt temp_fri_01.txt | wc -l
# 0?

Oldřich Frisch,
Frisch, Oldřich (1903-1955). Sanskrit Reader [Text]

Номер страницы = Page number
фopмa = form

See readme_python_csv_quotationmarks.txt ---
Thus, recreate_01.py is best WiTHOUT csv.reader!

Typo in Frish_Cologne.xlsx:
  line 2314, column N
  old: "having a shining banner''
  new: "having a shining banner"
----------------------------------------------
# create fri_02.txt from fri_01.txt
python create_02.py fri_01.txt fri_02.txt
skipping line # 1: <TITLE>Friš Sanskrit Reader Vocabulary 1956
8155 records

----------------------------------------------
Instruction file name: readme_new_dict_fri.txt
  Follow these instructions for
  the various actions needed to install the Frish dictionary 
The code for dictionary is 'fri' ('FRI')
Instructions adapted from
 /sanskrit-lexicon/COLOGNE/readme_new_dict_addition.md

---------------------------------------------
Some adjustments to fri_02.txt required to
get xml validation.

<L>96<pc>14<K1>ajya</K1><K2>ajya</K2>
<K2>ajya absol. < 

 ' < ' occurs 684 times.
 The Mathematical Operators block (U+2200–U+22FF) contains characters for mathematical, logical, and set notation.
 ≺ u+227A PRECEDES

Replace ' < ' with ' ≺ '  (since '<' has special sense in xml)

-----------------------------------------

-------------------------------------------
creation of pdffiles.txt
 This is an 'index' file corresponding pc values from fri_02.txt
 e.g. '<pc>11' corresponds to scan image file '0013.png'
 The pc values (e.g. 11) corresponds to 'internal page number',
 e.g. to '0013.png'
 For the first few internal pages, the correspondence is <pc>N = (N+2).png
 We use this rule to create pdffiles.txt

python make_pdffiles.py pdffiles.txt

There are problems with this correspondence.
See discussion at '02-02-2025' below


----------------------------------------
syncing local repos with github

---- csl-orig

cd /c/xampp/htdocs/cologne/csl-orig
git pull
git add .
git commit -m "Initial CDSL version of Frish dictionary.
Ref: https://github.com/sanskrit-lexicon/frish/issues/3"
git push

---- csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git pull
git add .
git commit -m "Initial CDSL version of Frish dictionary.
Ref: https://github.com/sanskrit-lexicon/frish/issues/3"
git push

---- csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git pull
git add .
git commit -m "Initial CDSL version of Frish dictionary.
Ref: https://github.com/sanskrit-lexicon/frish/issues/3"
git push

---- csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev
git pull
git add .
git commit -m "Initial CDSL version of Frish dictionary.
Ref: https://github.com/sanskrit-lexicon/frish/issues/3"
git push

----------------------------------------
update cologne server
pull the repos:
  csl-orig, csl-pywork, csl-websanlexicon,
  csl-apidev
---- generate Frish displays
cd csl-pywork/v02
grep 'fri' redo_cologne

----------------------------------------
02-02-2025
Preparation for index checking

---------- check png filenames for sequencing:
 Expect to have file names 0003.png - 0351.png with no gaps
cd ../temp_Frish-PNG/
ls *.png > ../fri_01/pngfiles.txt
vf ../fri_01

python check_png.py pngfiles.txt check_png.txt
 349 png files
 from 0003.png - 0351.png inclusive (no gaps) =
  (351 - 2) = 349
  
 0003.png - 0010.png are 'preface' pages  (8)
 0345.png - 0351.png are 'afterword' pages (7)
 (334) other pages:
 internal page   1 is in 0011.png
 internal page 349 is in 0344.png

 (+ 8 7 334) = 349  check!

 From fri_02.txt,
   first pc value is 11
   last  pc value is 349
 Thus, we expect (349 - 11 + 1) = 339 distinct pc values in fri_02.txt

 Finally, we expect there to be a separate png for each pc value.

 So we have 334 png files, but expect 339 png files.

 So there appear to be 5 missing png files !!

------ check_pc
python check_pc.py fri_02.txt check_pc.txt
338 distinct pc numbers in fri_02.txt
 [NOTE: expeccted 339 pc values, but foundonly 338 in fri_02.txt
  
Also, check_pc finds 3 sequencing problems:
sequence problem 1:
prev : <L>3351<pc>143<k1>DAtrI<k2>DAtrI
 cur : <L>3377<pc>142<k1>DIvant<k2>DIvant
sequence problem 2:
prev : <L>3377<pc>142<k1>DIvant<k2>DIvant
 cur : <L>3404<pc>145<k1>DvajAhfta<k2>DvajAhfta
sequence problem 3:
prev : <L>7674<pc>327<k1>susaMkrudDa<k2>susaMkrudDa
 cur : <L>7729<pc>329<k1>sonmAda<k2>sonmAda

----- correct these sequence problems
cp fri_02.txt fri_03.txt

sequence Problem 1:
 a) internal page 142 is scan file 0137.png
    In fri_02.txt, the following records correctly marked <pc>142
     <L>3331<pc>142<k1>DApayati<k2>DApayati
     through
     <L>3331<pc>142<k1>DApayati<k2>DApayati
 
 b) in fri_02.txt, the following records are marked <pc>143
    <L>3351<pc>143<k1>DAtrI<k2>DAtrI
    through
    <L>3376<pc>143<k1>DIra<k2>DIra
 c) in fri_02.txt, 27 records INCORRECTLY MARKED as <pc>142
    <L>3377<pc>142<k1>DIvant<k2>DIvant
    through
    <L>3377<pc>142<k1>DIvant<k2>DIvant
 d) Change (in fri_03.txt)  <pc>142 to <pc>144 in these 27 records

   
 e) Jim did not find an image file for internal page 143 or 144
    - Jim examined image files 
----------------------------------------
Sequence Problem 2 solved by the change above

----------------------------------------
sequence problem 3:
prev : <L>7674<pc>327<k1>susaMkrudDa<k2>susaMkrudDa
 cur : <L>7729<pc>329<k1>sonmAda<k2>sonmAda

0322.png = internal page 327
corresponds to fri_02.txt
  <L>7674<pc>327<k1>susaMkrudDa<k2>susaMkrudDa
  through
  <L>7701<pc>327<k1>sUpAyana<k2>sUpAyana

0323.png = internal page 328
corresponds to fri_02.txt
  <L>7702<pc>327<k1>sUrya<k2>sUrya
  through
  <L>7728<pc>327<k1>sodara<k2>sodara
 There are 27 of these
 
And there are no <pc>328 in fri_02.txt.

CHANGE: in fri_03.txt
  change <pc>327 to <pc>328 in these 27 lines

----------------------------------------
Rerun check_pc program using fri_03.txt
python check_pc.py fri_03.txt check_pc.txt
339 distinct pc numbers in fri_03.txt
check_sequence finds no problems

----------------------------------------
install fri_03.txt both locally and at cologne
cp fri_03.txt /c/xampp/htdocs/cologne/csl-orig/v02/fri/fri.txt

---- do local install
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'fri' redo_xampp_all.sh
sh generate_dict.sh fri  ../../fri
sh xmlchk_xampp.sh fri
# ok

sync to Github
---- csl-orig

cd /c/xampp/htdocs/cologne/csl-orig
git pull
git add .
git commit -m "Frish dictionary based on fri_03.txt
Ref: https://github.com/sanskrit-lexicon/frish/issues/4"
git push

-----------------------------
install at Cologne

1. pull csl-orig
2. regenerate displays for fri
  cd csl-pywork/v02

# grep 'fri' redo_cologne_all.sh
sh generate_dict.sh fri  ../../FRIScan/2025/

  


*******************************************

We now have things working on local display.
Known things remaining to do.
1. scans
2. csl-homepage
3. csl-doc
