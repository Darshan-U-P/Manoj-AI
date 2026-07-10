from llama_cpp import Llama

print("Loading model...")

llm = Llama(
    model_path="models/base/Qwen3-4B-Instruct-2507-Q4_K_M.gguf",
    n_gpu_layers=-1,
    verbose=True
)

print("Loaded!")

response = llm(
    "Hello!",
    max_tokens=32
)

print(response["choices"][0]["text"])