"""2. Passage length distribution & passages per section."""

import math
from collections import Counter, defaultdict
from .utils import parse_id, percentile, word_count


def analyze_lengths(corpus: list) -> None:
    print("\n" + "=" * 60)
    print("2. PASSAGE LENGTH & PASSAGES PER SECTION")
    print("=" * 60)

    lengths = sorted(word_count(p["text"]) for p in corpus)
    n = len(lengths)
    mean = sum(lengths) / n
    std = math.sqrt(sum((x - mean) ** 2 for x in lengths) / n)

    print("\n[Passage word-count stats]")
    print(f"  count : {n}")
    print(f"  min   : {lengths[0]}")
    print(f"  p25   : {percentile(lengths, 25):.0f}")
    print(f"  median: {percentile(lengths, 50):.0f}")
    print(f"  p75   : {percentile(lengths, 75):.0f}")
    print(f"  p90   : {percentile(lengths, 90):.0f}")
    print(f"  max   : {lengths[-1]}")
    print(f"  mean  : {mean:.1f}")
    print(f"  std   : {std:.1f}")

    bucket_size = max(1, (lengths[-1] - lengths[0]) // 10)
    buckets: dict[int, int] = defaultdict(int)
    for wc in lengths:
        buckets[(wc - lengths[0]) // bucket_size] += 1

    print("\n[Word-count histogram]")
    bar_width = 30
    max_count = max(buckets.values())
    for k in sorted(buckets):
        lo = lengths[0] + k * bucket_size
        hi = lo + bucket_size - 1
        cnt = buckets[k]
        bar = "█" * int(cnt / max_count * bar_width)
        print(f"  {lo:4d}-{hi:4d} | {bar:<{bar_width}} {cnt}")

    section_counts = Counter(parse_id(p["id"])["chapter"] for p in corpus)
    counts = sorted(section_counts.values())

    print("\n[Passages-per-section stats]")
    print(f"  total sections : {len(counts)}")
    print(f"  min            : {counts[0]}")
    print(f"  median         : {percentile(counts, 50):.0f}")
    print(f"  max            : {counts[-1]}")
    print(f"  mean           : {sum(counts) / len(counts):.1f}")
    print("\n[Sections with most passages (top 10)]")

    for section, cnt in section_counts.most_common(10):
        print(f"  {section}: {cnt}")
