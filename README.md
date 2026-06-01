# AI Interview Bot Frontend

## Overview

This is the Streamlit frontend for the AI Interview Bot. Users can select a topic, difficulty level, and question type to generate interview questions using the FastAPI backend.

## Features

* User-friendly interface
* Topic-based interview questions
* Difficulty selection
* Multiple question types
* Real-time AI-generated responses

## Tech Stack

* Python
* Streamlit
* Requests
* FastAPI Backend

## Project Structure

frontend/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

## Installation

Clone the repository:

git clone <frontend_repository_url>

Move to project directory:

cd frontend

Create virtual environment:

python -m venv venv

Activate virtual environment:

Windows:
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Run Application

streamlit run app.py

Application URL:

http://localhost:8501

## Backend Configuration

Update API URL:

API_URL = "https://your-render-backend-url.onrender.com"

Example:

API_URL = "https://interview-bot-backend.onrender.com"

## Usage

1. Enter Topic
2. Select Difficulty Level
3. Select Question Type
4. Click Generate Questions
5. View AI-generated interview questions

## Deployment

Platform: Streamlit Community Cloud

Main File:

app.py

Requirements File:

requirements.txt

## Author

Vinod Doddaka
