#!/usr/bin/env groovy

pipeline {
    agent any

    parameters {
        string(name: 'VERSION', defaultValue: '', description: 'Full version string for this.')
        string(name: 'YUKON_TYPE', defaultValue: '', description: 'Bronze or Copper')
    }


    stages {
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