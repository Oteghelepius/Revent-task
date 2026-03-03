A simple RESTful API built with **Flask** for managing tasks. Supports creating, updating, deleting, and listing tasks.

## Features

- Create, update, delete, and list tasks
- In-memory storage
- Dockerized application
- Kubernetes-ready deployment
- CI/CD with GitHub Actions to push Docker image and deploy to AWS EKS
- Rolling updates with `imagePullPolicy: Always`

---

## Project Structure
revent/
├── .github/
│   └── workflows/
│       └── revent.yml
├── api/
│   ├── app.py
│   └── Dockerfile
├── k8s/
│   ├── deployment.yaml
└── README.md