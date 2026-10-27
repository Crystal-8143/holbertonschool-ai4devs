# Microservices Architecture - Job Tracker
The monolith is decomposed into independent services, each owning its own data and communicating through an API Gateway, direct service-to-service calls, and asynchronous events on a message broker.

- **Frontend App**: Responsive web client for job seekers and coaches. Talks only to the API Gateway.
- **API Gateway**: Single entry point. Routes requests to services, verifies tokens issued by the Auth Service, and applies rate limiting.
- **Auth Service**: Handles registration, login (email and OAuth), sessions, 2FA, and role-based access (job seeker, coach, admin). Owns the Auth DB.
- **Application Service**: Core CRUD for job applications (company, role, link, salary, source, tags) plus search and filtering. Publishes events such as `application.created` and `application.updated`.
- **Pipeline Service**: Manages Kanban stages and stage history (Saved → Applied → Screening → Interview → Offer → Rejected/Withdrawn). Publishes `stage.changed` events.
- **Contacts Service**: Stores recruiters, hiring managers, and referrals, linked to applications by ID.
- **Document Service**: Manages resumes, cover letters, and notes. Metadata lives in its own database, files in object storage.
- **Reminder Service**: Schedules follow-ups and deadline alerts. Consumes application and stage events (for example, auto-creating a "follow up in 7 days" reminder when an application moves to Applied) and triggers the Notification Service.
- **Notification Service**: Delivers email and push messages through an external provider. Isolated so provider changes do not affect other services.
- **Analytics Service**: Consumes events to build response-rate, time-in-stage, and conversion-by-source metrics in a read-optimized store.
- **Calendar Integration Service**: Syncs interviews and deadlines with Google/Outlook calendars and handles OAuth tokens for those providers.
- **Message Broker**: Asynchronous event bus (for example RabbitMQ or Kafka) that decouples publishers from consumers.
- **Database per Service**: Each service owns its data store and no other service reads it directly, which preserves independence.