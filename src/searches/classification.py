import numpy as np
from sklearn.utils import shuffle
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import config


def get_split_data(df, column, type):
    df = shuffle(df)
    size = df.comment.count()

    if column == "x":
        series = df.comment
    elif column == "y":
        series = df.Categorie
    else:
        raise ValueError("column must be x or y")

    if type == "train":
        split_data = series.iloc[:int(size/2)]
    elif type == "test":
        split_data = series.iloc[int(size/2):]
    else:
        raise ValueError("type must be train or test")

    return split_data.values


def make_nb_classifier():
    clf_nb = Pipeline([('vect', CountVectorizer()),
                       ('tfidf', TfidfTransformer()),
                       ('clf', MultinomialNB())])

    return clf_nb


def make_svm_classifier():
    clf_svm = Pipeline([('vect', CountVectorizer()),
                        ('tfidf', TfidfTransformer()),
                        ('clf-svm', SGDClassifier(loss='hinge',
                                                  penalty='l2',
                                                  alpha=1e-3,
                                                  n_iter=5,
                                                  random_state=42))])
    return clf_svm


def classify(df, model):
    x_train = get_split_data(df, "x", "train")
    x_test = get_split_data(df, "x", "test")

    y_train = get_split_data(df, "y", "train")
    y_test = get_split_data(df, "y", "test")

    if model == "svm":
        clf = make_svm_classifier()
    elif model == "nb":
        clf = make_nb_classifier()
    else:
        raise ValueError(f"model must be in {config.MODELS}")

    clf.fit(x_train, y_train)
    y_predict = clf.predict(x_test)
    score = np.mean(y_predict == y_test)

    return score
