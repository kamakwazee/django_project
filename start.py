import mechanize

br = mechanizee.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
br.open('http://localhost:8000/textapp/')

br.form = list(br.forms())[0]

for control in br.form.controls:
	print control
	print '\n type=%s, name=%s, value=%s' % (control.type, control.name, br[control.name])
