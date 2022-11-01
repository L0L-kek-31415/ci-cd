pipeline {
    agent any
    stages {
        stage('linker and test') {
            agent { dockerfile {
                filename 'Dockerfile'
                }
            }
            steps {
                echo 'Start'
                sh 'flake8 .'
                sh 'black .'
                echo 'tests'
                sh 'python -m pytest'
                echo 'Finish'
            }
        }
        stage('Build') {
            steps {
                script{
                 app = docker.build 'Dockerfile'
                }
            }
        }
    }
}