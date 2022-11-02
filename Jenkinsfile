pipeline {
    environment {
        registryCredential = 'docker-hub'
        imageName = 'lolkek/fast-api'
    }
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
                 dockerImage = docker.build imageName
                }
            }
            }
        stage('Deploy Image') {
            steps{
                script
                {
                     withCredentials([usernameColonPassword(credentialsId: '123', variable: 'USERPASS')]) {
                        sh """
                            set +x
                            docker login -u lolkek31415 -p ${USERPASS}
                        """
                        dockerImage.push()
                     dockerImage.push('latest')
                    }
//                   docker.withRegistry( '', registryCredential)
//                   {
//                      dockerImage.push()
//                      dockerImage.push('latest')
//                   }
                }
            }
        }
    }
}