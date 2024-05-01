import xml.etree.ElementTree as ET

my_tree = ET.parse('../../sample.xml')
my_root_1=my_tree.getroot()
print(my_root_1)
print(ET.tostring(my_root_1, encoding='utf8').decode('utf8'))
# List of tags
for el in my_root_1.iter():
   print([el.tag])
#------------------------------------------------------------------------------------------------------------------
data='''<?xml version="1.0" encoding="UTF-8"?>
<Snapshot Date="2015-02-22">
    <Instruments id="45334">Hello
        <ADR InstrumentId="US92857W2098" InstrumentName="Vod ADR NYSE" ISIN="US92857W2098" Market="XNYS" CUSIP="92857W209" ConversionRatio="2" MarketsListedIn="XNYS">
            <Component InstrumentId="GB00BH4HKS39"/>
        </ADR>
    </Instruments>
    <Portfolios>Good By
        <Portfolio PortfolioId="11">Now
            <price>50</price>
            <Asset AssetId="1" AssetName="Vodafone ADR" InstrumentId="US92857W2098" Quantity="14000"/>
        </Portfolio>
        <Portfolio PortfolioId="12">Again Now
            <Asset AssetId="1" AssetName="Vodafone Equity" InstrumentId="GB00BH4HKS39" Quantity="30000"/>
        </Portfolio>
    </Portfolios>
</Snapshot>'''
my_root=ET.fromstring(data)
print(ET.tostring(my_root, encoding='utf8').decode('utf8'))
print(my_root)
print(my_root.tag)
print(my_root[0].tag)
print(my_root[0].attrib)
print(my_root.find('Instruments').get('id'))

"""
for elem in my_root:
    print(elem.tag,elem.attrib)
    
for x in my_root:
    print(x.text)

for y in my_root.findall('Portfolios'):
    item=y.find('Portfolio').text
    print(item)
#---------------------------------------------------------------------------------------------------------------
    #Modifying current element
for z in my_root_1.iter('Price'):
    a=str(z.text)+' from 2020'
    z.text=str(a)
    z.set('updated','yes')   
my_tree.write('new_2.xml')


#Adding new element
ET.SubElement(my_root_1[0],'special')
for k in my_root_1.iter('special'):
    b='Something special'
    k.text=str(b)
my_tree.write('new_3.xml')
#----------------------------------------------------------------------------------------------------------
#Removing current attribute
my_root_1[0][0].attrib.pop('InstrumentId')
my_tree.write('new_4.xml')
#---------------------------------------------------------------------------------------------------------------
#Removing tag
my_root_1[0].remove(my_root_1[0][0])
my_tree.write('new_5.xml')
#-------------------------------------------------------------------------------------------------------------
#Clearing tag
my_root_1[0].clear()
my_tree.write('new_6.xml')
"""