import pandas as pd


def download_data_csv(url: str, path: str):
    """
    Downloads from from specified url and save the as csv in a specified path

    Args:
        url (str): the url where data is stored in web
        path (str): the path where data will be stored in local machine

    Returns:
        None
    """

    dataframe = pd.read_csv(url, sep="\t", names=["labels", "message"])
    dataframe.to_csv(path, index=False)



