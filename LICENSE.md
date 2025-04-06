//main.py
from agents.jd_summarizer import summarize_jd
from agents.resume_parser import parse_resume
from agents.matcher import compute_match_score
from agents.shortlister import shortlist_candidate
from agents.scheduler import send_interview_email

jd_path = "data/jds/sample_jd.txt"

jd_path = "data/jds/sample_jd.txt"
resume_path = "data/resumes/sample_resume.pdf"

jd_summary = summarize_jd(jd_path)
resume_data = parse_resume(resume_path)

score = compute_match_score(jd_summary, resume_data)
if shortlist_candidate(score):
    send_interview_email(resume_data['email'], score)
else:
    print("Candidate not shortlisted.")


def summarize_jd(jd_path):
    with open(jd_path, 'r') as file:
        jd_text = file.read()

    summary = {
        'skills': ['Python', 'Machine Learning', 'SQL'],
        'experience': '2+ years',
        'qualification': 'Bachelor Degree in CS'
    }
    print("JD summarized:", summary)
    return summary


import PyPDF2

def parse_resume(resume_path):
    with open(resume_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = " ".join([page.extract_text() for page in reader.pages])

    resume_data = {
        'skills': ['Python', 'SQL'],
        'experience': '3 years',
        'qualification': 'Bachelor Degree in CS',
        'email': 'candidate@example.com'
    }
    print("Resume parsed:", resume_data)
    return resume_data

def compute_match_score(jd_summary, resume_data):
    jd_skills = set(jd_summary['skills'])
    resume_skills = set(resume_data['skills'])

    matched_skills = jd_skills.intersection(resume_skills)
    score = (len(matched_skills) / len(jd_skills)) * 100

    print(f"Match score: {score:.2f}%")
    return score

def shortlist_candidate(score, threshold=80):
    return score >= threshold

from utils.email_helper import send_email

def send_interview_email(to_email, score):
    subject = "Interview Invitation"
    body = f"Congratulations! Based on a {score:.2f}% match with our job description, we would like to invite you for an interview."
    send_email(to_email, subject, body)



def send_email(to_email, subject, body):
    print(f"Sending email to {to_email} with subject '{subject}':\n{body}\n")



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
