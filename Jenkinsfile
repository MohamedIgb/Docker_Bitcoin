pipeline {

  agent any
  
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t flaskapp:$BUILD_NUMBER .'
      }
    }
     stage('Tag') {
        steps{
            sh 'docker tag flaskapp:$BUILD_NUMBER mohammedig/bitcoin:$BUILD_NUMBER'
        }
         
     }

    stage('Push container') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker', passwordVariable: 'pass', usernameVariable: 'username')]) {
                    sh 'docker login -u ${username} -p ${pass}'
                    sh 'docker push mohammedig/bitcoin:$BUILD_NUMBER'
                }
            }
        }
    }

    
}