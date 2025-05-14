# CVScore
Sorting and scoring CVs based on job descriptions using FastAPI, LangChain, and LLMs

## System flow:

```mermaid
graph TD;
    A[Create Job with detail description] --> B[get job_id]
    B --> C[Upload CVs with Job Id]
    C --> D[get score in the scale of 0-10 for each of the uploaded CVs]
```
