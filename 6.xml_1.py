from xml.dom import minidom

my_tree = minidom.parse('../../sample.xml')
data=open('../../sample.xml')
a=minidom.parse(data)
print(a)

#------------------------------------------------------
#data_1=minidom.parse_string('<myxml>Using<empty/>parseString</myxml>')
tagname=my_tree.getElementsByTagName('Instruments')[0]
print(tagname)
print(tagname.attributes['id'].value)
print(tagname.firstChild.data) #childNodes[0]
#-----------------------------------------------------
tagname_1=my_tree.getElementsByTagName('Portfolio')
print(tagname_1[1].firstChild.data)
print(len(tagname_1))
#------------------------------------------------------
for x in tagname_1:
    print(x.attributes['PortfolioId'].value)
#------------------------------------------------------------------

for x in tagname_1:
    print(x.firstChild.data,x.attributes['PortfolioId'].value)
    
