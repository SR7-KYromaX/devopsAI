pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[credentialsId: '50a34337-6574-4fc1-a969-c848f3a5566e', url: 'https://github.com/SR7-KYromaX/devopsAI.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: '50a34337-6574-4fc1-a969-c848f3a5566e', url: 'https://github.com/SR7-KYromaX/devopsAI.git'
                bat 'python sort.py'
                
            }
        }
        stage('Test') {
            steps {
                echo "Testing is done"
            }
        }
    }
}
