import requests
from collections import Counter
import matplotlib.pyplot as plt
import re

def fetch_text_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def map_func(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    return [word for word in words if word]


def reduce_func(counters):
    return Counter(words)

def visualize_top_words(word_frequencies, top_n=10):
    top_words = word_frequencies.most_common(top_n)
    words, frequencies = zip(*top_words)
    plt.bar(words, frequencies)
    plt.xlabel("Words")
    plt.ylabel("Quantity")
    plt.title("Top 10 words")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("top_words.png")  
    print("Plot saved as 'top_words.png'")



if __name__ == "__main__":
    url = input("Enter URL: ").strip()
    text = fetch_text_from_url(url)
    words = map_func(text)

    word_frequencies = reduce_func(words)

    visualize_top_words(word_frequencies, top_n=10)


    #  url = "https://www.gutenberg.net.au/ebooks01/0100021.txt"