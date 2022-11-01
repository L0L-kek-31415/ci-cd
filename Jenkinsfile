pipeline {
    agent { dockerfile true }

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