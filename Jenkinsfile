pipeline {
    agent any

    environment {
        IMAGE_NAME = 'fordon-app'
        CONTAINER_NAME = 'fordon'
    }

    stages {

        stage('Checkout Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/vrushti22/Fordon.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Remove old container if exists
                    sh "docker rm -f ${CONTAINER_NAME} || true"
                    // Run container
                    sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}"
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
        success {
            echo "Docker container is running!"
        }
        failure {
            echo "Something went wrong, check Jenkins logs"
        }
    }
}
