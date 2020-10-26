from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special" id="itemOne">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
#print(type(soup)) # <class 'bs4.BeautifulSoup'>
#print(soup) # prints the whole html
#print(soup.head) # prints the head of the html
#print(soup.body) # prints the body of the html

# soup.find("div") === soup.body.div -> both will print the FIRST div it finds
div = soup.find("div")
"""
<div id="first">
<h3 data-example="yes">hi</h3>
<p>more text.</p>
</div>
"""
# print(type(div)) # <class 'bs4.element.Tag'>

all_div = soup.find_all("div") # FINDS all occurences
# print(all_div)
"""
[ <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>, 
  <div data-example="yes">bye</div>]
"""

byId = soup.find(id="itemOne") # FINDS any elements by id
# print(byId) # <li class="special" id="itemOne">This list item is special.</li>

#You need to use find_all for classes class_  if you want them all
byClass = soup.find_all(class_="special") # FINDS all elements by CLASS
# print(byClass) # [<li class="special" id="itemOne">This list item is special.</li>, <li class="special">This list item is also special.</li>]

#You need to use find_all for attributes if you want them all
byAttr = soup.find_all(attrs={"data-example":"yes"}) # FINDS any elements with key attribute: data-example AND value: yes
# print(byAttr) # [<h3 data-example="yes">hi</h3>, <div data-example="yes">bye</div>]

#=======CSS SELECTORS: use the selectors you would use when using CSS===============================================================
# WHEN YOU USE .select(selector) -> [YOU always get a list back]

selector_byId = soup.select("#itemOne") # SELECTS any element with this id
#print(selector_byId) # [<li class="special" id="itemOne">This list item is special.</li>]

selector_byClass = soup.select(".special") # SELECTS ALL elements with this class
# print(selector_byClass) # [<li class="special" id="itemOne">This list item is special.</li>, <li class="special">This list item is also special.</li>]

selector_byTag = soup.select("div") # SELECTS ALL elements using this tag
# print(selector_byTag)
"""
[ <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>, 
  <div data-example="yes">bye</div>]
"""

selector_byAttr = soup.select("[data-example]") # SELECTS any element with key attribute: data-example
# print(selector_byAttr) # [<h3 data-example="yes">hi</h3>, <div data-example="yes">bye</div>]


