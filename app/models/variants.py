def search(c, gene=None):
    c.execute('SELECT * FROM variants WHERE gene = ?', (gene,))
    return [{key: row[key] for key in row.keys()} for row in c.fetchall()]
