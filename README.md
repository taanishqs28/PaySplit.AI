# PaySplit.AI

**PaySplit.AI** is a portfolio-ready SaaS project designed for freelancers, gig workers, and side hustlers to track and manage their finances.  
It enables users to upload bank transaction CSVs, view summaries, and lays the foundation for advanced AI-powered categorization and tax estimation.

> This project demonstrates production-grade backend API development (FastAPI, PostgreSQL), robust error handling, modular design, and a clear roadmap for future extensibility (AI, frontend, multi-user, etc.).

---

## ✨ Version 1: Completed Features

- **CSV Upload & Parsing:** Upload bank transaction CSVs, parsed using `pandas`.
- **API Endpoints:** RESTful endpoints to upload, list, retrieve, and summarize transactions.
- **Database Integration:** PostgreSQL with SQLAlchemy ORM; tables auto-created if missing.
- **Error Handling:** Robust responses for bad files, missing fields, and server errors.
- **Automated Tests:** Pytest coverage for upload, parsing, and error cases.
- **API Versioning:** All endpoints under `/api/v1/` for future-proofing.
- **Modular Codebase:** Structured for maintainability and extensibility.
- **Environment Management:** Uses `python-dotenv` for configuration.
- **Production-Ready:** Clean, documented, and ready for portfolio/interview use.

---

## 🛠️ Tech Stack

| Layer       | Tech                                      |
|-------------|-------------------------------------------|
| Backend     | Python, FastAPI, Uvicorn, Pandas, SQLAlchemy |
| Database    | PostgreSQL                                |
| Frontend    | Next.js (planned)                         |
| AI          | OpenAI API (planned)                      |
| Dev Tools   | VS Code, Git, GitHub, pytest              |

---

## 🚀 Getting Started

### Backend (FastAPI)

1. **Navigate to the server folder**
    ```bash
    cd server
    ```

2. **Create virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the backend**
    ```bash
    uvicorn app.main:app --reload --port 4000
    ```

5. **Test in your browser:**
    - Visit http://localhost:4000/docs
    - Upload a sample .csv to the `/api/v1/upload` endpoint

---

## 🏁 Version 1 Overview

- **Single-user backend:** All core features for uploading, storing, and summarizing transactions.
- **Robust error handling:** Clear HTTP responses for all error cases.
- **Automated tests:** Ensures reliability and correctness.
- **Ready for extension:** Designed for easy addition of AI, frontend, and multi-user features.

---

## 🛣️ Roadmap & Future Updates

### Planned Features

- **AI-Powered Categorization:** Use OpenAI to auto-categorize transactions.
- **Business/Personal Split:** Mark and split transactions for business vs. personal use.
- **State-Based Tax Logic:** Estimate taxes based on user’s state.
- **Frontend UI:** Next.js dashboard for uploads, summaries, and visualizations.
- **User Authentication:** Multi-user support and secure login.
- **CRUD Endpoints:** Update, delete, and filter transactions.
- **PDF Export:** Download transaction summaries for tax filing.
- **Third-Party Integrations:** Plaid/Stripe for automated bank data import.
- **CI/CD Pipeline:** Automated testing and deployment.
- **Alembic Migrations:** Database schema versioning.
- **End-to-End Tests:** Full workflow coverage.
- **Security & DevOps:** Best practices for production SaaS.

---

## 📌 Project Goals

- Build a full-stack, production-grade SaaS app from scratch.
- Demonstrate backend skills (FastAPI, PostgreSQL, error handling, testing).
- Prepare a standout portfolio project for interviews.
- Help freelancers and gig workers manage finances with ease.

---

## 📬 Contact

**Built by: Taanishq Sethi**  
- GitHub:   https://github.com/taanishqs28  
- LinkedIn: https://www.linkedin.com/in/taanishq-sethi/  
- Email:    taanishqsethi28@gmail.com  