from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class Job(Base):

    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    source: Mapped[str] = mapped_column(
        String(100)
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    company: Mapped[str] = mapped_column(
        String(255)
    )

    location: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    salary: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    url: Mapped[str] = mapped_column(
        String(1000),
        unique=True
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    date_posted: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    date_found: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


class Assessment(Base):

    __tablename__ = "assessments"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey("jobs.id")
    )

    fit_score: Mapped[int]

    recommendation: Mapped[str] = mapped_column(
        String(50)
    )

    match_level: Mapped[str] = mapped_column(
        String(100)
    )

    strengths: Mapped[str] = mapped_column(
        Text
    )

    transferable_skills: Mapped[str] = mapped_column(
        Text
    )

    skill_gaps: Mapped[str] = mapped_column(
        Text
    )

    mandatory_failures: Mapped[str] = mapped_column(
        Text
    )


class Application(Base):

    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey("jobs.id")
    )

    cover_letter: Mapped[str] = mapped_column(
        Text
    )

    ats_cover_letter: Mapped[str] = mapped_column(
        Text
    )

    reason_for_applying: Mapped[str] = mapped_column(
        Text
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )