# Radiology Reporting Platform

A full-stack web application that streamlines the radiology reporting workflow by converting dictated audio into structured, editable medical reports using AI.

## Overview

The platform enables radiologists to record or upload dictations, automatically transcribe the audio, generate a structured report using a large language model (LLM), review and edit the report, and securely save it for future access.

## Features

* User authentication using JWT
* Secure role-based access to reports
* Audio transcription using AI speech-to-text
* AI-powered generation of structured radiology reports
* Editable report interface before saving
* PostgreSQL database for persistent storage
* RESTful API built with FastAPI

## Tech Stack

### Frontend

* React

### Backend

* FastAPI
* SQLAlchemy
* Alembic
* JWT Authentication

### Database

* PostgreSQL

### AI Integration

* Speech-to-Text
* Large Language Model (LLM) for report structuring

## Application Workflow

```text
Radiologist records/uploads audio
            │
            ▼
      FastAPI Backend
            │
            ▼
   Speech-to-Text Service
            │
            ▼
     Raw Transcript
            │
            ▼
Large Language Model
            │
            ▼
Structured Report (JSON)
            │
            ▼
 React Report Editor
            │
            ▼
  Doctor reviews & edits
            │
            ▼
 Stored in PostgreSQL
```

## Project Structure

```text
radiology-reporting-platform/
├── backend/
│   ├── app/
│   ├── alembic/
│   ├── requirements.txt
│   └── main.py
├── frontend/
└── README.md
```

## Current Status

This project is under active development.

### Completed

* Backend project setup
* JWT authentication
* Database schema design
* SQLAlchemy models
* Alembic migrations
* Speech-to-text integration
* AI-powered report structuring

### In Progress

* React frontend
* Report editor improvements
* Dashboard and report management
* UI enhancements

## Future Improvements

* Patient management
* Search and filtering
* Report templates
* PDF export
* Role-based access for multiple user types
* Audit logs
* Cloud deployment

## Purpose

This project was built to explore the integration of modern AI capabilities into healthcare software while strengthening full-stack development skills using React, FastAPI, PostgreSQL, and large language models.
