### 1. Write App (TensorFlow)
- The code to build, train, and save the model in Google Cloud Storage Bucket.
- Entrypoint of the Dockerfile triggers the trainer.py python script

### 2. Setup Google Cloud 
- Create new project
- Enable Vertex AI APIs
- Create Vertex AI User Managed Notebook with youe preferred configuration
- Activate Cloud Run API and Cloud Build API

### 3. Install and init Google Cloud SDK
- https://cloud.google.com/sdk/docs/install

### 4. Dockerfile, requirements.txt, .dockerignore
- https://cloud.google.com/run/docs/quickstarts/build-and-deploy#containerizing

### 5. Cloud build & deploy
```
gcloud builds submit --tag gcr.io/<project_id>/<function_name>
```
Setup new Cloud Run application and deploy the container

### 6. Training
- Setup Custom Model training job on Vertex AI

### Code Lab Session
- [Follow the Code Lab](https://codelabs.developers.google.com/vertex_custom_training_prediction#0)