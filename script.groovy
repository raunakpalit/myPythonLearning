def testApp() {
    echo "Testing the application..."
    directory1 = pwd()
    echo "Direct is ${directory1}"
    dh = new File('.')
    dh.eachFile {
        println(it)
    }

    File myFile = new File("test.py")
    println myFile.text
}

return this