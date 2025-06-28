# SecureFlaskEdge:

A full-stack, containerized microservice with modular Python decorators for logging, authentication, and rate limiting—designed for cloud-native deployments (Docker, CI/CD, HTTPS, and Azure-ready).

```
Folder Structure
-----------------------
flask-decorator-stack/
├── app.py
├── db.py
├── config.py
├── requirements.txt
├── decorators/
│   ├── __init__.py
│   ├── log_request.py
│   ├── auth_required.py
│   └── rate_limiter.py



SQL Setup
---------------------------
Run in PostgreSQL shell:
CREATE DATABASE flask_logs;
\c flask_logs
CREATE TABLE api_logs (
    id SERIAL PRIMARY KEY,
    prefix TEXT,
    endpoint TEXT,
    method TEXT,
    duration_ms FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```
