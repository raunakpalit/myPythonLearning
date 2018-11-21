import shelve

with shelve.open("bike") as bike:
    import pdb
    pdb.set_trace()
    '''
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engin_size"] = 250
    # for key in bike:
    #     print(key)
    
    # print('=' * 40)

    print(bike["engine_size"])
    # print(bike["engin_size"])
    print(bike["colour"])
    '''

