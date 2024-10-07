pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                script {
                    try {
                        checkout scm
                    } catch (Exception e) {
                        error("Checkout failed: ${e.message}")
                    }
                }
            }
        }
        stage('Setup Python Virtual ENV for dependencies') {
            steps {
                sh 'chmod +x venvsetup.sh'
                sh './venvsetup.sh'
            }
        }
        stage('Setup Gunicorn Setup') {
            steps {
                sh 'chmod +x gunicorn.sh'
                sh './gunicorn.sh'
            }
        }
        stage('Setup NGINX') {
            steps {
                sh 'chmod +x nginx.sh'
                sh './nginx.sh'
            }
        }
    }

    post {
        failure {
            // Notify or log the failure
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}
