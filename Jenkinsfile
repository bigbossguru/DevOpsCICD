pipeline {
    agent any

    stages {
        stage('Clean all dependencies') {
            steps {
                sh 'docker kill $(docker ps -q)'
                sh 'docker system prune -fa'
                sh 'docker system prune -fa --volumes'
            }
        }
        stage('Check active containers') {
            steps {
                sh 'docker ps'
            }
        }
        stage('Build docker compose file and run project') {
            steps {
                sh 'docker compose up -d --build'
            }
        }
        stage('Show all active containers') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
