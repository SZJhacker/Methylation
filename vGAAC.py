#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import argparse, sys, re

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
    
def propertygroup(name):
    amphipathy = {
        'hydrophobicity': 'FIWLVMYCA',
        'moderate': 'THGSQ',
        'hydrophily': 'RKNEDP'
    }

    charge = {'positve': 'RK', 'neutral': 'NQSTCMAVGILFPWYH', 'negative': 'DE'}

    structure = {
        'aliphatic_group': 'GAVLISTCMDENQKR',
        'aromatic_group': 'FYW',
        'heterocyclics': 'HP'
    }

    polarity = {
        'polar': 'NQSTY',
        'nonpolar': 'ACGILMFPWV',
        'basic_polar': 'RHK',
        'acidic_polar': 'DE'
    }

    return eval(name)

def savefile(content, filename, separator):
    with open(filename, 'w') as f:
        if content == 0:
            print("descriptor calculation failed.")
            exit()
        else:
            for t in content:
                f.write(separator.join(t)+'\n')

def GAAC(fasta, group):
    groupkey = group.keys()

    encodings = []
    header = ['#']
    for key in groupkey:
        header.append(key)
    encodings.append(header)

    for i in fasta:
        name, sequence = i[0], i[1]
        code = [name]
        for i in header[1:]:
            aa_count = 0
            for aa in group[i]:
                aa_count += sequence.count(aa)
            code.append(str(aa_count / len(sequence)))
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
        choices=['amphipathy', 'charge', 'structure', 'polarity'], required=True)
    args = parser.parse_args()
    fasta = readFasta(args.inputfile)
    group = propertygroup(args.group)
    encodes = GAAC(fasta, group)
    savefile(encodes, args.outfile, args.separator.encode('utf-8').decode('unicode_escape'))