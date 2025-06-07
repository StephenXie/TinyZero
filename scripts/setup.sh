python ./download_model.py --model_id Qwen/Qwen2.5-1.5B-Instruct --output_dir ./model/Qwen2.5-1.5B-Instruct
python ./download_dataset.py --dataset_id Jiayi-Pan/Countdown-Tasks-3to4-Unique --output_dir ./data/Countdown-Tasks-3to4-Unique

python examples/data_preprocess/countdown.py --template_type=qwen-instruct --local_dir=./data/Countdown