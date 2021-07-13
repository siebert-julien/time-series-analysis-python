from typing import List

import pandas as pd


def prepare_dataframe(items: List[dict]) -> pd.DataFrame:
    """
    Creates and prepare a dataframe from a dictionary of github items
    :param items:
    :return: pandas dataframe
    """
    df = pd.DataFrame.from_dict(items)
    if df.empty:
        return df
    # change columns types
    df = df.astype({'language': 'category'})
    df.pushed_at = pd.to_datetime(df.pushed_at)
    df.updated_at = pd.to_datetime(df.updated_at)
    df = df.set_index('id')
    return df