def testApp() {
    echo "Testing the application..."
    directory1 = pwd()
    echo "Direct is ${directory1}"

    File myFile = new File("test")
    println myFile.text
}

return this