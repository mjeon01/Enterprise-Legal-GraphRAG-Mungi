"""1. Corpus hierarchy depth distribution."""

from collections import Counter, defaultdict
from .utils import parse_id


def analyze_hierarchy(corpus: list) -> None:
    print("=" * 60)
    print("1. CORPUS HIERARCHY")
    print("=" * 60)

    parsed = [parse_id(p["id"]) for p in corpus]

    depth_counter = Counter(p["depth"] for p in parsed)
    print("\n[Depth distribution]")
    depth_labels = {1: "chapter", 2: "subchapter", 3: "sub-subchapter"}
    for depth in sorted(depth_counter):
        label = depth_labels.get(depth, f"depth-{depth}")
        print(f"  depth {depth} ({label}): {depth_counter[depth]} passages")

    chapters_by_depth = defaultdict(set)
    for p in parsed:
        chapters_by_depth[p["depth"]].add(p["chapter"])

    print("\n[Unique sections per depth]")
    for depth in sorted(chapters_by_depth):
        print(f"  depth {depth}: {len(chapters_by_depth[depth])} unique sections")

    top_level = defaultdict(int)
    for p in parsed:
        top = p["chapter"].split(".")[0]
        top_level[top] += 1

    print("\n[Passages per top-level chapter]")
    for ch in sorted(top_level, key=lambda x: int(x) if x.isdigit() else 0):
        print(f"  Chapter {ch}: {top_level[ch]} passages")
