import streamlit as st

import torch
from transformers import pipeline
from transformers import AutoConfig, AutoTokenizer, AutoModelForTokenClassification

from libs.normalizer import Normalizer
from libs.examples import LANGUAGES, EXAMPLES
from libs.dummy import outputs as dummy_outputs
from libs.utils import local_css, remote_css

import meta

MODELS = {
    "English (en)": "m3hrdadfi/typo-detector-distilbert-en",
    "Persian (fa)": "m3hrdadfi/typo-detector-distilbert-fa",
    "Icelandic (is)": "m3hrdadfi/typo-detector-distilbert-is",
}


class TypoDetector:
    def __init__(
            self,
            model_name_or_path: str = "m3hrdadfi/typo-detector-distilbert-en"
    ) -> None:
        self.debug = True
        self.dummy_outputs = dummy_outputs
        self.model_name_or_path = model_name_or_path
        self.task_name = "token-classification"

        self.tokenizer = None
        self.config = None
        self.model = None
        self.nlp = None
        self.normalizer = None

    def load(self):
        if not self.debug:
            self.config = AutoConfig.from_pretrained(self.model_name_or_path)
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path)
            self.model = AutoModelForTokenClassification.from_pretrained(self.model_name_or_path, config=self.config)
            self.nlp = pipeline(
                self.task_name,
                model=self.model,
                tokenizer=self.tokenizer,
                aggregation_strategy="average"
            )

        self.normalizer = Normalizer()

    def detect(self, sentence):
        if self.debug:
            return self.dummy_outputs[0]

        typos = [sentence[r["start"]: r["end"]] for r in self.nlp(sentence)]

        detected = sentence
        for typo in typos:
            detected = detected.replace(typo, f'<span class="typo">{typo}</span>')

        return detected


@st.cache(allow_output_mutation=True)
def load_typo_detectors():
    en_detector = TypoDetector(MODELS["English (en)"])
    en_detector.load()

    is_detector = TypoDetector(MODELS["Icelandic (is)"])
    is_detector.load()

    fa_detector = TypoDetector(MODELS["Persian (fa)"])
    fa_detector.load()

    return {
        "en": en_detector,
        "fa": fa_detector,
        "is": is_detector
    }


def main():
    st.set_page_config(
        page_title="Typo Detector",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    remote_css("https://cdn.jsdelivr.net/gh/rastikerdar/vazir-font/dist/font-face.css")
    local_css("assets/style.css")
    detectors = load_typo_detectors()

    col1, col2 = st.beta_columns([6, 4])
    with col2:
        st.markdown(meta.INFO, unsafe_allow_html=True)

    with col1:
        language = st.selectbox(
            'Examples (select from this list)',
            LANGUAGES,
            index=0
        )
        detector = detectors[language]
        is_rtl = "rtl" if language == "fa" else "ltr"
        if language == "fa":
            local_css("assets/rtl.css")
        else:
            local_css("assets/ltr.css")

        prompts = list(EXAMPLES[language].keys()) + ["Custom"]
        prompt = st.selectbox(
            'Examples (select from this list)',
            prompts,
            # index=len(prompts) - 1,
            index=0
        )

        if prompt == "Custom":
            prompt_box = ""
        else:
            prompt_box = EXAMPLES[language][prompt]

        text = st.text_area(
            'Insert your text: ',
            detector.normalizer(prompt_box),
            height=100
        )
        text = detector.normalizer(text)
        entered_text = st.empty()

    detect_typos = st.button('Detect Typos !')

    st.markdown(
        "<hr />",
        unsafe_allow_html=True
    )
    if detect_typos:
        words = text.split()
        with st.spinner("Detecting..."):
            if not len(words) > 3:
                entered_text.markdown(
                    "Insert your text (at least three words)"
                )
            else:
                detected = detector.detect(text)
                detected = f"<p class='typo-box {is_rtl}'>{detected}</p>"
                st.markdown(
                    detected,
                    unsafe_allow_html=True
                )


if __name__ == '__main__':
    main()
