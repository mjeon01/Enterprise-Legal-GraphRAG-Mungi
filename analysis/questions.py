"""3. QA question listing for manual type classification."""


def list_questions(qa: list) -> None:
    print("\n" + "=" * 60)
    print("3. QA QUESTIONS (for manual classification)")
    print("=" * 60)
    print()
    print("  Suggested categories:")
    print("  [A] Factual / definition lookup")
    print("  [B] Procedural / process steps")
    print("  [C] Conditional / hypothetical scenario")
    print("  [D] Comparative / distinction")
    print("  [E] Causal / reason-why")
    print("  [F] Eligibility / permission check")
    print("  [G] Other")
    print()

    for item in qa:
        qid = item["id"]
        q = item["question"]
        pid = item["relevant_passage_id"]

        # word-wrap at ~75 chars
        words = q.split()
        line: list[str] = []
        lines: list[str] = []
        for w in words:
            if sum(len(x) + 1 for x in line) + len(w) > 75:
                lines.append(" ".join(line))
                line = []
            line.append(w)
        if line:
            lines.append(" ".join(line))

        print(f"  [{qid:>3}] (passage: {pid})")
        for i, ln in enumerate(lines):
            prefix = "            " if i > 0 else "        Q:  "
            print(f"{prefix}{ln}")
        print()
