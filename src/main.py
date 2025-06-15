from data.download_sms import download_data_csv

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
    path = "src/data/sms/sms.csv"

    download_data_csv(url,path)