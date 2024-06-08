pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bash 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        bash 'python3 hello.py'
      }
    }
  }
}