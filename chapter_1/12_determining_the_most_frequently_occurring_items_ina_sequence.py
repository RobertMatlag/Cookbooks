from collections import Counter

words = [
    "look",
    "into",
    "my",
    "eyes",
    "look",
    "into",
    "my",
    "eyes",
    "the",
    "eyes",
    "the",
    "eyes",
    "the",
    "eyes",
    "not",
    "around",
    "the",
    "eyes",
    "don't",
    "look",
    "around",
    "the",
    "eyes",
    "look",
    "into",
    "my",
    "eyes",
    "you're",
    "under",
]


if __name__ == "__main__":
    word_counts = Counter(words)
    print(word_counts)
    top_three = word_counts.most_common(3)
    print(top_three)

    # ale cudo
    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    word_counts.update(morewords)
    print(word_counts)

    a = Counter(words)
    b = Counter(morewords)

    print(a-b)
    print(a+b)
