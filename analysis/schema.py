from typing import List

from pydantic import BaseModel, Field


class Requirement(BaseModel):

    requirement: str

    category: str

    importance: str

    candidate_match: str

    evidence: str

    gap: str


class JobAssessment(BaseModel):

    fit_score: int = Field(
        ge=0,
        le=100
    )

    recommendation: str

    match_level: str

    role_summary: str

    strengths: List[str]

    transferable_skills: List[str]

    skill_gaps: List[str]

    experience_gaps: List[str]

    education_gaps: List[str]

    mandatory_failures: List[str]

    learning_priorities: List[str]

    requirements: List[Requirement]

    reasoning: str