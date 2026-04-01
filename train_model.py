import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Step 1 — Load dataset
print("Loading dataset...")
df = pd.read_csv("data/dataset.csv")
print(f"Total samples: {len(df)}")
print(df["attack_type"].value_counts())

# Step 2 — Prepare data
X = df["input"]
y = df["attack_type"]

# Step 3 — Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Step 4 — Convert text to numbers using TF-IDF
print("\nConverting text to numbers with TF-IDF...")
vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Step 5 — Train the model
print("Training Naive Bayes model...")
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Step 6 — Evaluate accuracy
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n✅ Model Accuracy: {accuracy * 100:.2f}%")
print("\nDetailed Report:")
print(classification_report(y_test, y_pred))

# Step 7 — Save the model
print("Saving model...")
with open("models/webguard_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model saved to models/")
print("✅ Vectorizer saved to models/")
print("\nWebGuard brain is ready! 🧠")