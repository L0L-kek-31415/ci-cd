pipeline {
    agent { dockerfile {
        filename 'Dockerfile'
        }
    }

    stages {
        stage('linker and test') {
            steps {
                echo 'Start'
                sh 'black .'
                sh 'flake8 .'
                echo 'tests'
                sh 'pytest'
                echo 'Finish'
            }
        }
    }
}