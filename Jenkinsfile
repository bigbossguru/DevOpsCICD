pipeline {
    agent any

    stages {
        stage('Check active containers') {
            steps {
                sh 'docker ps'
            }
        }
        stage('Check lint in the source code') {
            steps {
                sh 'docker compose run --rm app sh -s "flake8"'
            }
        }
        stage('Make migrations database') {
            steps {
                sh 'docker compose run --rm app sh -c "python manage.py makemigrations && python manage.py migrate"'
            }
        }
        stage('Run simple Test case') {
            steps {
                sh 'docker compose run --rm app sh -c "python manage.py waitdb && python manage.py test"'
            }
        }
        stage('Clean all dependencies') {
            steps {
                sh 'docker kill $(docker ps -q)'
                sh 'docker system prune -fa'
                sh 'docker system prune -fa --volumes'
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
