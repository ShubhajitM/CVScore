import os
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
import json
import re


class CVScoring:
    def __init__(self):
        load_dotenv()
        self.llm = GoogleGenerativeAI(model="gemini-2.0-flash")

    async def score_cv(self, job_description, cv_file: str) -> dict:
        # Placeholder for CV scoring logic
        # In a real implementation, you would process the CV file and score it

        prompt_template = PromptTemplate(
            input_variables=["job_description", "cv_content"],
            template="""
        You are an expert HR professional tasked with evaluating a candidate's CV against a specific job description. Your goal is to score the CV out of 100 based on its relevance to the job, including skills, experience, education, and overall alignment. Provide a detailed feedback explaining the score, highlighting strengths, weaknesses, and suggestions for improvement.

        **Input Details:**
        - **Job Description**: {job_description}
        - **CV Content**: {cv_content} The CV content will be provided in the base64 encoded format.

        **Instructions:**
        1. Analyze the CV content and job description thoroughly.
        2. Evaluate how well the candidate's skills, experience, and education match the job requirements.
        3. Assign a score between 0 and 100, where:
           - 90-100: Exceptional match
           - 80-89: Strong match
           - 70-79: Good match
           - 60-69: Moderate match
           - Below 60: Poor match
        4. Provide feedback that includes:
           - Strengths: What aligns well with the job description.
           - Weaknesses: Gaps or areas that don't meet the job requirements.
           - Suggestions: How the candidate can improve their CV or qualifications for this role.
        ** Output Format: (JSON format)** ONLY RETURN THE JSON RESPONSE
        - score: integer (0-100)
        - feedback: text (maximum 128 characters)
        """,
        )
        prompt = prompt_template.format(
            job_description=job_description, cv_content=cv_file
        )

        llm_raw_reponse = self.llm.invoke(prompt)
        # Extract JSON from markdown code block
        json_match = re.search(r"```json\s*(\{.*?\})\s*```", llm_raw_reponse, re.DOTALL)
        llm_response = json_match.group(1)

        print(f"LLM Response: {llm_response}")
        return json.loads(llm_response)


# Singleton instance of CVScoring
cv_scoring = CVScoring()
