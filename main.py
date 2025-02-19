import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import parse_with_llm


st.set_page_config(
    page_title="AI Web Scraper",
    layout="centered",
    page_icon="🔎",
)

# Streamlit App Title
st.title("🔎 AI Web Scraper & Data Extractor")

# Step 1: User Inputs Website URL
st.markdown(
    """
    ### **Step 1: Enter the Website URL**
    Enter the URL of the website you want to scrape. 
    The tool will extract the page content and prepare it for processing.
    """
)
url = st.text_input("🔗 Website URL")



# Step 2: Scrape the Website
if st.button("Scrape Website"):
    if url:
        with st.status("Scraping website... Please wait."):
            result = scrape_website(url)
            body_content = extract_body_content(result)
            cleaned_content = clean_body_content(body_content)

            st.session_state.dom_content = cleaned_content


        with st.expander("📜 View Extracted HTML body"):
            st.text_area("DOM Content", value=cleaned_content, height=300)
    else:
        st.error("❌ Please enter a valid URL before scraping.")

# Step 3: Process Extracted Data
if "dom_content" in st.session_state:
    st.markdown(
        """
        ### **Step 2: Describe What You Want to Extract**
        Enter a clear description of the specific data you need from the webpage. 
        Example descriptions:
        - **"Extract all product prices."**
        - **"Find the article headline and author."**
        - **"Get all the hyperlinks from this page."**
        """
    )

    parse_description = st.text_area("📝 What information do you need?")

    # Step 4: Extract Data Based on User Input
    if st.button("Extract Data"):
        if parse_description:
            with st.status("Extracting data... Please wait.", expanded=True):

                dom_chunks = split_dom_content(st.session_state.dom_content)

                response_placeholder = st.empty()
                streamed_text = ""

                # Process the LLM response with streaming
                for chunk in parse_with_llm(dom_chunks, parse_description):
                    if chunk and hasattr(chunk, "content"):
                        streamed_text += chunk.content
                        response_placeholder.markdown(f"### **📊 Extracted Data:**\n\n{streamed_text}")

            st.success("✅ Extraction Complete! 🎉")
        else:
            st.error("❌ Please provide a description of what to extract.")
