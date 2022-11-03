pipeline {
    environment {
        imageName = 'lolkek31415/fast-api'
    }
    agent any
    stages
    {
        stage('linker and test')
        {
            agent
            {
                dockerfile
                    {
                    filename 'Dockerfile'
                    }
                }
                steps
                {
//                     sh 'flake8 --statistics .'
//                     sh 'black --check .'
                    echo 'tests'
                    sh 'python -m pytest'
                }
            }

                stage('Build_2')
                {
                    steps
                    {
                        sh 'docker build -t $imageName .'
                    }
                }

                stage('Login')
                {
                    steps
                    {
                        script
                        {
                            docker.withRegistry( '', '123')
                            {
                                withCredentials([usernamePassword(credentialsId: '123', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')])
                                {
                                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin docker.io'
                                    sh 'docker tag $imageName $imageName'
                                    sh 'docker push $imageName'

                                }
                            }
                        }
                    }
                }
//         stage('Deploy to Kubernetes Cluster')
//         {
//             steps
//             {
//             ///CREATE AND APPLY THE PATCH. REMEMBER TO LOGIN ON THE CLUSTER. (-s $CLUSTER_URL --token $TOKEN_CLUSTER --insecure-skip-tls-verify)
//             sh  '''
//
//             PATCH_TO_DEPLOY={\\"metadata\\":{\\"labels\\":{\\"version\\":\\"${env.BUILD_ID}\\"}},\\"spec\\":{\\"template\\":{\\"metadata\\":{\\"labels\\":{\\"version\\":\\"${env.BUILD_ID}\\"}},\\"spec\\":{\\"containers\\":[{\\"name\\":\\"$NAME_DEPLOY\\",\\"image\\":\\"my-image:${env.BUILD_ID}\\"}]}}}}
//
//             kubectl patch deployment $NAME_DEPLOY  -n $NAMESPACE -p $PATCH_TO_DEPLOY \
//             -s $CLUSTER_URL --token $TOKEN_CLUSTER --insecure-skip-tls-verify
//
//             '''
//
//             }
//         }
    }
    post
    {
        always
        {
            sh 'docker logout'
        }
    }
}
