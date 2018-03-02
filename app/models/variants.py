def search(c, gene=None):
    if not gene:
        raise Exception('Search by gene name')
    c.execute('SELECT * FROM variants WHERE gene = ?', (gene.upper(),))
    return [{key: row[key] for key in row.keys()} for row in c.fetchall()]
