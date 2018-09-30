pipeline {
  agent any
  
  environment {
    FORM8_TAG = "$BRANCH_NAME-$BUILD_ID"
    FORM8_ENVIRONMENT = "$BRANCH_NAME"
    FORM8_ENV_TYPE = "dev"
  }

  stages {
    stage('Build') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'gcr', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh 'docker login -u $USER -p "$PASS" https://gcr.io && f8 build --push'
        }
      }
    }
    stage('Deploy') {
      steps {
        sh 'f8 deploy'
      }
    }
    stage('Test') {
      steps {
        sh 'f8 test'
      }
    }
  }
}
