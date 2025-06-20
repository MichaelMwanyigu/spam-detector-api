from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib

def train_model(data_path: str):
    dataframe = pd.read_csv(data_path)
    features = dataframe['message']
    labels = dataframe['labels']

    pipeline = Pipeline(
        [
            ('vectorizer',CountVectorizer()),
            ('classifier',MultinomialNB())
        ]
    )

    pipeline.fit(features,labels)
    joblib.dump(pipeline, 'src/model/spam_model.joblib')
    print("Model trained and saved")

if __name__ == "__main__":
    train_model("src/data/sms/sms.csv")
