\# GitOps Kubernetes Platform



> \*\*Automated CI/CD and GitOps deployment platform using Flask, Docker, Kubernetes, GitHub Actions, Docker Hub, Minikube, and ArgoCD.\*\*



\## 📌 Overview



The \*\*GitOps Kubernetes Platform\*\* is a DevOps project that demonstrates an end-to-end automated application deployment workflow.



The project uses a Flask application that is containerized with Docker, automatically built and pushed to Docker Hub using GitHub Actions, and deployed to Kubernetes through ArgoCD.



Git is used as the \*\*single source of truth\*\* for the desired Kubernetes configuration.



\### Deployment Flow



```text

Developer

&#x20;   │

&#x20;   │ git push

&#x20;   ▼

GitHub Repository

&#x20;   │

&#x20;   ▼

GitHub Actions

&#x20;   │

&#x20;   ├── Build Docker Image

&#x20;   ├── Push Image to Docker Hub

&#x20;   └── Update Kubernetes Manifest

&#x20;           │

&#x20;           ▼

&#x20;     Git Commit \& Push

&#x20;           │

&#x20;           ▼

&#x20;         ArgoCD

&#x20;           │

&#x20;      Automatic Sync

&#x20;           │

&#x20;           ▼

&#x20;  Minikube / Kubernetes

&#x20;           │

&#x20;           ▼

&#x20;    Flask Application

&#x20;           │

&#x20;           ▼

&#x20;      Healthy Pods

```



\---



\## 🎯 Objectives



\- Containerize a Flask application using Docker.

\- Deploy the application on Kubernetes.

\- Run Kubernetes locally using Minikube.

\- Implement Continuous Integration using GitHub Actions.

\- Automatically build and push Docker images to Docker Hub.

\- Automatically update Kubernetes deployment manifests.

\- Implement GitOps using ArgoCD.

\- Automatically synchronize Git changes with Kubernetes.

\- Perform Kubernetes rolling updates.

\- Implement readiness and liveness health checks.

\- Maintain Git as the source of truth for Kubernetes configuration.



\---



\## 🏗️ Architecture



```text

┌─────────────────────┐

│     Developer       │

│   Application Code  │

└──────────┬──────────┘

&#x20;          │

&#x20;          │ git push

&#x20;          ▼

┌─────────────────────┐

│       GitHub        │

│     Repository      │

└──────────┬──────────┘

&#x20;          │

&#x20;          ▼

┌─────────────────────┐

│   GitHub Actions    │

│        CI           │

├─────────────────────┤

│ Checkout            │

│ Docker Buildx       │

│ Docker Login        │

│ Build \& Push        │

│ Update K8s Manifest │

│ Commit \& Push       │

└──────────┬──────────┘

&#x20;          │

&#x20;          ├──────────────────────┐

&#x20;          ▼                      ▼

┌─────────────────────┐  ┌─────────────────────┐

│     Docker Hub      │  │       GitHub        │

│   Docker Image      │  │ Updated K8s Manifest│

└─────────────────────┘  └──────────┬──────────┘

&#x20;                                   │

&#x20;                                   │ Git Change

&#x20;                                   ▼

&#x20;                          ┌─────────────────────┐

&#x20;                          │       ArgoCD        │

&#x20;                          │      GitOps CD       │

&#x20;                          └──────────┬──────────┘

&#x20;                                     │

&#x20;                              Automatic Sync

&#x20;                                     │

&#x20;                                     ▼

&#x20;                          ┌─────────────────────┐

&#x20;                          │      Minikube       │

&#x20;                          │     Kubernetes      │

&#x20;                          ├─────────────────────┤

&#x20;                          │ Namespace           │

&#x20;                          │ Deployment          │

&#x20;                          │ Service             │

&#x20;                          │ 2 Replicas          │

&#x20;                          └──────────┬──────────┘

&#x20;                                     │

&#x20;                                     ▼

&#x20;                          ┌─────────────────────┐

&#x20;                          │   Flask Application │

&#x20;                          │       Healthy       │

&#x20;                          └─────────────────────┘

```



\---



\## 🧰 Technology Stack



| Technology | Purpose |

|---|---|

| Python | Application development |

| Flask | Web application framework |

| Docker | Containerization |

| Docker Hub | Container image registry |

| Kubernetes | Container orchestration |

| Minikube | Local Kubernetes cluster |

| kubectl | Kubernetes management |

| ArgoCD | GitOps continuous delivery |

