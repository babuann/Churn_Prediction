pipeline {
    agent any

    environment {
        VENV_DIR     = 'venv'
        GCP_PROJECT  = "cool-freehold-475210-c0"
        GCLOUD_PATH  = "/usr/lib/google-cloud-sdk/bin"
        GCP_REGION   = "us-central1"
        SERVICE_NAME = "ml-project"
    }

    stages {

        stage('Cloning Github repo to Jenkins') {
            steps {
                echo 'Cloning Github repo to Jenkins..........'

                git branch: 'main',
                    url: 'https://github.com/babuann/Churn_Prediction.git',
                    credentialsId: 'github-token'
            }
        }

        stage('Setting up our venv and installing dependencies') {
            steps {
                echo 'Setting up our venv and installing dependenciess..........'
                sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                '''
            }
        }

        stage('Building and Pusing Docker Image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                        echo "Building and Pushing Docker Image to GCR ......"

                        echo "Adding gcloud to PATH"
                        export PATH="'${GCLOUD_PATH}'":$PATH

                        echo "Checking gcloud version..."
                        which gcloud
                        gcloud --version

                        echo "Authenticating to GCP..."
                        gcloud auth activate-service-account --key-file="$GOOGLE_APPLICATION_CREDENTIALS"

                        echo "Setting GCP project..."
                        gcloud config set project "$GCP_PROJECT"

                        echo "Configuring Docker authentication..."
                        gcloud auth configure-docker --quiet

                        echo "Building Docker image..."
                        docker build -t "gcr.io/$GCP_PROJECT/$SERVICE_NAME:latest" .

                        echo "Pushing Docker image..."
                        docker push "gcr.io/$GCP_PROJECT/$SERVICE_NAME:latest"
                    '''
                }
            }
        }

        stage('Deploy to Google Cloud Run') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                        echo "Deploying to Google Cloud Run......"

                        echo "Adding gcloud to PATH"
                        export PATH="'${GCLOUD_PATH}'":$PATH

                        echo "Checking gcloud version..."
                        which gcloud
                        gcloud --version

                        echo "Authenticating to GCP..."
                        gcloud auth activate-service-account --key-file="$GOOGLE_APPLICATION_CREDENTIALS"

                        echo "Setting GCP project..."
                        gcloud config set project "$GCP_PROJECT"

                        echo "Deploying to Cloud Run..."
                        gcloud run deploy "$SERVICE_NAME" \
                            --image="gcr.io/$GCP_PROJECT/$SERVICE_NAME:latest" \
                            --platform=managed \
                            --region="$GCP_REGION" \
                            --allow-unauthenticated \
                            --port=5000
                    '''
                }
            }
        }
    }
}
