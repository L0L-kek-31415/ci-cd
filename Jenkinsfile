pipeline {
    environment {
        registryCredential = 'docker-hub'
        imageName = 'lolkek/fast-api'
        DOCKERHUB_CREDENTIALS=credentials('docker-hub')

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
//         stage('Deploy Image') {
//             steps{
//                 script
//                 {
//                         withCredentials([usernamePassword(credentialsId: '123', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
//                         sh """
//                             set +x
//                             docker login -u ${USERNAME} --password-stdin ${PASSWORD}
//                         """
//                         dockerImage.push()
//                         dockerImage.push('latest')
//                     }


//                   docker.withRegistry( '', '123')
//                   {
//                      dockerImage.push()
//                      dockerImage.push('latest')
//                   }

                stage('Build') {

                    steps {
                        sh 'docker build -t {imageName}:latest .'
                    }
                }

                stage('Login') {

                    steps {
                        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    }
                }

                stage('Push') {

                    steps {
                        sh 'docker push {imageName}:latest'
                    }
                }


    }
    post {
		always {
			sh 'docker logout'
		}
	}
}