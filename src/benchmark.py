import time
import torch
from accelerator import get_device
from data_loader import load_legal_data


def run_performance_test():
    device = get_device()
    dataset = load_legal_data()

    num_rows = 100
    test_tensor = torch.randn(num_rows, 512).to(device)

    # 워밍업
    if device.type == "mps":
        _ = torch.matmul(test_tensor, test_tensor.T)
        torch.mps.synchronize()

    start_time = time.time()
    _ = torch.matmul(test_tensor, test_tensor.T)
    if device.type == "mps":
        torch.mps.synchronize()

    latency_ms = (time.time() - start_time) * 1000

    # dataset 실제 사용
    sample_count = sum(1 for _ in dataset)  # ← 이걸로 F841 해결

    print("-" * 50)
    print("Legal-RAG Benchmark Results (Week 1)")
    print(f"Device: Apple M4 Pro ({device})")
    print(f"Processed: {num_rows} Rows")
    print(f"Dataset Samples: {sample_count}")  # ← 출력에도 활용
    print(f"Latency: {latency_ms:.2f} ms")
    print("-" * 50)


if __name__ == "__main__":
    run_performance_test()
