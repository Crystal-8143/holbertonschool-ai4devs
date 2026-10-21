## Carpool Connect - User Stories

### User Story 1: Create a User Profile
As a user, I want to create a profile so that I can use Carpool Connect and share basic information with other ride participants.

**Acceptance Criteria**:
- The user can register with the required account details.
- The system validates required fields and displays a clear error message when information is missing or invalid. 
- After successful registration, the user can access their profile.

**Priority**: MVP

### User Story 2: Publish a Ride
As a driver, I want to publish a ride with my route and schedule so that passengers travelling in the same direction can find a seat.

**Acceptance Criteria**:
- The driver can enter a starting location, destination, date, departure time, available seats, and suggested cost contribution.
- The system prevents the driver from publishing a ride if required details are missing or invalid.
- After publishing, the ride appears in search results for matching journeys.

**Priority**: MVP

### User Story 3: Search for Available Rides
As a passenger, I want to search for rides by route and travel date so that I can find a suitable carpool.

**Acceptance Criteria**:
- The passenger can enter a starting location, destination, and travel date.
- The system displays rides that match the search and have seats available.
- Each result shows the driver's profile, departure time, route, available seats, and cost contribution.

**Priority**: MVP

### User Story 4: View Ride Details
As a passenger, I want to view a ride's full details so that I can decide whether it meets my travel needs before requesting a seat.

**Acceptance Criteria**:
- The ride details show the pickup and destination locations, date, departure time, available seats, and cost contribution.
- The passenger can view the driver's basic profile and ratings, when available.
- The passenger can return to the search results without losing their search criteria.

**Priority**: MVP

### User Story 5: Request a Seat
As a passenger, I want to request an available seat so that I can ask the driver to include me in the trip.

**Acceptance Criteria**:
- A passenger can submit a request for a ride that has an available seat.
- The system confirms that the request has been submitted and marks it as pending.
- The passenger cannot submit duplicate active requests for the same ride.

**Priority**: MVP

### User Story 6: Manage Ride Requests
As a driver, I want to accept or decline passenger requests so that I can manage who joins my ride.

**Acceptance Criteria**:
- The driver can view pending requests for rides they have published.
- The driver can accept or decline each pending request.
- When a request is accepted, the system updates the request status and adjusts the remaining seat availability.

**Priority**: MVP

### User Story 7: View Request Status
As a passenger, I want to see the status of my ride requests so that I know whether my seat has been confirmed.

**Acceptance Criteria**:
- The passenger can view their submitted requests and their current statuses.
- Each request is clearly labelled as pending, accepted, or declined.
- The status is updated after the driver makes a decision.

**Priority**: MVP

### User Story 8: Edit or Cancel a Published Ride
As a driver, I want to edit or cancel a ride I have published so that I can keep the listing accurate when my plans change.

**Acceptance Criteria**:
- The driver can edit the details of a ride they own, subject to validation.
- The driver can cancel a ride and is asked to confirm the cancellation.
- Passengers with accepted requests are informed in the application that the ride has changed or been cancelled.

**Priority**: High

### User Story 9: Share Travel Costs
As a driver, I want to display the expected cost contribution per passenger so that everyone understands the proposed travel costs before confirming a ride.

**Acceptance Criteria**:
- The driver can enter a proposed cost contribution when creating or editing a ride.
- The proposed contribution is visible in ride search results and ride details.
- The system identifies the amount as a contribution estimate rather than an automatically processed payment.

**Priority**: High

### User Story 10: Rate a Completed Ride
As a passenger or driver, I want to rate the other participants after a completed ride so that future users can make more informed decisions.

**Acceptance Criteria**:
- A user can submit a rating from 1 to 5 after a ride is marked as completed.
- Only users associated with that ride can submit a rating for another participant.
- The system prevents a user from submitting more than one rating for the same participant on the same ride.

**Priority**: Medium

### User Story 11: Receive Ride Notifications
As a passenger or driver, I want to receive notifications about important ride updates so that I do not miss requests, confirmations, or cancellations.

**Acceptance Criteria**:
- The system creates an in-app notification when a request is accepted or declined.
- The system creates an in-app notification for affected participants when a confirmed ride is cancelled.
- Each notification identifies the relevant ride and update.

**Priority**: Medium

### User Story 12: View Environmental Impact
As a user, I want to see an estimate of the emissions saved by sharing a ride so that I can understand the potential environmental benefit of carpooling.

**Acceptance Criteria**:
- The system displays an estimated environmental impact for a completed shared ride when sufficient trip information is available.
- The estimate is labelled as approximate and is based on stated assumptions.
- If required information is unavailable, the system explains why an estimate cannot be shown.

**Priority**: Low