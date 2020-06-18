#!C:\python 3.5\python.exe
print("content-type:text/html;")
print()
####################################################################
####################################################################
###################### html 한글깨짐해결코드 ########################
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
####################################################################
####################################################################
####################################################################
import cgi
import module
import html_sanitizer
sanitizer = html_sanitizer.Sanitizer()  # default configuration




form = cgi.FieldStorage()
if 'id' in form:
    pageId=form['id'].value
    description = open('data/'+pageId,'r').read()

    # need to Sanitizer
    description = description.replace('<','&lt;')
    description = description.replace('>','&gt;')
    description = sanitizer.sanitize(description)

    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_btn = '''
    <form action='process_delete.py' method='post'>

        <input type='hidden' name='pageId' value={}>
        <input type='submit' value='Delete'>

    </form>'''.format(pageId)

    delete = "<a href='delete.py?id={}'>delete</a>".format(pageId)
else :
    pageId ='welcome'
    description = 'hello web'
    update_link =''
    delete_btn =''
import os



print(r'''<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <title>{users}</title>
  <link rel="stylesheet" href="style.css">
</head>

<body>
  <h1><a href='index.py'>{users}</a></h1>
  <div id='grid'>
    <ol>{fileList}</ol>

    <div id='article'>
    <a href='create.py'>creat</a>
    {update_link}
    {delete}
      <h2>{name}</h2>
      <p>{desc}</p>
    </div>
  </div>
</body>

</html>

'''.format(users='Python Page',name=pageId,desc=description,fileList=module.getList(),update_link=update_link,delete=delete_btn))
