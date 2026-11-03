# API Requirements – Job Tracker API

## Domain Overview
Job search management.

The Job Tracker API allows job seekers to manage their job applications, track their progress through hiring stages, attach notes and contacts, and review their application statistics.

The API provides communication between the frontend application and backend services, allowing users to create, retrieve, update, delete, search, and organise their job applications.

## Target Users

- **Job seekers:** Create and manage job applications, track hiring stages, and record notes and contacts.
- **Developers:** Build web and mobile applications that communicate with the API.
- **Career coaches / analysts:** Access application statistics and progress reports when explicitly authorised by the user.

## Core Operations

### Applications
1. **Create application** – `POST /v1/applications` – Create a new job application.
2. **Get application by ID** – `GET /v1/applications/{id}` – Retrieve details of a specific application.
3. **List / search applications** – `GET /v1/applications` – Retrieve, search, filter, and sort applications.
4. **Update application** – `PATCH /v1/applications/{id}` – Update existing application details.
5. **Delete application** – `DELETE /v1/applications/{id}` – Soft-delete an application.

### Stages
6. **List stages** – `GET /v1/stages` – Retrieve the user's available application stages.
7. **Create custom stage** – `POST /v1/stages` – Create a custom application stage.
8. **Move application to stage** – `POST /v1/applications/{id}/stage` – Change an application's current stage and record the change.
9. **Get stage history** – `GET /v1/applications/{id}/stage-history` – Retrieve the history of an application's stage changes.

### Notes and Contacts
10. **Add note** – `POST /v1/applications/{id}/notes` – Add notes to a job application.
11. **Add contact** – `POST /v1/applications/{id}/contacts` – Add recruiter or hiring manager contact information.

### Reporting
12. **Get stage summary** – `GET /v1/reports/stages` – Retrieve application counts, stage conversion rates, and average time spent in each stage.

## Data Validation Rules

### Application
- `company_name`: Required string, 1–100 characters.
- `job_title`: Required string, 1–150 characters.
- `job_url`: Optional, valid `HTTP` or `HTTPS` URL, maximum 2048 characters.
- `location`: Optional string, maximum 100 characters.
- `salary_min`: Optional integer, minimum value 0.
- `salary_max`: Optional integer, minimum value 0; must be greater than or equal to salary_min.
- `applied_date`: Valid ISO 8601 date (`YYYY-MM-DD`); cannot be in the future.
- `source`: Optional; must be one of `linkedin`, `company_site`, `referral`, `recruiter`, `job_board`, or `other`.
- `stage_id`: Required; must reference a stage belonging to the authenticated user.
- Duplicate active applications with the same `company`, `job title`, and `job URL` are not permitted.

### Stage
- `name`: Required string, 1–50 characters; must be unique per user (case-insensitive).
- `position`: Required integer, minimum value 1; must be unique per user.
- Default stages cannot be deleted.
- Custom stages cannot be deleted while applications reference them.
- Stage changes must reference an existing stage belonging to the user.
- Moving an application to its current stage is not permitted.
- Moving an application out of a terminal stage (Accepted, Rejected, Withdrawn) requires a comment.

**Default stages:**
- Wishlist
- Applied
- Screening
- Interview
- Offer
- Accepted
- Rejected
- Withdrawn

### Notes
- `content`: Required string, 1–5000 characters.
- Notes must belong to an existing application owned by the authenticated user.
- HTML tags must be escaped when displaying note content.

### Contacts
- `name`: Required string, 1–100 characters.
- `email`: Optional, valid email address, maximum 254 characters.
- `phone`: Optional, valid E.164 phone number format.
- `role`: Optional string, maximum 100 characters.

### General Validation
- All IDs must use UUIDv4 format.
- All timestamps must use UTC and ISO 8601 format.
- Unknown fields in request bodies must be rejected with `400 Bad Request`.
- `Pagination parameters`:
    - `limit`: Integer between 1 and 100 (default 20).
    - `offset`: Integer greater than or equal to 0.
- Validation errors must return a consistent JSON response identifying invalid fields and reasons.

## Non-Functional Requirements

### Performance and Latency
- Read endpoints (`GET`) must achieve a p95 response time below 200ms.
- Write endpoints (`POST`, `PATCH`, `DELETE`) must achieve a p95 response time below 400ms.
- Reporting endpoints must achieve a p95 response time below 800ms for up to 10,000 applications per user.

### Authentication and Authorisation
- JWT bearer authentication is required for all protected endpoints.
- Public endpoints are limited to:
    - `/v1/auth/register`
    - `/v1/auth/login`
    - `/v1/health`
- Access tokens expire after 15 minutes.
- Refresh tokens expire after 7 days.
- Users can only access, modify, and delete their own applications, stages, notes, and contacts.
- Career coaches and analysts must have explicit permission from the user and read-only access to shared data.

### Rate Limiting
- Authenticated users are limited to 100 API requests per minute.
- Authentication endpoints are limited to 10 requests per minute per IP address.
- Exceeding rate limits must return `429 Too Many Requests` with a `Retry-After` header.

### Availability and Reliability
- Target monthly uptime is 99.5%.
- Errors must return consistent HTTP status codes and meaningful error messages.
- Stage changes must be atomic: the application's current stage and its stage history entry must be saved together or not at all.
- Deleted applications must be recoverable for 30 days before permanent deletion.

### Security
- All API communication must use HTTPS with TLS 1.2 or higher.
- Passwords must be securely hashed using bcrypt or Argon2.
- Passwords must never be returned in API responses.
- Input must be validated and sanitised to prevent injection attacks.
- CORS must be restricted to configured origins.
- Users must not be able to access another user's private data.

### API Design Conventions
- Follow RESTful API design principles.
- Use JSON for requests and responses.
- Version endpoints under `/v1`.
- Use standard HTTP methods:
    - `GET` – Retrieve information.
    - `POST` – Create resources or perform actions.
    - `PATCH` – Update existing resources.
    - `DELETE` – Remove resources.
- Use appropriate HTTP status codes:
    - `200` – Successful request.
    - `201` – Resource created.
    - `204` – Successful deletion.
    - `400` – Invalid request.
    - `401` – Unauthenticated request.
    - `403` – Access forbidden.
    - `404` – Resource not found.
    - `409` – Resource conflict.
    - `422` – Unprocessable entity.
    - `429` – Too many requests.
    - `500` – Internal server error.
- Publish API documentation using the OpenAPI 3.0 specification at `/docs`.
- Include an `X-Request-ID` header in responses for request tracing.

### Observability
- Maintain structured logs for every request, including HTTP method, endpoint, response status, latency, and request ID.
- Do not include passwords, authentication tokens, or sensitive personal information in logs.
- Provide a `/v1/health` endpoint to report API and database health.