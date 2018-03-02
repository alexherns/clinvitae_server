from genes import autocomplete
from utils import make_test_string

def setup_test_gene(conn, gene):
    conn.cursor().execute('INSERT INTO variants (gene) VALUES (?)', (gene,))
    conn.commit()

def teardown_test_gene(conn, gene):
    conn.cursor().execute('DELETE FROM variants WHERE gene = ?', (gene,))
    conn.commit()

def test_missing(conn):
    assert autocomplete(conn.cursor(), 'unknown_prefix') == []

def test_found(conn):
    test_gene = make_test_string(10)

    try:
        setup_test_gene(conn, test_gene)
        for substr_size in range(len(test_gene)):
            assert test_gene in autocomplete(conn.cursor(), test_gene[:substr_size])
    finally:
        teardown_test_gene(conn, test_gene)
