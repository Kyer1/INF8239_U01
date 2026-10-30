from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

TARGET = "Target"
RANDOM_STATE = 42
CAT_COLS = [
    "Marital status", "Application mode", "Course", "Previous qualification",
    "Nacionality", "Mother's qualification", "Father's qualification",
    "Mother's occupation", "Father's occupation",
]


def leakage_columns(df):
    """Variables del 2º semestre: no disponibles al cierre del 1er semestre."""
    return [c for c in df.columns if "2nd sem" in c]


def split_xy(df):
    X = df.drop(columns=[TARGET] + leakage_columns(df))
    return X, df[TARGET]


def train_test(X, y):
    return train_test_split(X, y, test_size=0.20, random_state=RANDOM_STATE, stratify=y)


def build_preprocess(X):
    cat_cols = [c for c in CAT_COLS if c in X.columns]
    num_cols = [c for c in X.columns if c not in cat_cols]
    num_pipe = Pipeline([("imputer", SimpleImputer(strategy="median")),
                         ("scale", StandardScaler())])
    cat_pipe = Pipeline([("imputer", SimpleImputer(strategy="most_frequent")),
                         ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))])
    return ColumnTransformer([("num", num_pipe, num_cols), ("cat", cat_pipe, cat_cols)])