import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MultiLabelBinarizer

import preprocessing as pp


class DatasetManipulation:

    def __init__(self, csv_path):
        self.vectorizer = TfidfVectorizer()
        self.df = pd.read_csv(csv_path)
        self.clean_categories = [sample_categories.split(',') for sample_categories in list(self.df['category'])]
        label_binarizer = MultiLabelBinarizer()
        self.transformed_labels = label_binarizer.fit_transform(self.clean_categories)
        self.model = KNeighborsClassifier()

    @property
    def cleaned_corpus(self):
        return [pp.preprocess_text(sample) for sample in list(self.df['sentence'])]

    @property
    def features(self):
        return self.vectorizer.fit_transform(self.cleaned_corpus)

    def train(self):
        self.model.fit(self.features, self.transformed_labels)

    def predict(self, sentence):
        cleaned_sentence = pp.preprocess_text(sentence)
        features = self.vectorizer.transform([cleaned_sentence])
        return self.model.predict(features)
