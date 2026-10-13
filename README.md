# AI-Powered Biometric Attendance System

A unified monorepo for a multimodal attendance platform powered by computer vision,
voice biometrics, Streamlit, and Supabase, accompanied by a dedicated web landing
page.

## Repository Structure

- **app/**: Streamlit application for live camera detection, facial embeddings,
  voice biometrics, and Supabase database interactions.
- **landing/**: Lightweight Flask application serving the marketing showcase and
  documentation portal.

## Run locally

### Streamlit application

```bash
cd app
pip install -r requirements.txt
streamlit run app.py
```

The application uses secrets for Supabase and other service credentials. Copy the
example configuration, if present, into `.streamlit/secrets.toml` and never commit
real credentials.

### Landing page

```bash
cd landing
pip install -r requirements.txt
python app.py
```

The landing page runs at `http://localhost:5002`.

## Project origin and attribution

This repository combines and adapts the following public source projects:

- [AI Attendance Project - App](https://github.com/shradha-khapra/ai-attendance-project-app)
- [AI Attendance Project - Landing](https://github.com/shradha-khapra/ai-attendance-project-landing)

The original project structure, application concepts, and source components
remain attributable to the original author and repositories. This repository
combines the two projects into one monorepo and includes my integration,
dependency, deployment, and maintenance changes.

## My contributions

- Combined the application and landing page into one repository.
- Added a unified project structure and root dependency configuration.
- Updated deployment-related dependencies and system packages.
- Repaired Python module-path handling for the application entry point.
- Replaced deprecated deployment packages with supported alternatives.
- Updated the application dependencies for face recognition and voice biometrics.
- Added documentation for running both parts locally.

## Author and maintainer

- **Kunal Soni** - https://github.com/kunalsoni20
