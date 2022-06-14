pipeline {
    agent { dockerfile true }

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
        stage('build Postgres container') {
            steps {
                sh 'docker run -d --name my-postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres'
            }
        }
        stage('build pgAdmin4 container') {
            steps {
                sh 'docker run -d --name my-pgadmin -p 82:80 -e PGADMIN_DEFAULT_EMAIL=a@a.com -e PGADMIN_DEFAULT_PASSWORD=hello12345 -d dpage/pgadmin4'
            }
        }
        stage('Show all active containers') {
            steps {
                sh 'docker ps'
            }
        }
        stage('Build Django dockerfile project') {
            steps {
                sh 'docker build -t django-app-project .'
            }
        }
    }
}
