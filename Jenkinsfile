pipeline {
    agent any

    tools {
    'jenkins.plugins.shiningpanda.tools.PythonInstallation' 'Python3'
<<<<<<< HEAD
}
=======
    }
>>>>>>> 71ddc8f (Fix Jenkinsfile tool block)

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
