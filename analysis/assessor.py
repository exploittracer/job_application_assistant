import yaml


from analysis.llm import LLMClient
from analysis.schema import JobAssessment
from analysis.prompts import ASSESSMENT_INSTRUCTIONS


class JobAssessor:

    def __init__(self):

        self.llm = LLMClient()

    def load_candidate(self, path="candidate/profile.yaml"):

        with open(path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def build_input(self, candidate, job):

        return f"""
CANDIDATE PROFILE
=================

{yaml.dump(candidate, sort_keys=False)}


JOB POSTING
===========

Source:
{job.source}

Title:
{job.title}

Company:
{job.company}

Location:
{job.location or "Not specified"}

Salary:
{job.salary or "Not specified"}

Date Posted:
{job.date_posted or "Not specified"}

Job Description:
----------------

{job.description}
"""

    def assess(self, job):

        candidate = self.load_candidate()

        input_text = self.build_input(
            candidate,
            job
        )

        return self.llm.parse(
            instructions=ASSESSMENT_INSTRUCTIONS,
            input_text=input_text,
            response_model=JobAssessment
        )

