pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('=== Build Docker Image ===') {
            steps {
                sh '''
                docker build -t gohel-tailors:latest .
                '''
            }
        }

        stage("Login to Docker Hub"){
            steps{
                withCredentials([usernamePassword(credentialsId:'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]){

                sh'''
                echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                '''
                }
            }
        }
         

        stage('==== Tag and Push Image ====') {
            steps {
                sh '''
                docker tag gohel-tailors:latest prashantgohel321/gohel-tailors
                docker push prashantgohel321/gohel-tailors:latest
                '''
            }
        }

        stage("Deploy to ECS"){
            steps{
                sh '''
                    aws ecs update-service \
                        --cluster gohel-tailors-cluster2 \
                        --service gohel-tailors-task-service \
                        --force-new-deployment \
                        --region ap-south-1
                '''
            }
        }

        // stage('Build Check') {
        //     steps {
        //         sh '''
        //         echo "Checking flask app...."
        //         python3 -m py_compile app.py
        //         '''
        //     }
        // }
    }

    post {
        success {
            echo "****** IMAGE PUSHED SUCCESSFULL ******"
        }
        failure {
            echo "****** PIPELINE failed ******"
        }
    }
}
