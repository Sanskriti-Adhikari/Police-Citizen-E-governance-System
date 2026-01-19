# Police Management System

## Overview
The Police Management System is a software project designed to represent a digital platform for managing police operations and citizen services.  
The system provides separate modes for citizens and police officers, allowing structured handling of complaints, records, alerts, and officer-related data.

The project is organized into multiple versions, each extending system functionality.  
The system currently operates using demo data, with both frontend and backend components available.

---

## Version 1

Version 1 introduces core features for citizen and officer interaction.

### Citizen Mode
- Login and sign-up system  
- Filing complaints  
- Viewing public notices  
- Emergency dial functionality  

### Officer Mode
- Officer login  
- Adding and viewing complaint records  
- Officer allocation to cases  
- Case tracking  
- Receiving alerts and complaints  
- Dashboard with heatmap visualization based on complaint data  

Version 1 uses demo data. Frontend and backend components exist but operate independently.

---

## Version 2

Version 2 extends system capabilities with additional management features.

### Features
- Centralized dashboard  
- Crime records management  
- Officer information records  
- Holiday assignment for officers  
- Officer allocation by area  

---

## Trial 1

Trial 1 focuses on backend system implementation.
- Backend logic and data handling  
- API structure for system operations  
- Designed to support future frontend integration  

---

## Current Features
- Role-based access for citizens and officers  
- Login and sign-up system  
- Complaint management workflow  
- Dashboard-based data visualization  

---

## Technologies Used
- Frontend: HTML, CSS, JavaScript  
- Backend: Trial implementation  
- Data: Demo data  
- Development Environment: Visual Studio Code  

---

# How To Run (Version-1)

## Backend

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

## Frontend

cd frontend
npm install
npm start