current local directory: /c/xampp/htdocs/sanskrit-lexicon/Frish/fri_01/
** means further work required
# Step1. fri dictionary in cdsl system
1. Created a folder 'fri' in csl-orig/v02
  cd /c/xampp/htdocs/cologne/csl-orig
  git pull # sync local repo with github
  mkdir v02/fri
2. Copy latest fri.txt to csl-orig/v02/fri folder.
  cp /c/xampp/htdocs/sanskrit-lexicon/Frish/fri_01/fri_02.txt /c/xampp/htdocs/cologne/csl-orig/v02/fri/fri.txt
3. Add a blank file csl-orig/v02/fri_hwextra.txt.
  touch v02/fri/fri_hwextra.txt
4. ** Add a blank file csl-orig/v02/fri/fri-meta2.txt.
  touch v02/fri/fri-meta2.txt
5. ** Add a blank file csl-orig/v02/fri/friheader.xml
  touch v02/fri/friheader.xml
6. Create a folder csl-websanlexicon/v02/distinctfiles/fri/web/webtc.
  cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02/distinctfiles
  git pull
  mkdir fri
  mkdir fri/web
  mkdir fri/web/webtc
7. pdffiles.txt 
  python make_pdffiles.py pdffiles.txt   
  touch fri/web/webtc/pdffiles.txt
  It will have the following format. `pc:pdffilename` e.g. `011:0013.png'
  cp /c/xampp/htdocs/sanskrit-lexicon/Frish/fri_01/pdffiles.txt /c/xampp/htdocs/cologne/csl-websanlexicon/v02/distinctfiles/fri/web/webtc/pdffiles.txt
7a. the scanned image files are png format.
 file size info 6232 x 8942  (roughly 2 x 3(=)

  edit  /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/servepdfClass.php
  Add `'FRI' => "width ='1000' height='1300'",` to $imageParms.
7b. similar for csl-apidev application
 edit /c/xampp/htdocs/cologne/csl-apidev/servepdfClass.php
  Add `'FRI' => "width ='1000' height='1300'",` to $imageParms.


8. Add the following data in csl-pywork/v02/dictparms.py
   cd /c/xampp/htdocs/cologne/csl-pywork/v02
   git pull
```
"fri": {
  "dictup":"FRI",
  "dictlo":"fri",
  "dictname":u"Frisch Sanskrit Reader Vocabulary, 1956",
  "dictversion":"02",
 },
```
9. ** Add the following data in csl-websanlexicon/v02/dictparms.py
   cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
   git pull
```
 "fri":{
  "dictup":"FRI",
  "dictlo":"fri",
  "dictname":u"",
  "dictversion":"02",
  "dictyear":"2025",
  "dictaccent":False,
  "webtc2devatextoption":False,
  #"dictwc":"https://www.worldcat.org/title/halayudhas-abhidhanaratnamala-a-sanskrit-vocabulary/oclc/320893849",
  # "dictbe":u"HALĀYUDHA & JOSHĪ JAYAŚAṄKARA , Halāyudhakśa (Abhidhānaratnamālā) of Halāyudha",
  "dictwc":"TODO ", # **
  "dictbe":u"TODO ", # **
  "dicttitle":u"Frisch Sanskrit Reader Vocabulary, 1956",
 }
