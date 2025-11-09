---
library_name: transformers
license: apache-2.0
base_model: tarteel-ai/whisper-base-ar-quran
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: whisper-base-ar-quran-ft-hijaiyah-2
  results: []
datasets:
- Reinjin/Pelafalan_Huruf_Hijaiyah
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-base-ar-quran-ft-hijaiyah-2

This model is a fine-tuned version of [tarteel-ai/whisper-base-ar-quran](https://huggingface.co/tarteel-ai/whisper-base-ar-quran) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4117
- Accuracy: 0.9540

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.5618        | 1.0   | 1336  | 0.5533          | 0.8956   |
| 0.5432        | 2.0   | 2672  | 0.4359          | 0.9203   |
| 0.0009        | 3.0   | 4008  | 0.4872          | 0.9181   |
| 0.0005        | 4.0   | 5344  | 0.3842          | 0.9360   |
| 0.0002        | 5.0   | 6680  | 0.4643          | 0.9315   |
| 0.0425        | 6.0   | 8016  | 0.3426          | 0.9551   |
| 0.0001        | 7.0   | 9352  | 0.3894          | 0.9450   |
| 0.0001        | 8.0   | 10688 | 0.4227          | 0.9461   |
| 0.0001        | 9.0   | 12024 | 0.4511          | 0.9506   |
| 0.0           | 10.0  | 13360 | 0.4117          | 0.9540   |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cu121
- Datasets 3.1.0
- Tokenizers 0.20.3