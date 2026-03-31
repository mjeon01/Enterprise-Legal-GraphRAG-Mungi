"""4. Question-passage lexical overlap (Jaccard) → hard case identification."""

from .utils import tokenize, jaccard, percentile


def analyze_overlap(corpus: list, qa: list) -> None:
    print("\n" + "=" * 60)
    print("4. QUESTION-PASSAGE LEXICAL OVERLAP (Jaccard, stopwords removed)")
    print("=" * 60)

    passage_map = {p["id"]: p["text"] for p in corpus}

    scores = []
    missing = []
    for item in qa:
        pid = item["relevant_passage_id"]
        if pid not in passage_map:
            missing.append(item["id"])
            continue
        score = jaccard(tokenize(item["question"]), tokenize(passage_map[pid]))
        scores.append(
            {
                "qa_id": item["id"],
                "passage_id": pid,
                "score": score,
                "question": item["question"],
            }
        )

    if missing:
        print(f"\n  ⚠ {len(missing)} QA items have no matching passage: {missing}")

    scores_sorted = sorted(scores, key=lambda x: x["score"])
    vals = [s["score"] for s in scores_sorted]
    n = len(vals)

    print("\n[Jaccard overlap stats]")
    print(f"  count : {n}")
    print(f"  min   : {min(vals):.4f}")
    print(f"  p25   : {percentile(vals, 25):.4f}")
    print(f"  median: {percentile(vals, 50):.4f}")
    print(f"  p75   : {percentile(vals, 75):.4f}")
    print(f"  max   : {max(vals):.4f}")
    print(f"  mean  : {sum(vals) / n:.4f}")

    hard_threshold = percentile(vals, 25)
    hard_cases = [s for s in scores_sorted if s["score"] <= hard_threshold]

    print(
        f"\n[Hard cases] Jaccard ≤ {hard_threshold:.4f}  (bottom 25% — retrieval is harder)"
    )

    for hc in hard_cases:
        q_short = hc["question"][:80] + ("…" if len(hc["question"]) > 80 else "")
        print(
            f"  qa={hc['qa_id']:>3}  passage={hc['passage_id']:<15}  score={hc['score']:.4f}  {q_short}"
        )

    easy_threshold = percentile(vals, 75)
    easy_cases = [s for s in reversed(scores_sorted) if s["score"] >= easy_threshold]

    print(
        f"\n[Easy cases]  Jaccard ≥ {easy_threshold:.4f}  (top 25% — high lexical overlap)"
    )

    for ec in list(easy_cases)[:10]:
        q_short = ec["question"][:80] + ("…" if len(ec["question"]) > 80 else "")
        print(
            f"  qa={ec['qa_id']:>3}  passage={ec['passage_id']:<15}  score={ec['score']:.4f}  {ec['question'][:80]}"
        )
