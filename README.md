

-----



An interactive web application built with Streamlit and powered by the Google Gemini API to help users practice and prepare for debates. Get AI-generated suggestions, strategies, and sample speeches for any given topic.

[](https://www.python.org/downloads/)
[](https://streamlit.io)
[](https://opensource.org/licenses/MIT)

-----



**(https://jagadish-985-ai-debate-arena-app-gu5okf.streamlit.app)]** 

 \#\# 🛠️ Tech Stack

  * **Frontend:** [Streamlit](https://streamlit.io/)
  * **Language:** Python
  * **LLM:** [Google Gemini API](https://ai.google.dev/)

## ⚙️ Setup and Installation

Follow these steps to run the project locally.

### 1\. Prerequisites

Make sure you have **Python 3.9** or higher installed on your system.

### 2\. Clone the Repository

```bash
git clone https://github.com/Jagadish-985/AI_Debate_Arena.git
cd AI_Debate_Arena
```

### 3\. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 4\. Install Dependencies

Create a `requirements.txt` file with the following content:

```
streamlit
google-generativeai
```

Then, install the required libraries:

```bash
pip install -r requirements.txt
```

### 5\. Configure Your API Key

You need to provide your Google Gemini API key.

  * **Recommended Method:** Create a file named `.env` in the root of your project folder and add your key to it:

    ```
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
    ```

    *(To use this method, you'll need to install `python-dotenv` and modify the script to load the key from the environment variable.)*

  * **Simple Method:** Alternatively, paste your key directly into the `app.py` script as shown in the code.

### 6\. Run the Application

```bash
streamlit run app.py
```

Open your web browser and navigate to `http://localhost:8501`.

-----