| GitHub | Source control and GitOps repository |

| GitHub Actions | Continuous Integration |

| YAML | Kubernetes and CI/CD configuration |

| PowerShell | Local development environment |



\---



\## 📂 Project Structure



```text

gitops-kubernetes-platform/

│

├── app/

│   ├── app.py

│   ├── Dockerfile

│   └── requirements.txt

│

├── k8s/

│   ├── deployment.yaml

│   ├── namespace.yaml

│   └── service.yaml

│

├── argocd/

│   └── application.yaml

│

├── .github/

│   └── workflows/

│       └── build-and-push.yml

│

├── screenshots/

│   └── Project evidence screenshots

│

└── README.md

```



\---



\# 🐍 Application



The application is a Flask-based web service designed to demonstrate containerization, Kubernetes deployment, health monitoring, and GitOps-based delivery.



\### Application Details



| Property | Value |

|---|---|

| Application | GitOps Kubernetes Platform |

| Version | v1.1.0 |

| Environment | Kubernetes |

| Status | Healthy |

| Container Port | 5000 |



\### API Endpoints



| Endpoint | Description |

|---|---|

| `/` | Application homepage |

| `/health` | Application health check |

| `/api/info` | Application information |



\### Health Check Response



```json

{

&#x20; "status": "healthy"

}

```



\### Application Information Response



```json

{

&#x20; "application": "GitOps Kubernetes Platform",

&#x20; "version": "v1.1.0",

&#x20; "environment": "Kubernetes",

&#x20; "status": "healthy"

}

```



\---



\# 🐳 Docker



The Flask application is packaged as a Docker image.



\### Docker Repository



```text

narinder15/gitops-kubernetes-platform

```



The CI pipeline publishes images using:



\- `latest`

\- Git commit SHA



Example:



```text

narinder15/gitops-kubernetes-platform:<commit-sha>

```



Using a Git commit SHA makes each deployment traceable to the exact source code version that produced the image.



\### Local Docker Build



```powershell

docker build -t narinder15/gitops-kubernetes-platform:v1.1.0 ./app

```



\### Push Docker Image



```powershell

docker push narinder15/gitops-kubernetes-platform:v1.1.0

```



\---



\# ☸️ Kubernetes



The application is deployed to a local Kubernetes cluster running on \*\*Minikube\*\*.



\### Namespace



```text

gitops-platform

```



\### Deployment



```text

gitops-platform

```



The deployment uses:



\- 2 replicas

\- RollingUpdate strategy

\- Readiness probe

\- Liveness probe

\- CPU requests and limits

\- Memory requests and limits

\- `imagePullPolicy: Always`



\### Container Port



```text

5000

```



\### Service



| Property | Value |

|---|---|

| Service Name | `gitops-platform-service` |

| Type | `NodePort` |

| Port | `80` |

| NodePort | `30080` |



\### Kubernetes Deployment Strategy



```yaml

strategy:

&#x20; type: RollingUpdate

&#x20; rollingUpdate:

&#x20;   maxUnavailable: 0

&#x20;   maxSurge: 1

```



This allows Kubernetes to update application pods gradually while maintaining availability.



\---



\# 🔄 GitHub Actions CI



The Continuous Integration workflow is located at:



```text

.github/workflows/build-and-push.yml

```



The workflow is triggered when changes are pushed to the `main` branch affecting:



```text

app/\*\*

k8s/\*\*

.github/workflows/\*\*

```



\### CI Pipeline



```text

Git Push

&#x20;   ↓

Checkout Repository

&#x20;   ↓

Setup Docker Buildx

&#x20;   ↓

Docker Hub Authentication

&#x20;   ↓

Build Docker Image

&#x20;   ↓

Push Docker Image

&#x20;   ↓

Update Kubernetes Manifest

&#x20;   ↓

Commit Updated Manifest

&#x20;   ↓

Push Changes to GitHub

```



\---



\# 🔐 GitHub Actions Secrets



Docker Hub authentication is handled securely through GitHub repository secrets.



Required secrets:



```text

DOCKERHUB\_USERNAME

DOCKERHUB\_TOKEN

```



The credentials are not hard-coded into the workflow or application source code.



\---



\# 🔁 Automated Kubernetes Manifest Update



After successfully building and pushing the Docker image, GitHub Actions automatically updates:



```text

k8s/deployment.yaml

```



The workflow replaces the existing Docker image tag with the Git commit SHA.



