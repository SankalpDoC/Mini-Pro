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

        post {
            success {
                archiveArtifacts artifacts: 'dist/*', allowEmptyArchive: true
            }
        }

        stage('Containerize') {
            environment {
                DOCKER_HUB_CREDENTIALS = credentials('docker-hub')
                IMAGE_NAME = 'my-calculator'
                IMAGE_TAG = sh(script: 'echo $BUILD_ID', returnStdout: true).trim()
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
                        def app = docker.build("${IMAGE_NAME}:${IMAGE_TAG}", '.')
                        app.push()
                    }
                }
            }
        }
    }

    
    
}
