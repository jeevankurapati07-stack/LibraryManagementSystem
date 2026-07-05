# Library Management System

A production-grade, console-based Library Management System developed in Python 3 following strict Object-Oriented Programming (OOP) and Database configuration patterns.

## Key Features Met
* **OOP Entities:** Engineered explicit domain objects (`Book`, `Member`, `Transaction`) using classes to segregate logic layers cleanly.
* **Database Persistency:** Leveraged SQLite relational engines to track book records and automated live inventory checkings dynamically.
* **Workflow Defenses:** Integrated robust verification modules preventing operations from parsing logic failures (e.g., checking inventory levels before processing issues).
* **Decoupled Architecture:** Reused clean folder separation principles ensuring config vectors remain hidden securely within local environments.

## Setup Requirements
1. Install dependencies: `pip install python-dotenv`
2. Fire up the dashboard terminal environment: `python main.py`