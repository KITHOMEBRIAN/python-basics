
def remove_spaces(text):
    text_list = text.split(' ')
    new_text = ''.join(text_list)
    return new_text


def cost_of_project(engraving, solid_gold):
    engraving = remove_spaces(engraving)
    length_string = len(engraving)
    if solid_gold:
        cost= 100 + 10 * length_string
    else:
        cost= 50 + 7* length_string
    return cost


print(cost_of_project("kithome 187", True))
print(remove_spaces('12 34'))


