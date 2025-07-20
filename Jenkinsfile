pipeline {
    agent any

    tools {
        python 'Python3' // Must match your Jenkins Python tool name
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/16singhrhohan/hotel-booking-automation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --html=reports/report.html --self-contained-html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Test Report'
                ])
            }
        }
    }
}