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

            post {
                success {
                    archiveArtifacts artifacts: 'dist/*', allowEmptyArchive: true
                }
            }
        }

        stage('Containerize') {
            
            steps {
                script {
                    sh 'docker build -t incogdark/scientific-calculator:latest .'
                }
            }
        }

        stage('Pushing Container to Hub') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'dockhub-creds', variable: 'dockhub-creds')]) {
                        sh 'docker -t login -u incogdark ${dockhub-creds}'
                    }
                    sh 'docker push incogdark/scientific-calculator'
                }
            }
        }
    }

    
    
}
