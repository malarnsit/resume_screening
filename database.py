import sqlite3

conn = sqlite3.connect('db/recruitment.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS job_descriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    raw_text TEXT,
    summary TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS resumes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT,
    parsed_data TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS match_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER,
    resume_id INTEGER,
    score REAL,
    shortlisted BOOLEAN
)''')

c.execute('''CREATE TABLE IF NOT EXISTS interviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resume_id INTEGER,
    job_id INTEGER,
    scheduled_time TEXT,
    email_status TEXT
)''')

conn.commit()
conn.close()

