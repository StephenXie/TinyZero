#!/usr/bin/env python3
import os
import argparse
from pathlib import Path
from datasets import load_dataset

def main():
    parser = argparse.ArgumentParser(description="Download a Hugging Face dataset")
    parser.add_argument("--dataset_id", type=str, default="Jiayi-Pan/Countdown-Tasks-3to4-Unique",
                        help="Dataset ID on Hugging Face Hub")
    parser.add_argument("--output_dir", type=str, default="data/countdown_dataset",
                        help="Directory to save the dataset")
    args = parser.parse_args()
    
    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    print(f"Downloading dataset {args.dataset_id} to {args.output_dir}")
    
    # Download the dataset
    dataset = load_dataset(args.dataset_id)
    
    # Save the dataset to disk in parquet format
    for split_name, split_dataset in dataset.items():
        output_path = os.path.join(args.output_dir, f"{split_name}.parquet")
        split_dataset.to_parquet(output_path)
        print(f"Saved {split_name} split to {output_path}")
    
    # Also save as CSV for easier viewing
    for split_name, split_dataset in dataset.items():
        output_path = os.path.join(args.output_dir, f"{split_name}.csv")
        split_dataset.to_csv(output_path)
        print(f"Saved {split_name} split to {output_path}")
    
    # Print dataset info
    print("\nDataset Information:")
    print(f"Number of splits: {len(dataset)}")
    for split_name, split_dataset in dataset.items():
        print(f"Split '{split_name}': {len(split_dataset)} examples")
    
    print(f"\nDataset successfully downloaded to {args.output_dir}")
    print(f"Example data format: {dataset[next(iter(dataset.keys()))][0]}")

if __name__ == "__main__":
    main()
