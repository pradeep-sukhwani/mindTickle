def main(string=None):
	special_characters = ['{', '(', '[', '}', ')', ']']
	closing_match = {')': '(', ']': '[', '}': '{'}
	update_special_character = []
	for element in string:
		if len(update_special_character) > 0 and closing_match.get(element) and closing_match.get(element) == update_special_character[-1]:
			update_special_character.pop()
		elif element in special_characters:
			update_special_character.append(element)
	if len(update_special_character) > 0:
		return False
	else:
		return True

print(main("abc(x[m]{open_curly_brace}+{close_curly_brace}){open_curly_brace}-{close_curly_brace}".format(open_curly_brace="{", close_curly_brace="}")))

print(main("abc(x[m]{open_curly_brace}+){open_curly_brace}C{close_curly_brace}".format(open_curly_brace="{", close_curly_brace="}")))

stringVal = "fjk[]((hvsd)){sd[hsd]sff}[sdf{}]"
print(main(stringVal))
