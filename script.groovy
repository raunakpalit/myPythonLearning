def testApp() {
    echo "Testing the application..."
    workspace = pwd()
    echo "Workspace: ${workspace}"
    def exists = fileExists 'test.py'
    if (exists) {
        echo 'Yes'
            }
    else {
        echo 'No'
    }

    def data = readFile(file: 'test.py')
    println(data)
}

return this