```
10. Add the following line to csl-pywork/v02/redo_cologne_all.sh.
cd  /c/xampp/htdocs/cologne/csl-pywork/v02
    `sh generate_dict.sh fri  ../../FRIScan/2025/`
11. Add the following line to csl-pywork/v02/redo_xampp_all.sh.
    `sh generate_dict.sh fri  ../../fri`
12. Add the following line to csl-websanlexicon/v02/redo_cologne_all.sh 
   `sh generate_web.sh fri  ../../FRIScan/2025/`
13. Add the following line to csl-websanlexicon/v02/redo_xampp_all.sh file.
   `sh generate_web.sh fri  ../../fri`
14. ** Modify csl-websanlexicon/v02/makotemplates/web/webtc/dictinfo.php.
    * add line to '$cologne_pdfpages_urls' associative array, e.g.
    * "FRI"=>"//www.sanskrit-lexicon.uni-koeln.de/scans/FRIScan/2025/web/pdfpages",
15. Modify csl-apidev/dictinfo.php, in two places:
   * To `$dictyear`, add e.g. `"FRI"=>"2025",`
   * To `$cologne_pdfpages_urls`, add same as in `14` above.
16. Modify csl-apidev/sample/dictnames.js, add line to `dictnames`, e.g.
   * `['FRI' , 'Frisch Sanskrit Reader Vocabulary, 1956'],`
17. Modify csl-apidev/simple-search/v1.1/parse_uri.php, add item to 
   * `$parmvalues['dict']`,  e.g. 'fri'
18. Modify hwnorm1/sanhw1/sanhw1.py in two places:
   * in `dictyear` array, add `"FRI":"2025,"`
   * in `san_spc_dicts` array, add `"FRI"`
     * for sanskrit-english dictionary, modify `san_en_dicts`
     * etc.
   * Note that the 'redo' procedure of hwnorm1/sanhw1 (see the readme therein)
     has to be redone after the pywork/v02 generate_dict script is run and
   * also the hwnorm1c.sqlite file has to be copied to csl-apidev, and
     csl-apidev has to be pushed in order for the csl-apidev displays to work
     for the new dictionary (displays such as simple-search and servepdf)

# Step1a redo local display and debug
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh fri  ../../fri
  * debug naked '<' in fri_01.txt, and recreate fri_02.txt and copy to csl-orig
  cp /c/xampp/htdocs/sanskrit-lexicon/Frish/fri_01/fri_02.txt /c/xampp/htdocs/cologne/csl-orig/v02/fri/fri.txt

<L>935<pc>44<k1>Ayata<k2>Ayata
āyata (pp. <yam)  -> ... 
Doing steps upto `sh generate_dict.sh fri  ../../fri` added the FRI dictionary for local usage.
But it did not have the line breaks properly displayed. It also did not have Sanskrit text properly marked up for transliteration facility. So, even with 'Devanagari' as output, I used to get 'SLP1' output only.


------------------------------------------------------

Following steps not applicable as of Feb 1, 2025

# Step2. Add markup.

1. Add the dictcode in the following lines in csl-pywork/v02/makotemplates/pywork. This will add `<s>` tag to the whole entry. This will allow the conversion to various transliteration schemes.

```python
%if dictlo in ['skd','vcp','fri']:
def adjust_slp1(x):
 # in skd, all text is Devanagari.  But, the text is skd.txt does not use
%endif
%if dictlo not in ['skd','vcp','sch','md','shs','wil','ap90','bur','acc','yat','fri']:
def unused_adjust_slp1(x):
 # in vcp, all text is Devanagari.  But, the text is vcp.txt does not use
```

```python
%if dictlo in ['vcp','fri']:
 x = adjust_slp1(x) # add <s> markup to text
```

```python
%if dictlo in ['fri']:
 x = re.sub(r'(.)$', '\g<1><br/>', x)
 x = adjust_slp1(x) # add <s> markup to text
%endif
````

# Step3. Image for local installation.


6. Create a folder `cologne/scans/fri/pdfpages` e.g. `cologne/scans/fri/pdfpages`. scans folder is sibling of `csl-orig` folder.
7. Put the single page PDFs in this folder.
9. Put the pdffiles.txt into csl-websanlexicon/v02/distinctfiles/fri/web/webtc

# Step 4. Images on sanskrit-lexicon-scans

1. Create a new repository fri in sanskrit-lexicon-scans organization.
2. Copy README.md from some other repository, and make changes in the dictionary name.
3. Copy single page PDF files generated earlier into pdfpages directory.
4. add, commit and push to the repository.


# Still not handled

1. csl-homepage
2. csl-doc

