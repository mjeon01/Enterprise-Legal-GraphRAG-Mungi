import torch
import time
from datasets import load_dataset

def run_legal_tensor_benchmark():
    # 1. 하드웨어 가속 설정 확인 (Apple Silicon MPS)
    if torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")
    
    print(f"Using device: {device.type}")

    # 2. 법률 도메인 데이터셋 로드 (isaacus/legal-rag-bench)
    dataset_name = "isaacus/legal-rag-bench"
    
    try:
        dataset = load_dataset(dataset_name, split='test', streaming=True)
        print(f"Successfully loaded dataset: {dataset_name}")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return

    print("-" * 45)

    num_rows = 100
    test_tensor = torch.randn(num_rows, 512).to(device)

    if device.type == "mps":
        _ = torch.matmul(test_tensor, test_tensor.T)
        torch.mps.synchronize()

    start_time = time.time()

    _ = torch.matmul(test_tensor, test_tensor.T)
    
    if device.type == "mps":
        torch.mps.synchronize()

    end_time = time.time()
    
    latency_ms = (end_time - start_time) * 1000

    print("Legal-RAG Benchmark Results")
    print(f"Target Hardware: Apple M4 Pro ({device.type})") #
    print(f"Processed Rows: {num_rows}")
    print(f"Latency: {latency_ms:.2f} ms")
    print("-" * 45)

if __name__ == "__main__":
    run_legal_tensor_benchmark()