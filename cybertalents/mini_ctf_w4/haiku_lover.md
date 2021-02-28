Secure Coding : fix the vulnerability, by reading the code we found that it reads file from an argument so i thought about LFI, Path Traversal.

code before fixing :

```python
from flask import Flask, request, render_template
from os import getcwd
app  = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def main():
	if request.args.get('haiku'):
		haiku = request.args.get('haiku')
		try:
			f = open(f'{getcwd()}/haikus/{haiku}', 'r')
			content = f.read()
			f.close()
			return render_template('index.html', haiku=content)
		except Exception as e:
			print(str(e))
			return render_template('index.html', err=str(e))
	else:
		return render_template('index.html')
```

with some googling i tried this statment `os.path.commonprefix((os.path.realpath(getcwd()+'/haikus/'+str(haiku)),getcwd()+'/haikus/')) == getcwd()+'/haikus/'` it works as well on local but gives error on chall platform (i dm'ed the admin after solving that told him about this )

code after fixing by adding `and '..' not in request.args.get('haiku')`:

```python
from flask import Flask, request, render_template
from os import getcwd
#from os import path
app  = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def main():
	if request.args.get('haiku') and '..' not in request.args.get('haiku'):
		haiku = request.args.get('haiku')
		try:
			f = open(f'{getcwd()}/haikus/{haiku}', 'r')
			content = f.read()
			f.close()
			return render_template('index.html', haiku=content)
		except Exception as e:
			print(str(e))
			return render_template('index.html', err=str(e))
	else:
		return render_template('index.html')
```

__FLAG{CongratsOnSolvingThis}__