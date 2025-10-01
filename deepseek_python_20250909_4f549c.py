# 1. IMPORTS
import pandas as pd
import re
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# 2. LOAD DATA (replace with your dataset paths)
real_df = pd.read_csv("Real1 - TRUE1.csv")
fake_df = pd.read_csv("fake1 - fake1 (1).csv")

# 3. EXPLORE DATA (optional)
print("Real data shape:", real_df.shape)
print("Fake data shape:", fake_df.shape)

# 4. LABEL DATA
real_df["label"] = 1   # REAL
fake_df["label"] = 0   # FAKE

# 5. COMBINE DATASETS
df = pd.concat([real_df, fake_df], axis=0).reset_index(drop=True)

# 6. CLEAN TEXT
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

df["text"] = df["text"].apply(clean_text)
df = df.drop_duplicates(subset=["text"])
df = df[df["text"].str.len() > 20]

# 7. SPLIT DATA
X = df["text"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 8. BUILD PIPELINE (TF-IDF + Logistic Regression)
logreg_model = Pipeline([
    ("tfidf", TfidfVectorizer(
        stop_words="english",
        ngram_range=(1,2),
        max_df=0.9,
        min_df=2
    )),
    ("logreg", LogisticRegression(
        class_weight="balanced", 
        random_state=42,
        max_iter=1000,  # Increased iterations for convergence
        solver='liblinear'  # Good for smaller datasets
    ))
])

# 9. TRAIN
logreg_model.fit(X_train, y_train)

# 10. EVALUATE
y_pred = logreg_model.predict(X_test)
print("ACCURACY:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("\nCONFUSION MATRIX:\n", confusion_matrix(y_test, y_pred))
print("\nCLASSIFICATION REPORT:\n", classification_report(y_test, y_pred))

# 11. SAVE MODEL
joblib.dump(logreg_model, "logreg_fake_news_model.joblib")
print("\nModel saved as logreg_fake_news_model.joblib")

# 12. PREDICT FUNCTION
def predict_news(text):
    text = clean_text(text)
    pred = logreg_model.predict([text])[0]
    return "REAL" if pred == 1 else "FAKE"

# 13. TEST EXAMPLES
samples = [
    "WASHINGTON (Reuters) - The U.S. Congress on Thursday averted a government shutdown just one day before federal funding was due to expire, sending President Donald Trump a bill to provide just enough money to keep agencies operating through Jan. 19. With lawmakers eager to begin a holiday recess until Jan. 3, the House of Representatives and Senate scurried to pass the hastily written bill by votes of 231-188 and 66-32, respectively.",
    "Before Trump, Democrats and their allies in the leftist media rarely had to worry about being called out for their hypocrisy. First of all, there wasn t an opposing voice in the media and politicians in the Republican Party, most especially the President of the United States, certainly weren t going to call them out."
]

for i, s in enumerate(samples):
    print(f"\nNEWS {i+1}: {s[:100]}...")
    print("PREDICTION:", predict_news(s))

# 14. GET PREDICTION PROBABILITIES (optional)
def predict_news_with_prob(text):
    text = clean_text(text)
    pred = logreg_model.predict([text])[0]
    prob = logreg_model.predict_proba([text])[0]
    return "REAL" if pred == 1 else "FAKE", prob

# Test with probabilities
test_text = "Scientists have discovered a new breakthrough in renewable energy technology that could revolutionize the way we power our homes and cities."
prediction, probabilities = predict_news_with_prob(test_text)
print(f"\nTest prediction: {prediction}")
print(f"Probabilities: REAL={probabilities[1]:.4f}, FAKE={probabilities[0]:.4f}")