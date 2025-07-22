import os
from fastapi import FastAPI, HTTPException
import requests
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

app = FastAPI()

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

@app.get('/repo/{owner}/{repo}/issues')
def get_good_first_issues(owner: str, repo: str):
    url = f'https://api.github.com/repos/{owner}/{repo}/issues'
    params = {
        'state': 'open',
        'labels': 'good first issue,help wanted'
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch issues.")

    issues = response.json()
    filtered = [
        {
            'title': issue.get('title'),
            'url': issue.get('html_url'),
            'labels': [label['name'] for label in issue.get('labels', [])],
        }
        for issue in issues if issue.get('pull_request') is None
    ]

    return {'repo': f'{owner}/{repo}', 'issues': filtered}
