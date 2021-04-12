import pandas as pd
import logging

from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)


def read_from_postgres(db_name: str, table_name: str, connection_string: str) -> pd.DataFrame:
    engine = create_engine(connection_string)

    logging.info(f"Reading postgres database: '{db_name}', table: '{table_name}' ...")
    return pd.read_sql_table(table_name, con=engine)

