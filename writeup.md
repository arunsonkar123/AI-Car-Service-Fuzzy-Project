# AI-Based Car Service Recommendation System using Fuzzy Logic

## 1. Introduction
This project is a smart car service recommendation system that combines Artificial Intelligence and Fuzzy Logic. The goal is to understand a user's natural-language description of a car problem and recommend an appropriate service priority.

## 2. Problem Statement
Traditional service decisions may depend on fixed thresholds. Real-world car conditions are not always simply low or high. A car can be moderately old, moderately driven and have a fairly serious problem. Fuzzy logic is suitable because it handles such gradual conditions.

## 3. AI Component
The AI component uses LangChain and an LLM. The user can write a sentence such as: "My car is 5 years old, has driven 50,000 km and AC cooling is very low." The LLM extracts structured information such as car age, mileage, severity and problem type.

## 4. Fuzzy Logic Component
The fuzzy system has three input variables: car age, mileage and problem severity. Triangular membership functions convert crisp values into fuzzy memberships. Rules evaluate combinations of these memberships. The output variable is service priority from 0 to 100. Centroid defuzzification converts the fuzzy output into a numerical priority score.

## 5. User Interface and Deployment
The application uses Streamlit. It provides a text input, structured inputs and a recommendation button. The project can be hosted on Streamlit Community Cloud. Source code is maintained in GitHub.

## Conclusion
The project demonstrates how an LLM can understand natural language while fuzzy logic can model uncertain and gradual service conditions. The combined approach produces an understandable service recommendation and priority score.
