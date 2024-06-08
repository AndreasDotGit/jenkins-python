pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        python3 --version
      }
    }
    stage('hello') {
      steps {
        python3 hello.py
      }
    }
  }
}