pipeline {
    agent any
    environment {
        VENV_DIR   = 'venv'
        GCP_PROJECT = "cool-freehold-475210-c0"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
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
                    script {
                        echo 'Building and Pushing Docker Image to GCR ......'
                        sh """
                                echo 'Building and Pushing Docker Image to GCR ......'

                        
                                echo "Adding gcloud to PATH"
                                export PATH="/usr/lib/google-cloud-sdk/bin:\$PATH"

                                echo "Checking gcloud version..."
                                which gcloud
                                gcloud --version

                                echo "Authenticating to GCP..."
                                gcloud auth activate-service-account --key-file="\${GOOGLE_APPLICATION_CREDENTIALS}"

                                echo "Setting GCP project..."
                                gcloud config set project "${GCP_PROJECT}"

                                echo "Configuring Docker authentication..."
                                gcloud auth configure-docker --quiet

                                echo "Building Docker image..."
                                docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                                echo "Pushing Docker image..."
                                docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                """
                    }
                }
            }
        stage('Deploy to Google Cloud Run') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Deploy to Google Cloud Run......'
                        sh """
                                echo 'Deploy to Google Cloud Run......'

                        
                                echo "Adding gcloud to PATH"
                                export PATH="/usr/lib/google-cloud-sdk/bin:\$PATH"

                                echo "Checking gcloud version..."
                                which gcloud
                                gcloud --version

                                echo "Authenticating to GCP..."
                                gcloud auth activate-service-account --key-file="\${GOOGLE_APPLICATION_CREDENTIALS}"

                                echo "Setting GCP project..."
                                gcloud config set project "${GCP_PROJECT}"

                                gcloud run deploy ml-project \
                                    -- image=gcr.io/${GCP_PROJECT}/ml-project:latest \
                                    -- platform=managed \
                                    -- region=us-central1 \
                                    -- allow=unauthenticated 
                """
                    }
                }
            }
        }
    }
}
