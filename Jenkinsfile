#!/usr/bin/env groovy

def gv

pipeline {
    agent any
    }


    stages {
        stage("Build") {
            steps {
                script {
                    bat "python testme.py"
                    bat "python primary/FirstProgram.py"
                    bat "python primary/bracket_validation.py"
                }
            }
        }
    }
}
