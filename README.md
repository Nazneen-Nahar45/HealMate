<h1 align="center" style="color: green;">HealMate </h1>

**HealMate** is an AI-powered medical assistant platform designed to help users identify diseases from symptoms (via text or voice), receive personalized health recommendations, purchase medicines during emergencies, and book health services or appointments. It integrates machine learning models and chatbot technology to deliver a smart, accessible, and life-saving healthcare experience. 🏥💊🤖

---

<h2 align="left">💻 Built With:</h2>

* **Frontend:**
  * HTML5
  * CSS3
  * JavaScript
  * Bootstrap 5

* **Backend:**
  * Python (Django Framework)

* **Database:**
  * SQLite

* **Machine Learning Models:**
  * Support Vector Classifier (SVC)
  * Random Forest
  * Gradient Boosting
  * K-Nearest Neighbors (KNN)
  * Multinomial Naïve Bayes

* **APIs & Libraries:**
  * Flask (deployment)
  * Gemini API (AI chatbot)
  * pandas, numpy, scikit-learn, pickle
  * django-crispy-forms, crispy-bootstrap4, Pillow

---

<h2 align="left">⚙️ Run This Project:</h2>

1. **Install Required Tools:**
   * Python 3.12
   * VS Code or any Python IDE
   * Git

2. **Clone This Repository:**
   ```sh
   git clone https://github.com/Nazneen-Nahar45/HealMate


3. **Navigate to Project Directory:**

   ```sh
   cd HealMate
   ```

4. **Create a Virtual Environment (Optional but Recommended):**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

5. **Install Required Python Libraries:**

   ```sh
   pip install django
   pip install flask
   pip install pandas
   pip install numpy
   pip install scikit-learn
   pip install Pillow
   pip install django-crispy-forms crispy-bootstrap4
   ```

6. **Install Google Generative AI & Env Management:**
   To interact with Google’s Generative AI and manage your API keys, run:

   ```bash
   pip install google-generativeai python-dotenv Pillow
   # or, for the newer SDK:
   pip install google-genai
   ```

   Then create a `.env` file in your project root and add:

   ```text
   GOOGLE_API_KEY=your_google_api_key_here
   ```

   In your Python code, load it with `python-dotenv`:

   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()
   api_key = os.getenv("GOOGLE_API_KEY")
   ```

   This keeps your API keys secure and out of your codebase.
   
7. **Run the Django Server:**

   ```sh
   python manage.py runserver
   ```

8. **Open in Browser:**

   ```
   http://127.0.0.1:8000/
   ```

---

<h2 align="left">📸 Screenshots:</h2>

* **Home Page**
  ![Homepage](https://github.com/NishatTasnim01/Media-Vault/blob/main/Home.png)

* **Buy Medicine Page**
  ![Buy Medicine](https://github.com/NishatTasnim01/Media-Vault/blob/main/add.png)

* **Services Page**
  ![Services](https://github.com/NishatTasnim01/Media-Vault/blob/main/services.png)

* **About Us Page**
  ![About Us](https://github.com/NishatTasnim01/Media-Vault/blob/main/about.png)
  ![About Us1](https://github.com/NishatTasnim01/Media-Vault/blob/main/about1.png)
  ![About Us2](https://github.com/NishatTasnim01/Media-Vault/blob/main/about2.png)

* **Predict Disease**
  ![Predict Disease](https://github.com/NishatTasnim01/Media-Vault/blob/main/prediction.png)

* **AI Chatbot**
  ![AI Chatbot](https://github.com/NishatTasnim01/Media-Vault/blob/main/chatbot.png)

---

<h2 align="left">📊 Key Features:</h2>

* AI-based symptom-to-disease prediction via text and voice
* Personalized recommendations for:

  * Medicines
  * Diets
  * Workouts
  * Precautions
* Emergency medicine ordering
* Health service and appointment booking
* AI chatbot support (Gemini API)
* Admin dashboard to manage medicines, services, and appointments

---

<h2 align="left">📊 Diagrams:</h2>

* **Entity‑Relationship Diagram (ERD)**  
  ![ERD](https://github.com/NishatTasnim01/Media-Vault/blob/main/ER%20Diagram%20SVG.svg)

<h2 align="left">🌍 Social Impact:</h2>

* Helps users take control of their health anytime, anywhere
* Enables quick action in emergencies
* Reduces pressure on traditional healthcare systems
* Empowers individuals through digital health education

---

<h2 align="left">📆 Project Timeline (Gantt Chart):</h2>

 ![Gantt](https://github.com/NishatTasnim01/Media-Vault/blob/main/Gantt%20Chart.png)

---

### Built By:

* **Nazneen Nahar** - CSE, UAP (21201145)
* **Nishat Tasnim** - CSE, UAP (21201149)

### Instructor:

* **Md Mubtasim Fuad** - Lecturer, CSE, UAP

---

> 🚀 HealMate – Revolutionizing Healthcare, One Click at a Time.
