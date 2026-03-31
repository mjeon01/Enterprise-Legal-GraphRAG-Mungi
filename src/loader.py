from datasets import load_dataset


def load_all() -> tuple[list, list]:
    print("Loading corpus …")
    corpus = list(load_dataset("isaacus/legal-rag-bench", "corpus", split="test", streaming=True))
    print(f"  → {len(corpus)} passages")

    print("Loading QA …")
    qa = list(load_dataset("isaacus/legal-rag-bench", "qa", split="test", streaming=True))
    print(f"  → {len(qa)} questions\n")

    return corpus, qa
