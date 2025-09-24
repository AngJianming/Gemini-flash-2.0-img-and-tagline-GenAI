# Gemini-flash-2.0-img-and-tagline-GenAI

You need to configure the following secrets in your GitHub repository:

1. PROJECT_ID: Your Google Cloud project ID.
1. REGION: Your GKE zone (e.g., us-central1-c).To set secrets, go to your repository settings > Secrets and variables > Actions.

## Enable Google Cloud APIs

- Ensure the following APIs are enabled:

- Artifact Registry (artifactregistry.googleapis.com)

- Google Kubernetes Engine (container.googleapis.com)

- IAM Credentials API (iamcredentials.googleapis.com)