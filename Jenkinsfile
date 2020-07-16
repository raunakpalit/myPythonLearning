#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage('Setting up selenium') {
            steps {
                sh "docker run -d -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug"
            }
        }
        stage("build") {
            steps {
                echo "Building the application..."
            }
        }
        stage("test") {
            steps {
                echo "Testing the application..."
            }
        }
        stage("deploy") {
            steps {
                echo "Deploying the application..."
            }
        }
    }
}