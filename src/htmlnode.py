class HTMLNode:
    def __init__(self, **kwargs):
        self.tag = kwargs.get("tag", None)
        self.value = kwargs.get("value", None)
        self.children = kwargs.get("children", None)
        self.props = kwargs.get("props", None)

    def to_html(self):
        raise NotImplementedError("This method has not been implemented")

    def props_to_html(self):
        attributes = ""
        if self.props:
            attributes += "".join(f" {attr_name}=\"{attr_value}\"" for attr_name, attr_value in self.props.items())
        else:
            pass
        return attributes

    def __repr__(self):
        child_nodes = ''
        if self.children:
            child_nodes = "".join(f"{str(child_node)}" for child_node in self.children)
        else:
            pass

        html = f'''<{self.tag} {self.props_to_html()}>\n\t{self.value if not self.value == None else ""}\n\t{child_nodes}\n</{self.tag}>'''

        return html
            


# html_node = HTMLNode(tag="div",value="hello abibi", children=[HTMLNode(tag='p',value="I am a paragraph",children=[],props={"class": "text-center"})], props={
#     "href": "https://www.google.com", 
#     "target": "_blank",
# })

# print(str(html_node))