Example:



```yaml

image: narinder15/gitops-kubernetes-platform:<commit-sha>

```



GitHub Actions then creates a commit such as:



```text

Update image to <commit-sha>

```



and pushes the updated Kubernetes manifest back to GitHub.



This creates the bridge between \*\*Continuous Integration\*\* and \*\*GitOps Continuous Delivery\*\*.



\---



\# 🔱 ArgoCD



ArgoCD provides the Continuous Delivery layer of the project.



\### ArgoCD Application



```text

gitops-kubernetes-platform

```



\### Git Repository



```text

https://github.com/Narinder-code17/gitops-kubernetes-platform.git

```



\### Manifest Path



```text

k8s/

```



\### Kubernetes Namespace



```text

gitops-platform

```



\### Sync Policy



The ArgoCD application uses:



```text

Automated Sync

Prune

Self Heal

CreateNamespace=true

```



ArgoCD continuously compares the desired state stored in Git with the actual state of the Kubernetes cluster.



When the Git repository changes, ArgoCD automatically synchronizes the Kubernetes resources.



\---



\# 🔄 Complete CI/CD + GitOps Workflow



```text

1\. Developer modifies application

&#x20;             │

&#x20;             ▼

2\. Developer pushes code to GitHub

&#x20;             │

&#x20;             ▼

3\. GitHub Actions starts

&#x20;             │

&#x20;             ▼

4\. Docker image is built

&#x20;             │

&#x20;             ▼

5\. Docker image is pushed to Docker Hub

&#x20;             │

&#x20;             ▼

6\. Kubernetes deployment manifest is updated

&#x20;             │

&#x20;             ▼

7\. GitHub Actions commits the updated manifest

&#x20;             │

&#x20;             ▼

8\. Updated manifest is pushed to GitHub

&#x20;             │

&#x20;             ▼

9\. ArgoCD detects the Git change

&#x20;             │

&#x20;             ▼

10\. ArgoCD automatically synchronizes Kubernetes

&#x20;             │

&#x20;             ▼

11\. Kubernetes performs a rolling update

&#x20;             │

&#x20;             ▼

12\. New application pods become healthy

```



\---



\# 🧪 Verification



\## Check Kubernetes Pods



```powershell

kubectl get pods -n gitops-platform

```



Expected:



```text

2/2 pods Running

```



\## Check Deployment



```powershell

kubectl get deployment gitops-platform -n gitops-platform

```



\## Check Service



```powershell

kubectl get service -n gitops-platform

```



\## Check Current Docker Image



```powershell

kubectl get deployment gitops-platform -n gitops-platform -o jsonpath="{.spec.template.spec.containers\[0].image}"

```



\## Check ArgoCD Application



```powershell

kubectl get application gitops-kubernetes-platform -n argocd

```



Expected:



```text

NAME                         SYNC STATUS   HEALTH STATUS

gitops-kubernetes-platform   Synced        Healthy

```



\## Check Rollout



```powershell

kubectl rollout status deployment/gitops-platform -n gitops-platform

```



Expected:



```text

deployment "gitops-platform" successfully rolled out

```



\---



\# 🌐 Access the Application



Use Minikube to expose the Kubernetes service:



```powershell

minikube service gitops-platform-service -n gitops-platform

```



The service opens the Flask application in the default browser.



\### Available Endpoints



```text

/

```



```text

/health

```



```text

/api/info

```



\---



\# ❤️ Health Monitoring



The application exposes a `/health` endpoint that is used by Kubernetes for health monitoring.



\### Readiness Probe



The readiness probe checks:



```text

/health

```



This ensures that Kubernetes sends traffic only to containers that are ready to serve requests.



\### Liveness Probe



The liveness probe also checks:



```text

/health

```



If the application becomes unhealthy, Kubernetes can restart the affected container.



\---



\# 🔄 Rolling Update



The Kubernetes deployment uses:



```yaml

strategy:

&#x20; type: RollingUpdate

```



with:



```yaml

rollingUpdate:

&#x20; maxUnavailable: 0

&#x20; maxSurge: 1

```



This allows the application to transition from the old version to the new version without intentionally reducing the number of available replicas.



\---



\# 📊 Final Deployment Verification



The final deployment was successfully verified with:



```text

ArgoCD Sync Status : Synced

ArgoCD Health      : Healthy

Deployment         : 2/2 Ready

Pods               : 2/2 Running

Docker Image       : Git SHA tagged

```



