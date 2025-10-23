# flask_lab_project

## Backend Implementation – Member 1
### Files Created
#### Core Application

member1_backend/app.py – Main Flask application containing all routes and logic
member1_backend/requirements.txt – List of Python dependencies
member1_backend/templates/index.html – Homepage template for displaying and adding tasks
member1_backend/tests/test_app.py – Unit tests for route and functionality validation

### Features Implemented

#### Flask Web Server

Runs on port 5000
Serves index.html as the homepage

#### Core Routes

/ → renders homepage
/health → returns OK status for system check
/add → accepts POST request to add tasks
/toggle/<id> → toggles task completion status

#### In-Memory Data Storage

Maintains task list in runtime dictionary
Automatically updates UI on reload
Testing with Pytest
Validates each route response and status code
Confirms application bootstraps without error

### Integration Instructions

The frontend developer (Member 2) should:
Integrate templates/ from frontend into member1_backend/templates/.
Ensure all fetch requests target Flask routes (/add, /toggle/<id>, /health).
Verify CORS settings if frontend and backend run separately.

#### Testing

To test backend independently:
Create and activate Python virtual environment.
Install requirements: pip install -r requirements.txt
Run tests: pytest -q
Start app: python app.py
Visit http://localhost:5000
 and confirm health check at /health.


## DevOps Implementation – Member 3
### Files Created
#### Configuration & Automation

.github/workflows/ci_cd.yml – GitHub Actions workflow for CI/CD
member3_devops/Dockerfile – Docker image setup for Flask application
member3_devops/docker-compose.yml – Container orchestration for app + tests
member3_devops/.dockerignore – Ignored files for build optimization

#### Features Implemented

Continuous Integration (CI)
Runs Pytest automatically on every push and pull request
Checks syntax and dependencies via GitHub Actions
Continuous Delivery (CD)
Builds Docker image and pushes to Docker Hub (tagged by branch or version)
Option to deploy to a container service (Heroku, AWS ECR, or Render)

#### Dockerization

Multi-stage build for slim image
Includes Gunicorn for production serving
Health-check command defined in Compose file
Branch-Based Workflow
backend, frontend, and devops branches for isolated development
Pull Requests merged into main after pipeline success

### Integration Instructions

Ensure backend (Member 1) code passes all tests locally before pushing.
Push changes to GitHub → workflow automatically runs CI/CD pipeline.
Confirm Docker image build on GitHub Actions tab or Docker Hub.
Optionally, run locally for testing:
docker-compose up --build

Access the running app at http://localhost:5000

### Testing & Verification

Local: docker build -t flask-lab . → docker run -p 5000:5000 flask-lab

GitHub Actions: Check green ✅ status under “Actions” tab after push.

Docker Hub: Verify automatically built image is tagged correctly.
