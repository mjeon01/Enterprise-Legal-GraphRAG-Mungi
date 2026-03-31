import torch


def get_device() -> torch.device:

    if torch.backends.mps.is_available():
        device = torch.device("mps")
        status = "Apple Silicon GPU (MPS) Detected"
    elif torch.cuda.is_available():
        device = torch.device("cuda")
        status = "NVIDIA GPU (CUDA) Detected"
    else:
        device = torch.device("cpu")
        status = "CPU Mode (No Acceleration)"

    print(f"✓ {status}: Using {device}")
    return device
