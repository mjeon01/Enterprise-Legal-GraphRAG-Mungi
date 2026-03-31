from datasets import load_dataset


def load_legal_data(split: str = "test"):

    dataset_name = "isaacus/legal-rag-bench"

    try:
        dataset = load_dataset(dataset_name, split=split, streaming=True)
        print(f"✓ Successfully connected to Legal Dataset: {dataset_name}")
        return dataset
    except Exception as e:
        print(f"✗ Dataset Load Error: {e}")
        raise
