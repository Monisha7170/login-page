import re
import string

def preprocess_text(text):
    """
    Clean and preprocess a given text string.
    Steps:
    1. Lowercase
    2. Remove URLs, mentions, hashtags
    3. Remove punctuation and numbers
    4. Remove extra spaces
    """
    # 1. Lowercase
    text = text.lower()

    # 2. Remove URLs, mentions, hashtags
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)   # URLs
    text = re.sub(r'@\w+|#\w+', '', text)                # Mentions/hashtags

    # 3. Remove punctuation and numbers
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)  # punctuation
    text = re.sub(r'\d+', '', text)                                   # numbers

    # 4. Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# Example test
if __name__ == "__main__":
    sample = "Breaking News!!! COVID-19 cases rise in India 😷 #Health @WHO https://t.co/xyz123"
    cleaned = preprocess_text(sample)
    print("Original Text:\n", sample)
    print("\nCleaned Text:\n", cleaned)
