pipeline {
    agent any 
    stages {
        stage('Lint') { 
            steps {
                sh 'docker compose run --rm app sh -c "flake8"' 
            }
        }
        stage('Test') { 
            steps {
                sh 'docker compose run --rm app sh -c "python manage.py waitdb && python manage.py test"'
            }
        }
        stage('Deploy') { 
            steps {
                // 
            }
        }
    }
}