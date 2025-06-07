export N_GPUS=2
export BASE_MODEL=model/Qwen2.5-1.5B-Instruct
export DATA_DIR=data/Countdown
export ROLLOUT_TP_SIZE=2
export EXPERIMENT_NAME=countdown-qwen2.5-1.5b-vllm-xformers
export VLLM_ATTENTION_BACKEND=XFORMERS