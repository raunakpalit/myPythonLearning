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
                          sparseCheckoutPaths: [[path: 'resources/store.py']]]],
                          submoduleCfg: [],
                          userRemoteConfigs: [
                             [credentialsId: 'Lieutenant@1',
                              url: 'https://github.com/raunakpalit/stores-rest-api']]
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