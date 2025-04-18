import re

def count_words(text, method="regex"):
    """Count words using the selected method."""
    if not text:
        return 0

    method = method.lower()

    # Lightweight methods (preferred for performance and simplicity)

    if method == "split":
        # Fastest but naive — splits on any whitespace
        return len(text.split())

    elif method == "regex":
        # NLP-style tokenization using regex word boundaries (e.g., Google Docs-style)
        return len(re.findall(r'\b\w+\b', text))

    elif method == "legal":
        # Slightly cleaner parsing — remove citations, symbols, and section references
        cleaned = re.sub(r'\[\d+\]', '', text)                        # remove [1], [2], etc.
        cleaned = re.sub(r'§\s*\d+(\.\d+)*', '', cleaned)             # remove § 123.45
        return len(re.findall(r'\b\w+\b', cleaned))

    # Future, heavier NLP models (spaCy, NLTK, etc.)

    elif method == "nlp":
        # Placeholder for heavier NLP tokenizers — useful for advanced linguistic parsing
        raise NotImplementedError(
            "NLP-based word count is not yet implemented.\n"
            "You could use spaCy or NLTK to tokenize and count words here."
        )

    else:
        raise ValueError(f"Unsupported WORDCOUNT_METHOD: {method}")

