// pipeline{
//     agent any

//     stages{
//         stage('Cloning Github repo to Jenkins'){
//         steps{
//             script{
//                 echo 'Cloning Github repo to Jenkins..........'
//                 checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/babuann/Churn_Prediction.git']])
//             }
//         }
//     }
// }

pipeline {
    agent any
    environment {
        VENV_DIR='venv'
        GCP_PROJECT="cool-freehold-475210-c0"
        GCLOUD_PATH="/var/jenkins_home/google-cloud-sdk/bin"}

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

                // git branch: 'main',
                //     url: 'https://github.com/babuann/Churn_Prediction.git',
                //     credentialsId: 'github-token'
            }
        }
        stage('Building and Pusing Docker Image to GCR') {
            steps {
                withCredentials([file(credentialsId:'gcp-key',variable : 'GOOGLE_APPLICATION_CREDENTIALS')])
                {
                    script{
                        echo 'Building and Pushing DOcker Image to GCR ......'
                        sh '''
                            export PATH=$PATH:$(GCLOUD_PATH)
                        
                            gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                            gcloud config set project ${GCP_PROJREct}
                            gcloud auth configure-docker --quiet

                            docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .
                            docker push gcr.io/${GCP_PROJECT}/ml-project:latest 
                        '''
                    }
                }
               

                // git branch: 'main',
                //     url: 'https://github.com/babuann/Churn_Prediction.git',
                //     credentialsId: 'github-token'
            }
        }
    }
}