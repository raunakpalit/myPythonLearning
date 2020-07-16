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
                script {
                    checkout changelog: false,
                    poll: false,
                    scm: [$class: 'GitSCM',
                          branches: [[name: "master"]],
                          doGenerateSubmoduleConfigurations: false,
                          extensions: [[$class: 'SparseCheckoutPaths',
                          sparseCheckoutPaths: [[path: 'test.py']]]],
                          submoduleCfg: [],
                          userRemoteConfigs: [
                             [credentialsId: '51b67fe3-c792-4d4a-8999-866c4b9fb73e',
                              url: 'https://github.com/raunakpalit/RestAPI_Flask.git']]
                          ]
                }
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