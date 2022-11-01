pipeline {
    agent { dockerfile {
        filename 'Dockerfile'
        }
    }

    stages {
        stage('linker and test') {
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