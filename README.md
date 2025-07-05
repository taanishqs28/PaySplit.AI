# PaySplit.AI

**PaySplit.AI** is an AI-powered financial tracker built for freelancers, gig workers, and side hustlers.  
It helps users import their transaction history, categorize expenses as business or personal, and estimate taxes — all from a clean and modern interface.

> This is a full-stack project built to showcase my skills in backend API development (FastAPI), frontend UI (Next.js), file parsing, AI integration (OpenAI), and database design.

---

## ✨ Features

- ✅ Upload CSV files of transactions
- ✅ Parse and display transactions using `pandas`
- ✅ Clean, modular FastAPI backend
- ✅ Future: AI-powered categorization (OpenAI)
- ✅ Future: Frontend UI for uploading + dashboard
- ✅ Future: PostgreSQL database for persistent storage

---

## 🛠️ Tech Stack

| Layer       | Tech                             |
|------------|----------------------------------|
| Backend     | Python, FastAPI, Uvicorn, Pandas |
| Frontend    | Next.js (coming soon)            |
| AI          | OpenAI API (for smart categorization) |
| Database    | PostgreSQL (planned)             |
| Dev Tools   | VS Code, Git, GitHub             |

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
source venv/bin/activate # or venv\Scripts\activate on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Run the backend**
```bash
uvicorn app.main:app --reload --port 4000
```
5. **Test it in your browser:**
- Visit http://localhost:4000/docs
- Upload a sample .csv to the /upload endpoint

# 📌 PROJECT GOALS
- Build a full-stack production-grade app from scratch
- Strengthen FastAPI backend skills (async, modular, clean)
- Practice real-world file handling, error catching, and logging
- Integrate OpenAI for real transaction classification
- Prep a standout portfolio project for interviews
- Learn how to parse, clean, and manage financial data
- Build a useful tool for freelancers, gig workers, and creators

# 🛣 ROADMAP

- [x] Set up FastAPI backend structure
- [x] Enable CSV upload and parsing via pandas
- [x] Add CORS and API versioning
- [ ] Handle upload edge cases (bad file, missing columns, etc)
- [ ] Add OpenAI for category + business/personal suggestions
- [ ] Build frontend UI with Next.js + Tailwind
- [ ] Add income/expense visualization (Recharts)
- [ ] Add transaction tagging (personal, business, %, etc)
- [ ] Estimate quarterly taxes
- [ ] Add PostgreSQL for data persistence
- [ ] Add auth (Clerk.dev or Supabase Auth)
- [ ] Generate PDF tax summary
- [ ] Deploy backend + frontend

# 📬 CONTACT

**Built by: Taanishq Sethi**
- GitHub:   https://github.com/taanishqsethi
- LinkedIn: https://linkedin.com/in/taanishqsethi
- Email:    taanishqsethi28@gmail.com 