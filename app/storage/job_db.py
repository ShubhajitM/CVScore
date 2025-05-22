import datetime
import uuid


class BaseEntity:
    def __init__(self):
        createdAt: datetime = datetime.now()
        updatedAt: datetime = datetime.now()


class JobDetailsEntity(BaseEntity):
    def __init__(
        self, job_id: uuid.UUID, job_title: str, job_description: str, job_type: str
    ):
        self.job_id = job_id
        self.job_title = job_title
        self.job_description = job_description
        self.job_type = job_type

    @staticmethod
    def add_job_details(
        job_id: uuid.UUID, job_title: str, job_description: str, job_type: str
    ):
        job_details = JobDetailsEntity(job_id, job_title, job_description, job_type)
        job_details_map[job_id] = job_details

    @staticmethod
    def get_job_details(job_id: uuid.UUID):
        return job_details_map.get(str(job_id), None)


job_details_map: dict[str, any] = {
    "123e4567-e89b-12d3-a456-426614174000": """
            Job Purpose:

            Mandatory skills: Java, Spring, Spring boot, MS SQL, Microservices Architecture, Familiarity with RESTful APIs and web services.

            Desired Skills :Experience with containerization (e.g., Docker), Microsoft Azure CI/CD

            
            Relevant years of experience :5

            Industry & Education background : Bachelor’s degree in computer science, Information Technology, or a related field.

            
            Roles & Responsibilities:

            Design, develop, and maintain scalable applications using Java, Spring, and Spring Boot while collaborating with cross-functional teams to define and ship new features.

            Write clean, efficient code, troubleshoot applications for optimal performance, participate in code reviews, stay updated on technologies, and contribute to all phases of the development lifecycle.
       """
}
