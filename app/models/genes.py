def autocomplete(c, prefix):
    c.execute("SELECT DISTINCT gene FROM variants WHERE gene LIKE ?", (prefix.upper() + '%',))
    return [row['gene'] for row in c.fetchall()]
