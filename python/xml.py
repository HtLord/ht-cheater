import xml.etree.ElementTree as ET


"""
Load data as element tree
"""
# From file
t = ET.parse('/some/where/file.xml')

# From string
t = ET.fromstring(
	"""
	<hello>
		<world>1</world>
		<world>2</world>
		<world>3</world>
	</hello>
	<others>
		<nested>
			<nestedHead/>
			<nestedBody>
				<items>
					<item>
						<field1>1</field1>
						<field2>A</field2>
					</item>
					<item>
						<field1>2</field1>
						<field2>B</field2>
					</item>
					<item>
						<field1>3</field1>
						<field2>C</field2>
					</item>
				</items>
			<nestedBody/>
		</nested>
	</others>
	"""
)


"""
Get elements
"""
# In current layer
t.findtext('elementName')

# In nested layer
f
t.find('hello')