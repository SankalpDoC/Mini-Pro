pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'poetry init --no-interaction'
                sh 'tox'
            }
        }

        stage('Create Executable') {
            steps {
                sh 'pyinstaller --onefile calculator.py'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'dist/*', allowEmptyArchive: true
        }
    }
}
