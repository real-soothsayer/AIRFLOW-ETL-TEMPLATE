
import pandas as pd

from etl import logging, CONFIG

def deduplicate(file : str = "") -> pd.DataFrame:
    """Delete duplicated rows

    Args:
        file (str): Input file

    Returns:
        pd.DataFrame: Dataframe containing deduplicated rows
    """

    file = CONFIG["data_path"] + "person.csv"

    logging.info("Deduplicating file : " + file)

    return pd.read_csv(file).drop_duplicates()
