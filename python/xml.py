import xml.etree.ElementTree as ET


"""
Load data as element tree
"""
# From file
t = ET.parse('/some/where/file.xml')

# From string
t = ET.fromstring(
	"""
	<document>
		<hello>
			<world>1</world>
			<world>2</world>
			<world>3</world>
		</hello>
		<others>
			<field1>1</field1>
			<field2>2</field2>
			<field3>3</field3>
			<field4>4</field4>
			<field5>5</field5>
			<nested>
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
				</nestedBody>
			</nested>
		</others>
	</document>
	"""
)


"""
Get elements
"""
# In elements directly under root
hello = t.find('hello')
others = t.find('others')

# looping to get elements
for world in hello:
	print(world.text)

# Get specific elements value by its name
others.findtext('field1')
others.findtext('field4')