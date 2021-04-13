import pandas as pd
import logging

from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)


def write_to_postgres(df: pd.DataFrame, db_name: str, table_name: str, connection_string: str) -> None:
    engine = create_engine(connection_string)

    logging.info(f"Writing dataframe to database: '{db_name}', table: '{table_name}' ...")
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
