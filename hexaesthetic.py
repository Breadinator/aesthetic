# Works, but there is a bug in which it says "aesthetic :Unknown command" but prints the text regardless. /shrug
# Licensed under the Copyfree Open Innovation License, which can be found in the next comment.
# http://copyfree.org/content/standard/licenses/coli/license.txt

import hexchat

__module_name__ = 'aesthetic'
__module_author__ = 'Breadinator'
__module_version__ = '0.1'
__module_description__ = 'Make your text more a e s t h e t i c'

def strToAesthetic(word, word_eol, userdata):
	ugly = word_eol[1]
	aesthetic = ""
	
	for n, i in enumerate(ugly):
		if n == len(ugly) - 1:
			aesthetic += str(i).lower() + "   "
		else:
			aesthetic += str(i).lower() + " "

	hexchat.command("say " + aesthetic)

hexchat.hook_command('aesthetic', strToAesthetic, help="/aesthetic <string>")
hexchat.prnt(__module_name__ + " by " + __module_author__ + " loaded.")