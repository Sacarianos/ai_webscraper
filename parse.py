from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import dotenv
import os
import time
import streamlit as st

dotenv.load_dotenv()

DEEPSEEK_API_URL = "https://openrouter.ai/api/v1/"
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API")


model = ChatOpenAI(
    model_name="deepseek/deepseek-chat:free",
    temperature=0.2,
    openai_api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_API_URL,
    streaming=True,
)

# Define the prompt template
promp_template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)



def parse_with_llm(dom_chunks, parse_description, max_retries=3):
    prompt = ChatPromptTemplate.from_template(promp_template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        print(f"Processing batch {i} of {len(dom_chunks)}...")

        # Streamlit UI component for live updates
        response_placeholder = st.empty()  
        streamed_text = ""

        for attempt in range(3):  # Retry logic if response fails
            try:
                response = chain.stream(
                    {"dom_content": chunk, "parse_description": parse_description}
                )
                
                # Process streamed response token by token
                for chunk in response:
                    if chunk and hasattr(chunk, "content"):
                        streamed_text += chunk.content
                        response_placeholder.markdown(f"\n{streamed_text}")  # ✅ Live update in Streamlit

                # Append final streamed response
                parsed_results.append(streamed_text)
                break  # Stop retrying if response received

            except Exception as e:
                print(f"⚠️ Error on batch {i}, attempt {attempt + 1}: {e}")
                time.sleep(2)  # Short delay before retrying

    return "\n".join(parsed_results)