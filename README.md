# Online Code Editor Using CodeMirror, Django, and Compiler API

## Overview

This project is an online code editor built with Django and CodeMirror. It allows users to write, compile, and execute code in various programming languages through a web interface. The editor is styled using Bootstrap and relies on a Compiler API to handle code execution.

### Sample : 
1.![Screenshot 2024-09-07 174612](https://github.com/user-attachments/assets/146415f4-10ef-49bf-87c7-c0e98d506ae1)
2. ![Screenshot 2024-09-07 174441](https://github.com/user-attachments/assets/329fc606-04f0-46dc-8c29-2be4e4ca2186)
3.![Screenshot 2024-09-07 174539](https://github.com/user-attachments/assets/ec3ff58e-e70b-4f40-87b2-eb6985518f76)


## Features

- **Interactive Code Editing**: Utilize CodeMirror for a robust code editing experience with syntax highlighting, code completion, and more.
- **Support for Multiple Languages**: Compile and run code in Python, Java, C++, C#, and C .
- **User-Friendly Interface**: A clean, responsive design built with Bootstrap.
- **Real-Time Code Execution**: Execute code and fetch results dynamically using the Compiler API.

## Technologies Used

- **Python**: Server-side logic and backend processing using Django.
- **Django**: Web framework for routing, request handling, and backend logic.
- **HTML/CSS**: Structure and style of web pages.
- **Bootstrap**: Framework for responsive design and UI components.
- **CodeMirror**: JavaScript library for a feature-rich code editor.
- **Compiler API**: API for compiling and running code in different programming languages.
- **JavaScript**: Manages client-side interactions and API calls.
- **JSON**: Data format used for communication between the client and server.

## Installation

### Prerequisites

- Python 3.x
- Django
- Requests library

### Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ArunBhalla26/Online-Code-Editor-Using-CodeMirror-Django-and-Compiler-API.git

2. **Add a 'Static' folder containing 'CodeMirror' Library** :

   ```terminial
   Require CodeMirror version 5 or more.

3. **Start a virtual environment** :
     Add requirements.txt file
   ``` terminial
   python -m venv venv

   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4. **Install Required Packges **:
   ```terminial
   pip install -r requirements.txt
   
5.**Take Your API Key & Token** : 
    
    I have used Rapid API for the API Key and Token , you can consider that.
6.** Start Django Server** :
   ```terminial
   python manage.py runserver   
