Haan 👍 **pahile wala medium nahi, jo pehla complete README diya tha wahi**. Ye raha exactly:

````markdown
# AI-Based Car Service Recommendation System using Fuzzy Logic

An intelligent car service recommendation system that combines **Large Language Models (LLM)** with **Fuzzy Logic** to understand natural-language car problems and recommend an appropriate service with a priority score.

## 🚗 Project Overview

Car owners often describe vehicle problems in natural language, such as:

> "My car is 5 years old, has driven 50,000 km and the AC cooling is very low."

Understanding such descriptions and deciding which service should be performed can be difficult using only fixed conditions.

This project combines:

- **AI/LLM** for understanding and extracting information from the user's natural-language description.
- **Fuzzy Logic** for evaluating service priority using gradual values instead of simple yes/no conditions.
- **Streamlit** for the web interface.
- **Groq API + LangChain** for LLM processing.
- **Streamlit Community Cloud** for live deployment.

## 🎯 Objectives

- Understand car-service problems written in natural language.
- Extract relevant information such as:
  - Car age
  - Mileage
  - Problem description
  - Problem severity
- Apply fuzzy logic to calculate a service priority.
- Recommend a suitable car service.
- Provide an easy-to-use web interface.
- Deploy the application online for public access.

## ✨ Main Features

- 📝 Natural-language car problem input
- 🤖 AI-powered information extraction
- 🔗 LangChain-based LLM processing
- 🧠 Fuzzy inference system
- 📊 Fuzzy membership functions
- ⚙️ Fuzzy rule evaluation
- 🎯 Defuzzified priority score
- 🚗 Car-service recommendation
- 🌐 Live Streamlit web application

## 🧠 How the System Works

The application follows this workflow:

User enters car problem
        ↓
Natural-language input
        ↓
LangChain + LLM
        ↓
Extract car information
        ↓
Fuzzy Logic System
        ↓
Fuzzification
        ↓
Fuzzy Rule Evaluation
        ↓
Defuzzification
        ↓
Service Priority Score
        ↓
Recommended Car Service

### AI/LLM Component

The AI component receives the user's natural-language description and extracts structured information needed by the fuzzy system.

For example:

"My car is 5 years old, has driven 50000 km and AC cooling is very low."

The AI can interpret information such as:

Car Age: 5 years
Mileage: 50000 km
Problem: AC cooling is very low

LangChain is used to manage the interaction between the application and the LLM.

### Fuzzy Logic Component

The extracted values are passed to the fuzzy inference system.

The fuzzy system uses:

1. **Membership Functions**
2. **Fuzzification**
3. **Fuzzy Rules**
4. **Rule Evaluation**
5. **Defuzzification**

Instead of treating values only as `true` or `false`, fuzzy logic allows values to belong to categories with different degrees.

For example, mileage can gradually move from **Low** to **Medium** to **High** rather than changing at one fixed boundary.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application UI |
| LangChain | LLM application framework |
| Groq API | LLM/API service |
| scikit-fuzzy | Fuzzy logic implementation |
| NumPy | Numerical processing |
| SciPy | Scientific/numerical dependency |
| NetworkX | Dependency used by fuzzy-control functionality |
| Git | Version control |
| GitHub | Source-code repository |
| Streamlit Community Cloud | Deployment |

## 📁 Project Structure

AI-Car-Service-Fuzzy-Project/
│
├── app.py
├── requirements.txt
├── README.md
├── writeup.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml

> `.streamlit/secrets.toml` contains the API key locally and **must never be uploaded to GitHub**.

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/arunsonkar123/AI-Car-Service-Fuzzy-Project.git
````

### 2. Open the project

```bash
cd AI-Car-Service-Fuzzy-Project
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create:

`.streamlit/secrets.toml`

Add:

```toml
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

Replace `YOUR_GROQ_API_KEY` with your own API key.

**Never commit or publish the actual API key.**

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🖥️ How to Use

1. Open the application.
2. Enter a description of your car problem.
3. Submit the description for analysis.
4. The AI/LLM extracts relevant car information.
5. The fuzzy inference system evaluates the inputs.
6. The application calculates a priority score.
7. The application provides a service recommendation.

### Example Input

"My car is 5 years old, has driven 50000 km and AC cooling is very low."

The system processes the natural-language description and uses the extracted information for the recommendation.

## 🔐 Security

API credentials are stored using Streamlit Secrets.

The following should **never** be uploaded to GitHub:

* API keys
* Passwords
* Tokens
* Private credentials

Only the variable name/placeholders should be documented publicly.

## 🌐 Live Application

**Live Demo:**

[https://ai-car-service-fuzzy-project-j7lvsc5agxjv8cwtgd24s6.streamlit.app/](https://ai-car-service-fuzzy-project-j7lvsc5agxjv8cwtgd24s6.streamlit.app/)

## 📦 GitHub Repository

**Source Code:**

[https://github.com/arunsonkar123/AI-Car-Service-Fuzzy-Project](https://github.com/arunsonkar123/AI-Car-Service-Fuzzy-Project)

## 📚 Project Documentation

The project documentation covers:

* Abstract
* Introduction and problem statement
* Objectives and scope
* Technologies used
* IKS connection
* System architecture
* Methodology
* AI/LLM implementation
* Fuzzy Logic implementation
* Results
* Testing
* Limitations
* Future scope
* Conclusion
* References

## ⚠️ Limitations

* The quality of AI extraction depends on the clarity of the user's description.
* The system provides recommendations and does not replace professional vehicle inspection.
* Fuzzy rules are based on the parameters defined for this project.
* Internet access is required for the cloud-hosted LLM functionality.
* API availability and usage limits can affect AI processing.

## 🚀 Future Scope

Possible improvements include:

* Adding more vehicle-service categories.
* Adding additional car parameters.
* Using historical service records.
* Adding maintenance reminders.
* Adding service-cost estimation.
* Adding multilingual natural-language input.
* Connecting the system with a real service-center database.
* Adding user accounts and service history.
* Improving fuzzy rules using real-world service data.

## 👨‍💻 Author

**Arun Sonkar**
**T.Y. IT**
**IKS Individual Project**

## 📄 Academic Project

This project was developed as an individual academic project demonstrating the integration of:

**AI/LLM + LangChain + Fuzzy Logic + Streamlit**

The system demonstrates how natural-language understanding can be combined with a fuzzy inference system to generate a car-service recommendation.


