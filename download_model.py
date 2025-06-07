#!/usr/bin/env python3
import os
import argparse
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM

def main():
    parser = argparse.ArgumentParser(description="Download Qwen2.5-1.5B-Instruct model")
    parser.add_argument("--model_id", type=str, default="Qwen/Qwen2.5-1.5B-Instruct",
                        help="Model ID on Hugging Face Hub")
    parser.add_argument("--output_dir", type=str, default="model/Qwen2.5-1.5B-Instruct",
                        help="Directory to save the model")
    args = parser.parse_args()
    
    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    print(f"Downloading {args.model_id} to {args.output_dir}")
    
    # Download tokenizer
    print("Downloading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_id)
    tokenizer.save_pretrained(args.output_dir)
    
    # Download model
    print("Downloading model (this may take a while)...")
    model = AutoModelForCausalLM.from_pretrained(
        args.model_id,
        torch_dtype="auto",
        trust_remote_code=True
    )
    model.save_pretrained(args.output_dir)
    
    print(f"Model successfully downloaded to {args.output_dir}")

if __name__ == "__main__":
    main()
