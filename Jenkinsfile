pipeline {
    agent { dockerfile {
        filename 'Dockerfile'
        }
    }

    stages {
        stage('linker') {
            steps {
                echo 'Start'
                sh 'black .'
                echo 'Finish'
            }
        }
    }
}