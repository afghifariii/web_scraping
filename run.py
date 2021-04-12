import pandas as pd
import os
import sys

from web_scraping.web_scraping import scraper, transformer, writer, reader


URL = "https://id.wikipedia.org/wiki/Daftar_orang_terkaya_di_Indonesia"
DB_NAME = "web_scraping_db"
DB_USER = "username"
DB_PASSWORD = "secret"
DB_HOST = "db"
DB_PORT = "5432"
CONNECTION_STRING = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
TABLE_NAME = "orang_terkaya_indonesia"


def main() -> None:
    dfs = scraper.scrape(URL)
    df_2020 = transformer.transform(dfs[7], 2020)
    writer.write_to_postgres(df=df_2020, db_name=DB_NAME, table_name=TABLE_NAME, connection_string=CONNECTION_STRING)
    result_df = reader.read_from_postgres(db_name=DB_NAME, table_name=TABLE_NAME, connection_string=CONNECTION_STRING)
    
    print("Daftar Orang Terkaya di Indonesia:")
    print(result_df.to_string())


if __name__ == "__main__":
    main()
