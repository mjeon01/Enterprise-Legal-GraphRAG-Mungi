import re

STOPWORDS = {
    "the",
    "a",
    "an",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "do",
    "does",
    "did",
    "will",
    "would",
    "could",
    "should",
    "may",
    "might",
    "shall",
    "can",
    "to",
    "of",
    "in",
    "for",
    "on",
    "with",
    "at",
    "by",
    "from",
    "and",
    "or",
    "but",
    "not",
    "this",
    "that",
    "it",
    "its",
    "he",
    "she",
    "they",
    "their",
    "what",
    "who",
    "which",
    "how",
    "when",
    "where",
    "why",
    "if",
    "as",
    "so",
    "no",
    "any",
    "all",
    "there",
    "been",
    "about",
    "into",
    "than",
    "then",
    "also",
    "such",
    "both",
    "each",
    "other",
}


def parse_id(passage_id: str) -> dict:
    """
    '1.1-c1-s2' → chapter='1.1', chapter_num=1, section_num=2, depth=2
    depth = number of dot-separated parts in the chapter string
    """
    m = re.match(r"^([\d.]+)-c(\d+)-s(\d+)$", passage_id)
    if not m:
        return {
            "chapter": passage_id,
            "chapter_num": None,
            "section_num": None,
            "depth": 0,
        }
    chapter_str = m.group(1)
    depth = len(chapter_str.split("."))
    return {
        "chapter": chapter_str,
        "chapter_num": int(m.group(2)),
        "section_num": int(m.group(3)),
        "depth": depth,
    }


def percentile(sorted_vals: list, p: float) -> float:
    if not sorted_vals:
        return 0.0
    idx = (len(sorted_vals) - 1) * p / 100
    lo = int(idx)
    hi = min(lo + 1, len(sorted_vals) - 1)
    return sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * (idx - lo)


def word_count(text: str) -> int:
    return len(text.split())


def tokenize(text: str) -> set:
    tokens = re.findall(r"[a-z]+", text.lower())
    return {t for t in tokens if t not in STOPWORDS and len(t) > 2}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)
