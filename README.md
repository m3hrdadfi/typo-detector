<h1 align="center">Typo Detector using Transformers 🦁</h1>
<br/>


## English Version

### Dataset Information

For this specific task, I used [NeuSpell](https://github.com/neuspell/neuspell) dataset as my raw-data.

### Evaluation

The following tables summarize the scores obtained by model overall and per each class.

|       #      | precision |  recall  | f1-score |  support |
|:------------:|:---------:|:--------:|:--------:|:--------:|
|     TYPO     |  0.992332 | 0.985997 | 0.989154 | 416054.0 |
|   micro avg  |  0.992332 | 0.985997 | 0.989154 | 416054.0 |
|   macro avg  |  0.992332 | 0.985997 | 0.989154 | 416054.0 |
| weighted avg |  0.992332 | 0.985997 | 0.989154 | 416054.0 |


## Icelandic Version

### Dataset Information
Synthetic data for this specific task.


### Evaluation

The following tables summarize the scores obtained by model overall and per each class.

|       #      | precision |  recall  | f1-score | support |
|:------------:|:---------:|:--------:|:--------:|:-------:|
|     TYPO     |  0.98954  | 0.967603 | 0.978448 | 43800.0 |
|   micro avg  |  0.98954  | 0.967603 | 0.978448 | 43800.0 |
|   macro avg  |  0.98954  | 0.967603 | 0.978448 | 43800.0 |
| weighted avg |  0.98954  | 0.967603 | 0.978448 | 43800.0 |


## Persian Version

<div dir="rtl">
تشخیص‌دهنده خطا‌های املایی، حاصل آموزش مدل بیش از ۱۰۰ ساعت بر روی بیش از ۲ میلیون دیتا است. این مدل برای استفاده تحقیقاتی و مقالات به صورت آزاد در اختیار محققین قرار خواهد گرفت همچنین برای تست و استفاده به صورت آزاد در هاگینگ‌فیس قابل مشاهده خواهد بود. ولی لازم به ذکر است که استفاده از مدل برای مصارف شخصی، استارتاپی، شرکتی و سازمانی و حتی بهبود مدل و فروش آن منطقا و حقیقتا جایز نیست ولی شما میتوانید بسته به استفاده شخصی و یا ابعاد مدل کسب و کار خودتان لایسنس این مدل را خریداری کنید. این لایسنس شامل استفاده از مدل، تونینگ مدل و دیپلوی مدل خواهد بود.

- [استفاده شخصی](https://zarinp.al/377906)
- [استفاده جهت استارتاپ‌ها](https://zarinp.al/377907)
- [استفاده جهت شرکت‌ها و سازمان‌ها](https://zarinp.al/377908)
 
پس از خریداری لایسنس بر حسب اطلاعات وارد شده با شما تماس خواهیم گرفت، جهت تنظیم وقت پشتیبانی آنلاین جهت هماهنگی مدل متناسب با نوع کسب‌و‌کار شما.
 
 **لازم به ذکر است بهبود و ارتقا مدل جز در موارد خریداری شده لایسنس (شخصی، استارتاپی، شرکتی و سازمانی) و متناسب با همان زمینه مجاز می‌باشد. شما نمی‌توانید مدل را بهبود داده و از آن به هر طریقی درآمدزایی کنید.**
 
</div>

## Dataset Information

I made synthetic data for this specific task.


## Evaluation

The following tables summarize the scores obtained by model overall and per each class.

|       #      | precision |  recall  | f1-score |  support |
|:------------:|:---------:|:--------:|:--------:|:--------:|
|     TYPO     |  0.984098 | 0.984047 | 0.984073 | 307088.0 |
|   micro avg  |  0.984098 | 0.984047 | 0.984073 | 307088.0 |
|   macro avg  |  0.984098 | 0.984047 | 0.984073 | 307088.0 |
| weighted avg |  0.984098 | 0.984047 | 0.984073 | 307088.0 |



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
# model_name_or_path = "m3hrdadfi/typo-detector-distilbert-fa"
config = AutoConfig.from_pretrained(model_name_or_path)
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForTokenClassification.from_pretrained(model_name_or_path, config=config)
nlp = pipeline('token-classification', model=model, tokenizer=tokenizer, aggregation_strategy="average")
```

**For English:**
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

**For Icelandic:**
```python
sentences = [
"Páli, vini mínum, langaði að horfa á sjónnvarpið.",
"Leggir þciðursins eru þaktir fjöðrum til bað edravn fuglnn gekgn kuldanué .",
"Þar hitta þeir konu Björns og segir ovs :",
"Ingvar Sæmundsson ekgk rú sveitinni árið 2015 og etnbeitii sér að hinni þungarokkssvedt svnni Momentum .",
"Þar hitta þeir konu Björns og segir ovs :",
"Var hann síðaún hkluti af leikhópnum sem ferðaðist um Bandaríkin til að sýan söngleikinn ."
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
   [Input]:  Páli, vini mínum, langaði að horfa á sjónnvarpið.
[Detected]:  Páli, vini mínum, langaði að horfa á <i>sjónnvarpið</i>.
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  Leggir þciðursins eru þaktir fjöðrum til bað edravn fuglnn gekgn kuldanué .
[Detected]:  Leggir <i>þciðursins</i> eru þaktir fjöðrum til <i>bað</i> <i>edravn</i> <i>fuglnn</i> <i>gekgn</i> <i>kuldanué</i> .
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  Þar hitta þeir konu Björns og segir ovs :
[Detected]:  Þar hitta þeir konu Björns og segir <i>ovs</i> :
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  Ingvar Sæmundsson ekgk rú sveitinni árið 2015 og etnbeitii sér að hinni þungarokkssvedt svnni Momentum .
[Detected]:  Ingvar Sæmundsson <i>ekgk</i> <i>rú</i> sveitinni árið 2015 og <i>etnbeitii</i> sér að hinni <i>þungarokkssvedt</i> <i>svnni</i> Momentum .
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  Þar hitta þeir konu Björns og segir ovs :
[Detected]:  Þar hitta þeir konu Björns og segir <i>ovs</i> :
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  Var hann síðaún hkluti af leikhópnum sem ferðaðist um Bandaríkin til að sýan söngleikinn .
[Detected]:  Var hann <i>síðaún</i> <i>hkluti</i> af leikhópnum sem ferðaðist um Bandaríkin til að <i>sýan</i> söngleikinn .
----------------------------------------------------------------------------------------------------------------------------------
```

**For Persian:**
```python
sentences = [
    'و گلوله دور مقابکل غلم " بود .',
    'شلام تاریکی، دوسته قدیمی من',
    'در سدای سکوت، در روایئ ناآرام تنها غدم می‌زنم',
    'زیر هلقه نور چراغ خیابان',
    'و در صدای سکوت ضمضمه می شود',
    'ویرایستیار متن برای نویسندگان ، روزنامه نگاران و اسحاب رصانهه',
    'جکیم ابوالقفاسم فرذدوسی ساعر حماصی سصرای غرن جهارم استت ( تمامما قلط )',
    'میان عاشق و معشوق هیچ هائل نیست',
    'عذاهای زود حزم برای معده بهتر است .',
    'غضا خوردم و رفتم .',
    'او شاگرد خاص و عقرب به استاد بود .'
]

for sentence in sentences:
    typos = [sentence[r["start"]: r["end"]] for r in nlp(sentence)]

    detected = sentence
    for typo in typos:
        detected = detected.replace(typo, f' ـ {typo} ـ ')

    print("   [Input]: ", sentence)
    print("[Detected]: ", detected)
    print("-" * 130)
```

Output:
```text
   [Input]:  و گلوله دور مقابکل غلم " بود .
[Detected]:  و گلوله  ـ دور ـ   ـ مقابکل ـ   ـ غلم ـ  " بود .
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  شلام تاریکی، دوسته قدیمی من
[Detected]:   ـ شلام ـ  تاریکی،  ـ دوسته ـ  قدیمی من
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  در سدای سکوت، در روایئ ناآرام تنها غدم می‌زنم
[Detected]:  در  ـ سدای ـ  سکوت، در  ـ روای ـ  ـ ئ ـ   ـ ناآرام ـ  تنها  ـ غدم ـ  می‌زنم
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  زیر هلقه نور چراغ خیابان
[Detected]:  زیر  ـ هلقه ـ  نور چراغ خیابان
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  و در صدای سکوت ضمضمه می شود
[Detected]:  و در صدای سکوت  ـ ضمضمه ـ  می شود
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  ویرایستیار متن برای نویسندگان ، روزنامه نگاران و اسحاب رصانهه
[Detected]:   ـ ویرایستیار ـ  متن برای نویسندگان ، روزنامه نگاران و  ـ اسحاب ـ   ـ رصانهه ـ 
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  جکیم ابوالقفاسم فرذدوسی ساعر حماصی سصرای غرن جهارم استت ( تمامما قلط )
[Detected]:   ـ جکیم ـ   ـ ابوالقفاسم ـ   ـ فرذدوسی ـ   ـ ساعر ـ   ـ حماصی ـ   ـ سصرای ـ   ـ غرن ـ   ـ جهارم ـ   ـ استت ـ  (  ـ تمامما ـ   ـ قلط ـ  )
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  میان عاشق و معشوق هیچ هائل نیست
[Detected]:  میان عاشق و معشوق هیچ  ـ ها ـ  ـ ئ ـ  ـ ل ـ  نیست
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  عذاهای زود حزم برای معده بهتر است .
[Detected]:   ـ عذاهای ـ  زود  ـ حزم ـ  برای معده بهتر است .
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  غضا خوردم و رفتم .
[Detected]:   ـ غضا ـ  خوردم و رفتم .
----------------------------------------------------------------------------------------------------------------------------------
   [Input]:  او شاگرد خاص و عقرب به استاد بود .
[Detected]:  او شاگرد خاص و  ـ عقرب ـ  به استاد بود .
----------------------------------------------------------------------------------------------------------------------------------
```
