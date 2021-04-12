import pandas as pd
import re
import logging


logging.basicConfig(level=logging.INFO)


def is_money_miliar(string_money: str) -> bool:
    return string_money.lower().endswith("miliar")


def transform_money_format(string_money: str) -> str:
    half_clean_string = string_money.lower().replace(",", ".").replace(" ", "")
    return re.sub(r"[?\[M\]miliar|\[J\]juta]", "", half_clean_string)


def transform(df: pd.DataFrame, tahun: int) -> pd.DataFrame:
    logging.info("Transforming DataFrame ...")

    columns_mapping = {
        "Nomor Urut": "nomor_urut",
        "Nama": "nama",
        "Perusahaan": "perusahaan",
        "Kekayaan Bersih (US$)": "kekayaan_bersih_usd"
    }

    renamed_df = df.rename(columns=columns_mapping)
    renamed_df["tahun"] = tahun
    renamed_df["kekayaan_bersih_usd_juta"] = renamed_df["kekayaan_bersih_usd"].apply(
        lambda value: float(transform_money_format(value)) * 1000 if is_money_miliar(value) else float(transform_money_format(value))
    )

    return renamed_df[["nomor_urut", "tahun", "nama", "perusahaan", "kekayaan_bersih_usd_juta"]]

