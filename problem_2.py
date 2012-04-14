def output(data, format="xml"):
    globals()["output_" + format](data)

def output_xml(data):
    print "Called output_xml with data"

def output_ascii(data):
    print "Called output_ascii with data"

def output_serializable(data):
    print "Called output_serializable with data"

output([1,2,3], format="xml")
output([1,2,3], format="ascii")
output([1,2,3], format="serializable")
