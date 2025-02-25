# 🚢 Titanic Dataset Chat Agent

A smart chatbot that interacts with the **Titanic dataset** using **FastAPI**, **LangChain**, and **Streamlit**. Users can ask natural language questions about the dataset, get **text-based insights**, and generate **visualizations** dynamically.

---

## ✨ Features

✅ **Natural Language Queries** - Ask questions like *"How many male passengers survived?"*  
✅ **AI-Powered Responses** - Uses an LLM to process and analyze the Titanic dataset.  
✅ **Interactive Visualizations** - Generates graphs & charts based on queries.  
✅ **Streamlit UI** - Clean and intuitive frontend for interacting with the chatbot.  
✅ **FastAPI Backend** - Serves API responses efficiently.  
  

---

## 📌 Tech Stack

- **Backend**: FastAPI, LangChain, OpenAI API (or alternative LLMs like DeepSeek, Grok, etc.)  
- **Frontend**: Streamlit  
- **Data Handling**: Pandas  
- **Visualization**: Matplotlib, Seaborn  


---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Titanic-Bot.git
cd Titanic-Bot
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a **.env** file in the `backend/` folder:
```
OPENAI_API_KEY=your_api_key_here
```


### 5️⃣ Start the Backend
```bash
uvicorn backend.main:app --reload
```

### 6️⃣ Start the Frontend (Streamlit)
```bash
streamlit run frontend/app.py
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/query?question=your_query` | Get AI response & visualization |

---

