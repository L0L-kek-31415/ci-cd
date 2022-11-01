pipline {
    stages{
        stage("linker and test") {
            agent{
                dockerfile true
                }
            steps {
                sh 'black .'
                sh 'flake8 .'
                sh 'pytest'
                }
            }
        }
    }