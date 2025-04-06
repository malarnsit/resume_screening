# agents/jd_summarizer.py

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
