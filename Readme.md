### vGAAC
“vGAAC.py” is a Python script that is used to extract the various grouped amino acid composition (vGAAC) features of protein sequences. We can use “-h” or “--help” to print a help message, as follows:

```bash
python3 vGAAC.py --help

usage: vGAAC.py [-h] -i INPUTFILE -o OUTFILE [-s SEPARATOR]
                [-g {amphipathy,charge,structure,polarity}]

feature extraction of protein physicochemical property

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        The name of inputfile, which should be fasta format
  -o OUTFILE, --outfile OUTFILE
                        The name of outfile
  -s SEPARATOR, --separator SEPARATOR
                        the separator of outfile, default symbol is commas
  -g {amphipathy,charge,structure,polarity}, --group {amphipathy,charge,structure,polarity}
                        the group of protein physicochemical properties
```
The script has a total of four parameters: “-i,” “-o,” “-s,” and “-g.” <br>
“-i” specifies the input file, “-o” specifies the output file, while “-s” specifies the delimiter of the output file. The default is a comma; “ g” specifies the groups of physical and chemical properties used for feature extraction, including amphipathy, charge, structure, and polarity groups. “-i,” “-o,” and “-g” are required parameters.<br>
For example, using the following command to extract protein features according to the “amphipathy” group:
```bash
python3 vGAAC.py -i infile.fa -g amphipathy -o outfile.csv 
```
or, using the following command to extract protein features according to the “charge” group

```bash
python3 vGAAC.py -i infile.fa -g charge -o outfile.csv 
```
or, using the following command to extract protein features according to the “structure” group

```bash
python3 vGAAC.py -i infile.fa -g structure -o outfile.csv 
```
or, using the following command to extract protein features according to the “polarity” group

```bash
python3 vGAAC.py -i infile.fa -g polarity -o outfile.csv 
```

### AAPVC
“AAPVC.py” is a Python script that is used to extract the amino acid property value Composition(AAPVC)features of protein sequences. We can use “-h” or “--help” to print a help message, as follows:
```bash
python3 AAPVC.py --help

usage: AAPVC.py [-h] -i INPUTFILE -o OUTFILE [-s SEPARATOR] -g
                {Kyte_Doolittle,Hopp_Woods,Cornette,Eisenberg,Rose,Janin,Engelman}

feature extraction of protein physicochemical property

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        input file should be fasta format
  -o OUTFILE, --outfile OUTFILE
                        output file, the format depend on 'separator'
                        parameter
  -s SEPARATOR, --separator SEPARATOR
                        the separator of out file, default symbol is commas
  -g {Kyte_Doolittle,Hopp_Woods,Cornette,Eisenberg,Rose,Janin,Engelman}, --group {Kyte_Doolittle,Hopp_Woods,Cornette,Eisenberg,Rose,Janin,Engelman}
                        the group of protein physicochemical properties
```
The script has a total of four parameters: “-i,” “-o,” “-s,” and “-g.” <br>
“-i” specifies the input file, “-o” specifies the output file, while “-s” specifies the delimiter of the output file. The default is a comma; “ g” specifies the groups of hydrophobic properties used for feature extraction, including Kyte_Doolittle, Hopp_Woods, Cornette, Eisenberg, Rose, Janin and Engelman. “-i,” “-o,” and “-g” are required parameters.<br>
For example, using the following command to extract protein features according to the “Kyte_Doolittle” group:
```bash
python3 AAPVC.py -i infile.fa -g Kyte_Doolittle -o outfile.csv 
```
or, using the following command to extract protein features according to the “Hopp_Woods” group

```bash
python3 AAPVC.py -i infile.fa -g Hopp_Woods -o outfile.csv 
```
or, using the following command to extract protein features according to the “Cornette” group

```bash
python3 AAPVC.py -i infile.fa -g Cornette -o outfile.csv 
```
or, using the following command to extract protein features according to the “Eisenberg” group

```bash
python3 AAPVC.py -i infile.fa -g Eisenberg -o outfile.csv 
```
or, using the following command to extract protein features according to the “Rose” group

```bash
python3 AAPVC.py -i infile.fa -g Rose -o outfile.csv 
```
or, using the following command to extract protein features according to the “Janin” group

```bash
python3 AAPVC.py -i infile.fa -g Janin -o outfile.csv 
```
or, using the following command to extract protein features according to the “Engelman” group

```bash
python3 AAPVC.py -i infile.fa -g Engelman -o outfile.csv 
```