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
data = soup.body.contents
# print(data) # all tags in the body AS a LIST [] :
"""
['\n', <div id="first"> <h3 data-example="yes">hi</h3> <p>more text.</p> </div>, '\n', 
<ol> <li class="special" id="itemOne">This list item is special.</li>
<li class="special">This list item is also special.</li>
<li>This list item is not special.</li>
</ol>, '\n', <div data-example="yes">bye</div>, '\n']
"""
element = data[1] # -> <div id="first"> <h3 data-example="yes">hi</h3> <p>more text.</p> </div>
# print(element.contents) # ['\n', <h3 data-example="yes">hi</h3>, '\n', <p>more text.</p>, '\n']
#---------------------------------------------------------------------------------------------------------
# next_sibling -> next element in the contents array
# next_siblings -> array of all the next elements in the contents array
# previous_sibling -> previous element in the contents array
# previous_siblings -> array of all the previous elements in the contents array

# print(element.next_sibling) # \n
# print(element.next_sibling.next_sibling) # <ol> ... </ol> BUT USE THE SEARCH METHODS BELOW BETTER:

siblingsOfDivFirst = element.next_siblings
# print(siblingsOfDivFirst) # <generator object PageElement.next_siblings at 0x028ED450>
for target_list in siblingsOfDivFirst:
    pass # print(target_list)
#---------------------------------------------------------------------------------------------------------
# parent -> parent content of current element
# parents -> list of all parents of current element
# print(element.parent) :
"""
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
"""
# print(element.parents) # <generator object PageElement.parents at 0x031ED140>
# for target_list in element.parents:
#     print(target_list) # -> first the body and all its content, then the whole html and all its contents

#SEARCHING----------------------------------------------------------------------------------------------
# find_next_sibling([class_=, id=, etc]) : find next sibling(non empty or \n) | if args passed, find next sibling that has: class_: "any", id: "asd", etc
# find_next_siblings([class_=, id=, etc]) : find next siblings(non empty or \n) | if args passed, find next siblings that has: class_: "any", id: "asd", etc
# find_previous_sibling([class_=, id=, etc]) | find_previous_siblings([class_=, id=, etc]) # same as find next but the opposite direction
# find_parent(["div"]) : find parent | if args passed, find parent that is "tag"

# print(element.find_next_sibling()) # <ol> ... </ol> -> this will find the next sibling with tag

lastElement = soup.body.find_all(attrs={'data-example':'yes'})[1] # <div data-example="yes">bye</div>
# print(lastElement.previous_sibling) # \n
# print(lastElement.find_previous_sibling()) # <ol> ... </ol> -> this will find the previous sibling with tag








