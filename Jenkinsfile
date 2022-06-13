pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Deploy') {
            steps {
                echo 'docker-compose --version'
            }
        }
    }
}