The final GitOps deployment demonstrated that a Docker image produced by GitHub Actions was automatically propagated through Git to ArgoCD and then deployed to Kubernetes.



\---



\# 📸 Project Evidence



The project contains screenshots documenting the implementation and verification process, including:



\- Kubernetes cluster setup

\- Kubernetes namespace

\- Kubernetes deployment

\- Kubernetes service

\- Running application

\- Docker image creation

\- Docker Hub image push

\- ArgoCD installation

\- ArgoCD application configuration

\- ArgoCD synchronization

\- GitHub Actions workflow

\- Successful Docker CI pipeline

\- Automated Kubernetes image update

\- Automated Git commit and push

\- ArgoCD automatic deployment

\- Final healthy Kubernetes pods



\---



\# 🎓 DevOps Concepts Demonstrated



This project provides hands-on implementation of:



\- Git

\- GitHub

\- GitHub Actions

\- Continuous Integration

\- Continuous Delivery

\- GitOps

\- Docker

\- Docker Hub

\- Containerization

\- Kubernetes

\- Kubernetes Deployments

\- Kubernetes Services

\- Kubernetes Namespaces

\- Minikube

\- kubectl

\- ArgoCD

\- Automated Synchronization

\- Rolling Updates

\- Readiness Probes

\- Liveness Probes

\- Immutable Docker Image Tags

\- Configuration as Code

\- Self-Healing GitOps concepts



\---



\# 🔐 Security Considerations



The project follows basic CI/CD security practices:



\- Docker Hub credentials are stored as GitHub repository secrets.

\- Credentials are not stored in source code.

\- Docker images are tagged using Git commit SHA values.

\- Kubernetes configuration is version-controlled.

\- ArgoCD deploys only the desired state stored in Git.



For a production environment, additional security controls should be implemented, including:



\- Container vulnerability scanning

\- Kubernetes RBAC hardening

\- Network policies

\- Kubernetes Secrets management

\- TLS/HTTPS

\- Image signing and verification

\- Security policy enforcement



\---



\# 🚀 Future Enhancements



Possible future improvements include:



\- Automated unit and integration testing

\- Docker image vulnerability scanning

\- Kubernetes security scanning

\- Prometheus monitoring

\- Grafana dashboards

\- Centralized logging

\- Kubernetes Ingress

\- TLS/HTTPS

\- Helm charts

\- Separate development and production environments

\- External secrets management

\- Deployment notifications

\- Automated rollback

\- Cloud Kubernetes deployment using Amazon EKS, Azure AKS, or Google GKE



\---



\# 📌 Key Project Highlights



\### Continuous Integration



GitHub Actions automatically builds and publishes Docker images.



\### GitOps



Git acts as the single source of truth for the desired Kubernetes configuration.



\### Continuous Delivery



ArgoCD automatically synchronizes changes from Git to Kubernetes.



\### Automated Image Updates



GitHub Actions automatically updates the Kubernetes deployment with the newly built image.



\### Traceable Deployments



Docker images use Git commit SHA tags, allowing each deployment to be traced back to a specific source commit.



\### Kubernetes Reliability



The deployment uses multiple replicas, rolling updates, readiness probes, and liveness probes.



\---



\# 🏁 Conclusion



The \*\*GitOps Kubernetes Platform\*\* demonstrates a complete automated DevOps and GitOps deployment lifecycle.



The project separates Continuous Integration and Continuous Delivery:



```text

GitHub Actions

&#x20;     │

&#x20;     ├── Build Docker Image

&#x20;     └── Push Docker Image

&#x20;             │

&#x20;             ▼

&#x20;       Update Git Manifest

&#x20;             │

&#x20;             ▼

&#x20;           ArgoCD

&#x20;             │

&#x20;             └── Deploy \& Synchronize

&#x20;                     │

&#x20;                     ▼

&#x20;                 Kubernetes

&#x20;                     │

&#x20;                     ▼

&#x20;             Healthy Application

```



The implementation provides a repeatable, version-controlled, and automated approach to deploying containerized applications on Kubernetes.



\---



\## 👨‍💻 Project



\*\*GitOps Kubernetes Platform\*\*



\*\*Technologies:\*\* Python • Flask • Docker • Docker Hub • Kubernetes • Minikube • kubectl • GitHub • GitHub Actions • ArgoCD • Git



\*\*Repository:\*\* `Narinder-code17/gitops-kubernetes-platform`

