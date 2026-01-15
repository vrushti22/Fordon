pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/vrushti22/Fordon.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fordon-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f fordon || true
                docker run -d --name fordon -p 5000:5000 fordon-app
                '''
            }
        }
    }
}
