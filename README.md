<p align="center" width="50%">
<img src="assets/logo.jpg" alt="VideoTuna" style="width: 30%; min-width: 200px; display: block; margin: auto; background-color: transparent;">
</p>

# VideoTuna
Let's finetune video generation models!


## ⏰TODOs
- [x] inference vc, dc   
- [x] finetune & train vc2，dc   
- [x] opensora-train, inference  
- [x] flux inference, fine-tune  
- [x] cogvideo inference, fine-tune  
- [ ] merge diffusion parts
- [ ] refactor vc, opensora, cogvideo and flux 
- [ ] add peft lora 
- [ ] add RL for alignment 
- [ ] add documents 
- [ ] add unit test support 
- [ ] svd, open-sora-plan

## 🔆 Updates



## 🔆 Introduction
🤗🤗🤗 VideoTuna is an open-sourcing finetuning framework for text-to-video generation.

### Features
1. All in one framework: Inference and finetune state-of-the-art T2V models.
2. Continuous training
3. Fintuning: domain-specific.
4. Fintuning: enhanced language understanding.
5. Fintuning: enhancement.
6. Human preference alignment/Post-training: RLHF, DPO.

### Code Structure
```
VideoTuna
├── configs
│ ├── model_name_inf.yaml
│ └── model_name_train.yaml
├── checkpoints
├── docs
├── inputs
├── results
├── src
│ ├── dataset
│ ├── model-1
│ ├── model-2
│ └── model-N
├── scripts
│ ├── inference_xxx.py
│ └── train_xxx.py
├── shscripts
│ ├── inference_xxx.sh
│ └── train_xxx.sh
├── utils
└── test

```

### Checkpoint Structure
```
VideoTuna/
    └── checkpoints/
        ├── dynamicrafter/
        │   └── i2v_576x1024
        ├── stablediffusion/
        │   └── v2-1_512-ema
        ├── videocrafter/
        │   ├── t2v_v2_512
        │   ├── t2v_v1_1024
        │   └── i2v_v1_512
        ├── open-sora/
        │   └── # TODO
        └── cogvideo/
            └── # TODO
```

### Models

|T2V-Models|HxWxL|Checkpoints|
|:---------|:---------|:--------|
|CogVideo|TODO|[TODO](https://huggingface.co/VideoCrafter/VideoCrafter2/blob/main/model.ckpt)
|Open-Sora 1.2|TODO|[TODO](https://huggingface.co/VideoCrafter/VideoCrafter2/blob/main/model.ckpt)
|Open-Sora 1.1|TODO|[TODO](https://huggingface.co/VideoCrafter/VideoCrafter2/blob/main/model.ckpt)
|Open-Sora 1.0|TODO|[TODO](https://huggingface.co/VideoCrafter/VideoCrafter2/blob/main/model.ckpt)
|Open-Sora Plan 1.2.0|TODO|[TODO](https://huggingface.co/VideoCrafter/VideoCrafter2/blob/main/model.ckpt)
|Open-Sora Plan 1.1.0|TODO|[TODO](https://huggingface.co/VideoCrafter/VideoCrafter2/blob/main/model.ckpt)
|Open-Sora Plan 1.0.0|TODO|[TODO](https://huggingface.co/VideoCrafter/VideoCrafter2/blob/main/model.ckpt)
|VideoCrafter2|320x512x16|[Hugging Face](https://huggingface.co/VideoCrafter/VideoCrafter2/blob/main/model.ckpt)
|VideoCrafter1|576x1024x16|[Hugging Face](https://huggingface.co/VideoCrafter/Text2Video-1024/blob/main/model.ckpt)
|VideoCrafter1|320x512x16|[Hugging Face](https://huggingface.co/VideoCrafter/Text2Video-512/blob/main/model.ckpt)

|I2V-Models|HxWxL|Checkpoints|
|:---------|:---------|:--------|
|DynamiCrafter|576x1024x16|[Hugging Face](https://huggingface.co/Doubiiu/DynamiCrafter_1024/blob/main/model.ckpt)|
|VideoCrafter1|320x512x16|[Hugging Face](https://huggingface.co/VideoCrafter/Image2Video-512/blob/main/model.ckpt)|

* Note: H: height; W: width; L: length

## 🔆 Get started

### 1.Prepare environment
```
conda create --name videotuna python=3.10 -y
conda activate videotuna
pip install -r requirements.txt
git clone https://github.com/JingyeChen/SwissArmyTransformer
pip install -e SwissArmyTransformer/
rm -rf SwissArmyTransformer
```

### 2.Prepare checkpoints
```
# ---- T2V ----
# cogvideo

# open-sora

# videocrafter
wget https://huggingface.co/VideoCrafter/VideoCrafter2/resolve/main/model.ckpt   # videocrafter2-t2v-512
wget https://huggingface.co/VideoCrafter/Text2Video-1024/resolve/main/model.ckpt # videocrafter1-t2v-1024

# ---- I2V ----
# dynamicrafter
wget https://huggingface.co/Doubiiu/DynamiCrafter_1024/resolve/main/model.ckpt   # dynamicrafter-i2v-1024

# videocrafter
wget https://huggingface.co/VideoCrafter/Image2Video-512/resolve/main/model.ckpt # videocrafter1-i2v-512

```
after these commands, the model checkpoints should be placed as [Checkpoint Structure]().

### 3.Inference state-of-the-art T2V/I2V models

- Inference a set of target models in one command:

    ```bash todo.sh```



- Inference a specific model:

Task|Models|Commands|
|:---------|:---------|:---------|
|T2V|cogvideo|`bash shscripts/inference_cogVideo_diffusers.sh`|
|T2V|open-sora||
|T2V|videocrafter-v2-320x512|`bash shscripts/inference_t2v_vc2.sh`
|I2V|dynamicrafter|`bash shscripts/inference_dc_i2v_576x1024.sh`|
|I2V|videocrafter1|`bash shscripts/inference_vc1_i2v_320x512.sh`|
|T2I|flux|`bash shscripts/inference_flux_schnell.sh`|

For detailed inference settings please check [docs/inference.md](docs/inference.md).

### 4. Finetune T2V models
#### Lora finetuning for 
specific domains 

#### Finetuning for enhanced langugage understanding 



(1) Prepare data


(2) Finetune  
```
bash configs/train/000_videocrafter2ft/run.sh
```

### 5. Evaluation


### 6. Alignment


## 🍻 Contributors

## 📋 License

## 😊 Citation

