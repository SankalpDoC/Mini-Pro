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
                sh 'pytest -v TestSciCal.py'
            }
        }

        stage('Create Executable') {
            steps {
                sh 'pyinstaller --onefile --name=SciCalculator SciCal.py'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'dist/*', allowEmptyArchive: true
        }
    }
}
