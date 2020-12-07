pipeline {
    agent any

    environment {
        ENV_FILE = '/opt/env/dataverse_dv03.env'
    }

    stages {
        stage('Setup') {
            steps {
                sh '''
                    python3 -V
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements-dev.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    ./venv/bin/python -m pytest -v --junit-xml=report.xml --html=report.html
                '''
            }

            publishHTML target : [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportFiles: 'report.html',
                reportName: 'Test Report'
            ]
        }

        stage('Cleanup') {
            steps {
                sh 'rm -rf venv'
            }
        }
    }
}
