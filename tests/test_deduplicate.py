
import pytest
import sys
import pandas as pd

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DAG_DIR = ROOT / 'dags'

if DAG_DIR not in sys.path:
    sys.path.insert(0, DAG_DIR.as_posix())

from etl.common.deduplicate import deduplicate

from unittest.mock import patch

# Create a fixture to consolidate a testing dataframe before running the test
@pytest.fixture
def testing_df():
    return pd.DataFrame(
        [
            ["toto", 14, 140],
            ["toto", 14, 140],
            ["titi", 21, 150],
            ["titi", 21, 150],
            ["toto", 14, 140]
        ],
        columns= ["name", "age", "size"]
    )


# Test1 : Check if the dedup lines has been removed (check the size after dedup)
# We are using read_csv mock to simulate the pandas read_csv function
@patch('etl.common.deduplicate.pd.read_csv')
def test_deduplicate(mock_read_csv, testing_df):
    mock_read_csv.return_value = testing_df
    assert deduplicate().shape[0] == 2
