# 🔎 AI Web Scraper & Data Extractor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-web-scraper-app.streamlit.app/)

## 🚀 Overview

AI Web Scraper is a **Streamlit-based web scraping tool** that extracts content from webpages using **Selenium & Browserless.io**, and then **leverages DeepSeek V3 AI for intelligent data extraction**. Users can **scrape, extract, and process specific information** from websites using natural language queries.

🔗 **Live App:** [AI Web Scraper](https://ai-web-scraper-app.streamlit.app/)  
📚 **GitHub Repository:** [Sacarianos/ai_webscraper](https://github.com/Sacarianos/ai_webscraper)  

---

## 🛠 **Features**
✔️ **Headless Web Scraping** using **Selenium + Browserless.io**  
✔️ **AI-Powered Data Extraction with DeepSeek V3**  
✔️ **Streamlit UI** for easy interaction  
✔️ **Handles JavaScript-rendered pages**  
✔️ **Secure API Key Management** via `secrets.toml`  
✔️ **Error Handling & Logging** to prevent crashes  

---

## 🛠️ **Installation & Setup**
### **1⃣ Clone the Repository**
```bash
git clone https://github.com/Sacarianos/ai_webscraper.git
cd ai_webscraper
```

### **2⃣ Create a Virtual Environment**
```bash
python -m venv ai
source ai/bin/activate  # MacOS/Linux
ai\Scripts\activate  # Windows
```

### **3⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4⃣ Set Up API Keys**
#### **🔹 Browserless.io API Key**
- **Sign up for Browserless.io**: [https://www.browserless.io](https://www.browserless.io/)
- Copy your **API Key**
- **Store it in `.streamlit/secrets.toml`**:
  ```toml
  [browserless]
  api_key = "your_browserless_api_key"
  ```
  
#### **🔹 DeepSeek V3 API Key**
- **Sign up for DeepSeek AI**: [https://deepseek.com](https://deepseek.com)
- Copy your **API Key**
- **Store it in `.streamlit/secrets.toml`**:
  ```toml
  [deepseek]
  api_key = "your_deepseek_api_key"
  ```

---

## ▶️ **Run the App Locally**
```bash
streamlit run main.py
```
This will launch the web interface in your browser.

---

## 🖥 **Project Structure**
```
ai_webscraper/
│── .streamlit/               # Streamlit configuration & API keys
│   ├── secrets.toml          # API Keys (DO NOT COMMIT)
│── ai/                       # Virtual environment (not included in repo)
│── scrape.py                 # Web scraping logic (Selenium & Browserless)
│── parse.py                  # AI-powered data extraction (DeepSeek V3)
│── main.py                   # Streamlit App UI
│── requirements.txt           # Python dependencies
│── README.md                  # Documentation
│── .gitignore                 # Ignore unnecessary files
```

---

## 🔥 **How It Works**
### **1⃣ Enter a Website URL**
- Provide a **URL of the page** you want to scrape.

### **2⃣ Extract Web Content**
- The app **renders the page using Selenium** and retrieves its content.

### **3⃣ Describe What You Need**
- Input a **natural language query** (e.g., "Extract all product prices").

### **4⃣ AI Extracts the Data (DeepSeek V3)**
- The **DeepSeek V3 AI-powered parser** extracts relevant content from the page.

---

## 💀 **DeepSeek V3 Integration**
🔍 **Why Use DeepSeek V3?**
- **Advanced LLM capabilities** to extract and structure data.
- **Handles complex queries with high accuracy.**
- **Faster response times for real-time extraction.**

📏 **How We Use DeepSeek V3**:
- The extracted page content is **sent to DeepSeek V3 API**, which processes **structured data extraction** based on the user’s query.
- It **understands context** and **filters relevant information** using advanced AI.

---

## 📅 **Deploying to Streamlit Cloud**
1. Push your code to **GitHub**.
2. Go to **[Streamlit Cloud](https://share.streamlit.io/)**.
3. Select **"Deploy a new app"** and connect your repository.
4. Set **secrets in Streamlit Cloud** (`Secrets` > Add API keys).
5. Click **Deploy**.

---

## 🚀 **Troubleshooting**
### **🔴 Web Scraping Fails (`WebDriverException`)**
- Check if **Browserless.io API Key** is valid.
- Ensure **Selenium session is fresh** (restart the app).

### **🔴 API Keys Not Working**
- Ensure `secrets.toml` exists and contains **valid keys**.
- If using **Streamlit Cloud**, add secrets under **Settings > Secrets**.

---

## 🎯 **Future Improvements**
✅ **Add support for multiple URLs**  
✅ **Improve DeepSeek AI-based extraction accuracy**  
✅ **Enhance error logging & handling**  

---

## 🤝 **Contributing**
Want to improve this project? Feel free to submit **issues** or **pull requests**!

---

## 📚 **License**
This project is **MIT Licensed**.

---

🚀 **Enjoy scraping the web with AI!**  
🔗 **Live App:** [AI Web Scraper](https://ai-web-scraper-app.streamlit.app/)  
📚 **GitHub Repository:** [Sacarianos/ai_webscraper](https://github.com/Sacarianos/ai_webscraper)  

