<h1 align="center">Typo Detector using Transformers 🦁</h1>
<br/>

## Dataset Information

For this specific task, I used [NeuSpell](https://github.com/neuspell/neuspell) dataset as my raw-data.

## Evaluation

The following tables summarize the scores obtained by model overall and per each class.

|       #      | precision |  recall  | f1-score |  support |
|:------------:|:---------:|:--------:|:--------:|:--------:|
|     TYPO     |  0.992332 | 0.985997 | 0.989154 | 416054.0 |
|   micro avg  |  0.992332 | 0.985997 | 0.989154 | 416054.0 |
|   macro avg  |  0.992332 | 0.985997 | 0.989154 | 416054.0 |
| weighted avg |  0.992332 | 0.985997 | 0.989154 | 416054.0 |


## How to use

You use this model with Transformers pipeline for NER (token-classification).

### Installing requirements

```bash
pip install transformers
```

### Prediction using pipeline

```python
import torch
from transformers import AutoConfig, AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


model_name_or_path = "m3hrdadfi/typo-detector-distilbert-en"
config = AutoConfig.from_pretrained(model_name_or_path)
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForTokenClassification.from_pretrained(model_name_or_path, config=config)
nlp = pipeline('token-classification', model=model, tokenizer=tokenizer, aggregation_strategy="average")
```

```python
sentences = [
 "He had also stgruggled with addiction during his time in Congress .",
 "The review thoroughla assessed all aspects of JLENS SuR and CPG esign maturit and confidence .",
 "Letterma also apologized two his staff for the satyation .",
 "Vincent Jay had earlier won France 's first gold in gthe 10km biathlon sprint .",
 "It is left to the directors to figure out hpw to bring the stry across to tye audience .",
]

for sentence in sentences:
    typos = [sentence[r["start"]: r["end"]] for r in nlp(sentence)]

    detected = sentence
    for typo in typos:
        detected = detected.replace(typo, f'<i>{typo}</i>')

    print("   [Input]: ", sentence)
    print("[Detected]: ", detected)
    print("-" * 130)
```

Output:
```text
   [Input]:  He had also stgruggled with addiction during his time in Congress .
[Detected]:  He had also <i>stgruggled</i> with addiction during his time in Congress .
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  The review thoroughla assessed all aspects of JLENS SuR and CPG esign maturit and confidence .
[Detected]:  The review <i>thoroughla</i> assessed all aspects of JLENS SuR and CPG <i>esign</i> <i>maturit</i> and confidence .
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  Letterma also apologized two his staff for the satyation .
[Detected]:  <i>Letterma</i> also apologized <i>two</i> his staff for the <i>satyation</i> .
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  Vincent Jay had earlier won France 's first gold in gthe 10km biathlon sprint .
[Detected]:  Vincent Jay had earlier won France 's first gold in <i>gthe</i> 10km biathlon sprint .
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  It is left to the directors to figure out hpw to bring the stry across to tye audience .
[Detected]:  It is left to the directors to figure out <i>hpw</i> to bring the <i>stry</i> across to <i>tye</i> audience .
----------------------------------------------------------------------------------------------------------------------------------
```
