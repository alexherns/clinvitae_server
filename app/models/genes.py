def autocomplete(c, prefix):
    prefix = prefix + '%'
    print prefix

    c.execute("SELECT DISTINCT gene FROM variants WHERE gene LIKE ?", (prefix,))
    return c.fetchall()
