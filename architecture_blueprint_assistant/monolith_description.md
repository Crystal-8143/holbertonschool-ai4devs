# Monolithic Architecture - Job Tracker
Job Tracker is built as a single deployable backend application. All business modules live in one codebase, run in one process, and share one database.

- **Frontend App**: Responsive web interface used by job seekers (and coaches) to manage their search. Communicates with the backend over a single API.
- **Backend Monolith**: The one deployable unit that contains all modules below. Simplifies development, testing, and deployment for a solo project.
- **Authentication Module**: Handles registration, login (email and OAuth), sessions, optional 2FA, and role-based access for job seekers, coaches, and admins.
- **Application Tracking Module**: Core logic for creating, editing, searching, filtering, and tagging job applications.
- **Pipeline Board Module**: Manages the Kanban stages (Saved → Applied → Screening → Interview → Offer → Rejected/Withdrawn) and stage history.
- **Contacts Module**: Stores recruiters, hiring managers, and referrals, linked to specific applications.
- **Document Storage Module**: Handles upload and retrieval of resumes, cover letters, and interview notes; metadata goes to the database, files to file storage.
- **Reminders and Notifications Module**: Schedules follow-ups and deadline alerts and sends them through an external email/push provider.
- **Analytics Dashboard Module**: Calculates response rates, time-in-stage, and conversion by source from application data.
- **Calendar Integration Module**: Syncs interviews and deadlines with Google/Outlook calendars through their APIs.
- **Shared Database**: A single relational database storing all application data (users, applications, contacts, reminders, stage history).
- **File Storage**: Object or disk storage for uploaded documents.
- **External Services**: Email/push provider and calendar APIs, accessed only from the monolith.

