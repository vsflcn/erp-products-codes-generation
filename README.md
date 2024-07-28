# DevOps Mini Project

This project is a simple web application built with Python Flask. The application provides an API for generating unique product codes, which is a common feature in ERP systems.

## Project Structure

devops-mini-project/
workflows/
│── ci.yml
├── Jenkinsfile
├── Dockerfile
├── app.py
├── requirements.txt
└── docker-compose.yml


## Files

- `app.py`: Main application code with endpoints for generating product codes.
- `requirements.txt`: Python dependencies for the project.
- `Dockerfile`: Docker configuration for building the application container.
- `docker-compose.yml`: Docker Compose configuration for running the application.
- `Jenkinsfile`: Jenkins pipeline configuration for CI/CD.
- `.github/workflows/ci.yml`: GitHub Actions workflow for CI/CD.

## Endpoints

- `GET /generate_code`: Generates a single unique product code.
- `POST /generate_codes`: Generates multiple unique product codes. Requires a JSON body with the field `quantity`.

## Running the Application

### Using Docker

To build and run the application using Docker:

```bash
docker build -t my-flask-app .
docker run -d -p 5000:5000 my-flask-app
```
## Using Docker Compose

To run the application using Docker Compose:
```bash
docker-compose up
```

## Jenkins

The project includes a Jenkinsfile for setting up a Jenkins pipeline. The pipeline will:

    Checkout the code from the GitHub repository.
    Build the Docker image.
    Run the Docker container.

## License

This project is licensed under the MIT License.
