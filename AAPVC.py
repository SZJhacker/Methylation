#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import argparse, os, re, sys
import pandas as pd
from data import readFasta, savefile

def readFasta(file):	
    with open(file) as f:
        records = f.read()

    if re.search('>', records) == None:
        print('The input file seems not in fasta format.')
        sys.exit(1)

    records = records.split('>')[1:]
    myFasta = []
    for fasta in records:
        array = fasta.split('\n')
        name, sequence = array[0].split()[0], ''.join(array[1:]).upper()
        myFasta.append([name, sequence])
    return myFasta
    
def savefile(content, filename, separator):
    with open(filename, 'w') as f:
        if content == 0:
            print("descriptor calculation failed.")
            exit()
        else:
            for t in content:
                f.write(separator.join(t)+'\n')

def amphipathy(fasta, group):
    value_path = os.path.split(os.path.realpath(__file__))[0] + '/property_value.csv'
    dataform = pd.read_csv(value_path, index_col=['scale'])
    dataform_header = list(dataform.columns.values)
    encodings = []
    header = ['#']

    for key in dataform_header:
        header.append(group + '_' + key)
    encodings.append(header)

    for i in fasta:
        name, sequence = i[0], i[1]
        code = [name]
        for aa in dataform_header:
            aa_number = sequence.count(aa) / len(sequence)
            code.append(str(aa_number * dataform[aa][group]))
        encodings.append(code)
    return encodings


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="feature extraction of protein physicochemical property",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '-i',
        '--inputfile',
        help="input file should be fasta format",
        required=True)
    parser.add_argument(
        '-o',
        '--outfile',
        help="output file, the format depend on 'separator' parameter",
        required=True)
    parser.add_argument(
        '-s',
        '--separator',
        help="the separator of out file, default symbol is commas",
        default=",")
    parser.add_argument(
        '-g',
        '--group',
        help="the group of protein physicochemical properties",
        choices=[
            'Kyte_Doolittle', 'Hopp_Woods', 'Cornette', 'Eisenberg', 'Rose',
            'Janin', 'Engelman'
        ],
        required=True)

    args = parser.parse_args()
    fasta = readFasta(args.inputfile)
    encodes = amphipathy(fasta, args.group)
    savefile(encodes, args.outfile, args.separator.encode('utf-8').decode('unicode_escape'))