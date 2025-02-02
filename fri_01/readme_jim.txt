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

<L>96<pc>14<K1>ajya</K1><K2>ajya</K2>
<K2>ajya absol. < 

 ' < ' occurs 684 times.
 The Mathematical Operators block (U+2200–U+22FF) contains characters for mathematical, logical, and set notation.
 ≺ u+227A PRECEDES

Replace ' < ' with ' ≺ '  (since '<' has special sense in xml)

-----------------------------------------
renumbering
The png files (in folder Frish-PNG) are slightly out of sync
with the 'pc' in fri.txt
Example <L>248<pc>19<k1>ananta<k2>ananta
The 'pc' value (e.g. 19) is the INTERNAL PAGE Number
This corresponds to '0021.png'
0021.
RULE:  <pc>N  <-> (N+2).png

Program to recreate pdffiles.txt
python make_pdffiles.py pdffiles.txt

We can rename the png files in sanskrit-lexicon-scans/FRI
  when this is created.

There are problems with pdffiles.txt --  (the index).

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
----------------------------------------
----------------------------------------
----------------------------------------

Installing fri in csl.
The code for dictionary is 'fri' ('FRI')
Adapt instructions based on 
 /sanskrit-lexicon/COLOGNE/readme_new_dict_addition.md

Instruction file name: readme_new_dict_fri.txt

We now have things working on local display.
Known things remaining to do.
1. scans
2. csl-homepage
3. csl-doc

