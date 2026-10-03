pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                bat 'py -3 -m venv venv'
                bat 'venv\\Scripts\\python -m pip install --upgrade pip'
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
                bat 'venv\\Scripts\\python -m playwright install chromium'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\python -m pytest --junitxml=reports\\junit.xml'
            }
        }
    }
}