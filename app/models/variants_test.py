import pytest

from variants import search
from utils import make_test_string

def setup_test_variant(conn, gene, alias):
    conn.cursor().execute('INSERT INTO variants (gene, alias) VALUES (?, ?)', (gene,alias))
    conn.commit()

def teardown_test_variants(conn, gene):
    conn.cursor().execute('DELETE FROM variants WHERE gene = ?', (gene,))
    conn.commit()

def test_missing(conn):
    assert search(conn.cursor(), 'unknown_gene') == []

def test_invalid_params(conn):
    with pytest.raises(Exception) as excinfo:
        search(conn.cursor())

def test_found(conn):
    test_gene = make_test_string(10)
    test_alias1 = make_test_string(10)
    test_alias2 = make_test_string(10)

    try:
        setup_test_variant(conn, test_gene, test_alias1)
        setup_test_variant(conn, test_gene, test_alias2)

        # get results
        results = search(conn.cursor(), gene=test_gene)

        # confirm we have results only from this gene
        for result in results:
            assert result['gene'] == test_gene

        # confirm we have found all variants
        aliases = [result['alias'] for result in results]
        assert test_alias1 in aliases
        assert test_alias2 in aliases
        assert len(aliases) == 2
    finally:
        teardown_test_variants(conn, test_gene)
