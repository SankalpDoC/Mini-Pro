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
                    //sh 'docker build -t incogdark/scientific-calculator:latest .'
                    image = docker.build "incogdark/scientific-calculator:latest"
                }
            }
        }

        stage('Pushing Container to Hub') {
            steps {
                script {
                    /*withCredentials([usernamePassword(credentialsId: 'dock-creds', passwordVariable: 'Dock-Creds_P', usernameVariable: 'Dock-Creds')]) {
                        sh 'docker -t login -u incogdark ${dockhub-creds}'
                    }
                    sh 'docker push incogdark/scientific-calculator' */

                    docker.withRegistry('',"dock-creds") {
                        image.push()
                    }
                }
            }
        }

        stage('Deployment via Ansible') {
            steps {
                script {
                    
                    sh 'export LC_ALL=en_IN.UTF-8'
                    
                }
                //ansiblePlaybook becomeUser: null, colorized: true, disableHostKeyChecking: true, installation: 'Ansible', inventory: 'hosts', playbook: 'playbook.yml', sudoUser: null
                //ansiblePlaybook becomeUser: 'ansi_master', colorized: true, credentialsId: 'ssh-creds', disableHostKeyChecking: true, installation: 'ansible', inventory: 'hosts', playbook: 'playbook.yml'
                ansiblePlaybook becomeUser: 'ansi_master', colorized: true, credentialsId: 'ssh-creds', disableHostKeyChecking: true, installation: 'ansible', playbook: 'playbook.yml'
            
            }
        }    
    
    }
}