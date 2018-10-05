import csv
from hashlib import sha256
def hash_password_hack(input_file_name, output_file_name):
    List = dict()
    for i in range(0, 10000):
        Num = '{:d}'.format(i).zfill(4)
        List[sha256(Num.encode('utf-8')).hexdigest()] = Num
    with open(input_file_name, 'r') as r, open(output_file_name, 'w') as o:
        reader = csv.reader(r)
        writer = csv.writer(o, lineterminator='\n')
        for row in reader:
            Print = (row[0], List[row[1]])
            writer.writerow(Print)

hash_password_hack('/home/zigmond/input.csv', '/home/zigmond/output.csv')
