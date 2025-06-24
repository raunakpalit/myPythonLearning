def outerfunc(text):
    def innerfunc():
        print(text)

    return innerfunc()

outerfunc('Raunak Palit')