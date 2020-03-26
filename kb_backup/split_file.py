lines_per_file = 1000
smallfile = None
with open('01.31.2020.e8cbc9b9-dc8a-4768-958d-89835896b2a6-KB.tsv') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'small_file_{}.tsv'.format(
                lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()
