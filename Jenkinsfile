#!/usr/bin/env groovy

def gv

pipeline {
    agent any


    stages {
        stage("Build") {
            steps {
                script {
                    bat "python testme.py"
                    bat "python primary/FirstProgram.py"
                    bat "python primary/bracket_validation.py"
                    bat "python primary/dictionary_map.py"
                    bat "python primary/factorial.py"
                    bat "python primary/fibonacci_series.py"
                    bat "python primary/palindrome.py"
                    bat "python primary/prime_numbers.py"
                    bat "python primary/remove_char_string.py"
                    bat "python primary/reverse_integer_string.py"
                    bat "python primary/sum_digits.py"
                }
            }
        }
    }
}
