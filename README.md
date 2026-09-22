# AI-Based Car Service Recommendation System using Fuzzy Logic

## Problem
Car owners may not know which service is required or how urgently it should be performed.

## Solution
This mini project combines an LLM through LangChain with a genuine fuzzy inference system.

## AI/LLM component
The user can describe a car problem in natural language. LangChain sends the text to an LLM, which extracts:
- car age
- mileage
- problem severity
- problem description

## Fuzzy Logic component
The extracted/entered values are fuzzified using triangular membership functions.

Inputs:
- Car age: New / Medium / Old
- Mileage: Low / Medium / High
- Severity: Low / Medium / High

Output:
- Service priority: Low / Medium / High

The system evaluates fuzzy rules and uses centroid defuzzification to produce a priority score from 0 to 100.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

For the AI feature, configure `OPENAI_API_KEY`. Without the key, the structured inputs still demonstrate the fuzzy inference system.

## Deployment
Deploy `app.py` and `requirements.txt` on Streamlit Community Cloud. Add `OPENAI_API_KEY` in the app's Secrets settings.
