import os
import json
import yaml
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq

class TextExtractor:
    def __init__(self, config):
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = os.getenv("GROQ_MODEL_NAME")

        self.prompt_path = config.get("prompt_path")
        self.output_path = config.get("output_json_path")

        if not self.api_key:
            raise ValueError("Missing GROQ_API_KEY in .env")

        self.llm = ChatGroq(
            model_name=self.model,
            api_key=self.api_key
        )

        with open(self.prompt_path, "r", encoding="utf-8") as f:
            prompt_text = f.read()

        self.prompt = PromptTemplate.from_template(prompt_text, template_format="jinja2")
        self.chain = self.prompt | self.llm


    def extract(self, text):
        try:
            result = self.chain.invoke({"text": text})
            result_text = result.content 
            print("\n🔎 Raw LLM Output:\n", result_text, "\n")
            start = result_text.find("{")
            end = result_text.rfind("}") + 1
            clean_json = result_text[start:end]

            return json.loads(clean_json)

        except Exception as e:
            print("JSON parsing error:", e)

     

    def save_output(self, metadata):
        try:
            with open(self.output_path, "w", encoding="utf-8") as f:
                json.dump(metadata, f, indent=2)
            print(f" Metadata saved to {self.output_path}")
        except Exception as e:
            print(e)
