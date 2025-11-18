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
    environment{
        VENV_DIR='venv'
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

                // git branch: 'main',
                //     url: 'https://github.com/babuann/Churn_Prediction.git',
                //     credentialsId: 'github-token'
            }
        }
    }
}