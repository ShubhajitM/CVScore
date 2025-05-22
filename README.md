# CVScore
Sorting and scoring CVs based on job descriptions using FastAPI, LangChain, and LLMs

## Set Up

```sh
conda create --name cv-score python=3.11

conda activate cv-score

pip install -r requirements.txt 

python main.py
```

## System flow:

```mermaid
graph TD;
    A[Create Job with detail description] --> B[get job_id]
    B --> C[Upload CVs with Job Id]
    C --> D[get score in the scale of 0-100 for each of the uploaded CVs]
```
