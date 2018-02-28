import sqlite3
import os
import sys

schema_file = sys.argv[1]
data_file = sys.argv[2]
db_file = sys.argv[3]

conn = sqlite3.connect(db_file)
c = conn.cursor()


schema = open(schema_file).read().strip()

with open(data_file) as f:
    headers = f.readline().strip().split('\t')
    headers = [header.replace(' ', '_').lower() for header in headers]
    c.execute(schema)
    for line in f:
        encoded = line.decode('latin1').strip().split('\t')
        var_holders = ', '.join(['?']*len(encoded))
        header_vars = ', '.join(headers[:len(encoded)])
        insertSql = 'INSERT INTO variants ({0}) VALUES ({1})'.format(
            header_vars,
            var_holders,
        )
        c.execute(insertSql, encoded)


conn.commit()
conn.close()
