import re
from src.lib.text_type import TextType
from src.textnode import TextNode

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT.value:
            if delimeter in node.text:
                if node.text.count(delimeter) % 2 != 0:
                    raise Exception("Invalid markdown syntax")

                regex_pattern = fr"{re.escape(delimeter)}(.*?){re.escape(delimeter)}"
                match = re.findall(regex_pattern, node.text)

                splitted_text = node.text.split(delimeter)   

                for text in splitted_text:
                    if text in match:
                        new_node = TextNode(text, text_type)
                        result.append(new_node)
                    else:
                        new_node = TextNode(text, TextType.TEXT)
                        result.append(new_node)  
            else:
                result.append(node)
        else:
            result.append(node)
    return result

            
        



        




# print(result)
# print(re.findall(delimeter_pattern, "this is a `code block` word")[0].replace("`", ""))