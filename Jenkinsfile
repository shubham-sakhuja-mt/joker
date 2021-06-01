pipeline {
  agent any
  
  environment {
    COMMIT_HASH = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
    F8_TAG = "$BRANCH_NAME-$BUILD_ID-$COMMIT_HASH"
    F8_ENVIRONMENT = "$BRANCH_NAME"
    F8_ENV_TYPE = "dev"
  }

  stages {
    stage('Build') {
      steps {
        withDockerRegistry([url: 'https://971963691537.dkr.ecr.us-east-1.amazonaws.com', credentialsId: 'ecr:us-east-1:aws-creds']) {
          sh 'f8 build --push'
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
