# demo_web

https://demoweb-hgy9hnozudsgdfcdcwddyq.streamlit.app/

# 📝 Streamlit Student Information Form

A simple **Streamlit web application** that collects basic student information through an interactive form and displays the submitted details.

## 🚀 Features

* Enter student's **Name**
* Enter **Father's Name**
* Enter **Address**
* Select **Class** from a dropdown
* Submit information using a **Done** button
* Display entered information dynamically
* Simple and beginner-friendly Streamlit UI

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Pandas**

## 📂 Project Structure

```text
Streamlit-Student-Form/
│
├── streamlit.py
├── README.md
└── modified_data.csv
```

## 📦 Installation

First, install the required libraries:

```bash
pip install streamlit pandas
```

## ▶️ How to Run

Open the project folder in your terminal and run:

```bash
streamlit run streamlit.py
```

Streamlit will start the application in your browser.

## 💻 Code Overview

The application uses Streamlit widgets to collect user information:

```python
name = st.text_input("Enter your name :")
Fname = st.text_input("Enter your Father name")
Adr = st.text_area("Enter text :")

classdata = st.selectbox(
    "Enter your class :",
    (1, 2, 3, 4, 5, 6)
)

button = st.button("Done")
```

When the **Done** button is clicked, the entered information is displayed:

```python
if button:
    st.markdown(f"""
    Name : {name}
    Father Name : {Fname}
    Address : {Adr}
    Class : {classdata}
    """)
```

## 📊 Streamlit Components Used

| Component         | Purpose                     |
| ----------------- | --------------------------- |
| `st.text_input()` | Takes text input            |
| `st.text_area()`  | Takes multi-line text       |
| `st.selectbox()`  | Provides dropdown selection |
| `st.button()`     | Creates a clickable button  |
| `st.markdown()`   | Displays formatted text     |
| `st.dataframe()`  | Displays Pandas DataFrame   |

## 📌 Future Improvements

This project can be extended by adding:

* Form validation
* Email and phone number fields
* Submit form using `st.form()`
* Store data in CSV/MySQL
* Edit and delete student records
* Login/authentication
* Better UI styling
* Student data dashboard

## 🎯 Learning Objective

This project was created to understand the basics of **Streamlit**, including creating UI components, taking user input, handling button events, and displaying dynamic data.

## 👨‍💻 Author

**Alok Kumar**

Student | Python | Machine Learning | Deep Learning

---

⭐ If you found this project useful, consider giving the repository a star!
