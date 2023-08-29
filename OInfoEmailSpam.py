import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Analysis Section
data = pd.read_csv("E:/DATASETS/EMAIL_SPAM.csv", encoding="latin-1")

st.title("Email Spam Detection with Machine Learning")

st.write("In email classification:")
st.write("- Spam refers to unsolicited and unwanted emails sent in bulk.")
st.write("- Ham refers to legitimate and desired emails that users expect.")

X = data["v2"]
y = data["v1"]
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)
classifier = MultinomialNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

# Streamlit section
st.markdown(
    f"<h3 style='text-align: center; color: red;'>Accuracy: {accuracy:.2f}</h3>",
    unsafe_allow_html=True,
)
# Graph section
spam_count = data[data["v1"] == "spam"].shape[0]
ham_count = data[data["v1"] == "ham"].shape[0]
st.bar_chart({"Spam": spam_count, "Ham": ham_count})


# Prediction Section
st.markdown(
    "<h2 style='text-align: center;'>Enter an email to test:</h2>",
    unsafe_allow_html=True,
)
user_input = st.text_area("Email Text")

if st.button("Predict"):
    user_input_vectorized = vectorizer.transform([user_input])
    prediction = classifier.predict(user_input_vectorized)[0]

    if prediction == "spam":
        st.markdown(
            f"<h2 style='text-align: center; color: red;'>Predicted: {prediction}</h2>",
            unsafe_allow_html=True,
        )
        st.write("It's a fake mail.")
    else:
        st.markdown(
            f"<h2 style='text-align: center; color: blue;'>Predicted: {prediction}</h2>",
            unsafe_allow_html=True,
        )
        st.write("It's a valid mail.")
