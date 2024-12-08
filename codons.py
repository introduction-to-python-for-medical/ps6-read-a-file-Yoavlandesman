def create_codon_dict(file_path):
    file = open(file_path)
    rows = file.readlines()
    file.close()
    d = {}
    for row in rows:
        row_parts = row.strip().split('\t')
        codon = row_parts[0]
        amino_acid = row_parts[2]
        d[codon] = amino_acid
    return d


