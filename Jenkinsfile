pipeline{
    agent any
    stages {

        stage('Setup Python Virtual ENV for dependencies'){

      steps  {
            sh '''
            chmod +x venvsetup.sh
            ./venvsetup.sh
            '''}
        }
        stage('Setup Gunicorn Setup'){
            steps {
                sh '''
                chmod +x gunicorn.sh
                ./gunicorn.sh
                '''
            }
        }
        stage('setup NGINX'){
            steps {
                sh '''
                chmod +x nginx.sh
                ./nginx.sh
                '''
            }
        }
    }
}