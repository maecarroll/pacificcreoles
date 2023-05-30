import xml.etree.ElementTree as ET


def elan2str(elanfile, tierid):
    """Extract texts from Elan file returns string
    
    Elanfile = elanfile
    tierid = TIER_ID of the elan file you wish to extract. Assume a
    minimal elan templte. Wont always work.
    """
    output = str()
    tree = ET.parse(elanfile)
    root = tree.getroot()
    for x in root.findall('.//*[@TIER_ID= "%s"]/*/*/ANNOTATION_VALUE' % tierid):
        try:
            output = output + x.text + '. ' 
        except:
            pass
    return(output)