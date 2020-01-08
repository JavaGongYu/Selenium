from xml.dom.minidom import parse

dom = parse('../date_file/config.xml')

root = dom.documentElement

tag_name = root.getElementsByTagName('platform')

print(tag_name[0].firstChild.data)
