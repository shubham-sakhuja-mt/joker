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
        withDockerRegistry([url: 'https://gcr.io', credentialsId: 'gcr']) {
          sh 'echo "<span style=\\"color:green\\">foobar</span>"'
          sh 'f8 build --push'
        }
      }
    }
    stage('Deploy') {
      parallel {
        stage('Update') {
          steps {
            sh 'f8 deploy'
          }
        }
        stage('Load Test') {
          steps {
            sh 'f8 test -i load'
          }
        }
      }
    }
    stage('Test') {
      steps {
        sh 'f8 test -i func'
      }
    }
  }
}
