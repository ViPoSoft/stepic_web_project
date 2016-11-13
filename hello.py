#def app(environ, start_response):
#    data = ''
#    for line in environ["QUERY_STRING"].split("&"):
#        data = data+line+"\n"
#    start_response('200 OK', [('Content-Type', 'text/plain')])
#return data


#    data = '\n'.join(environ['QUERY_STRING'].split('&'))
#    status = '200 OK'
#    response_headers = [
#        ('Content-type','text/plain'),
#        ('Content-Length', str(len(data)))
#    ]
#    start_response(status, response_headers)
#    return iter([data])
#
from re import sub

def app(environ, start_response):
    """wsgi minimal app.
    $ gunicorn hello:app
    """
    #parameters = parse_qs(environ.get('QUERY_STRING', ''))

    #output = ''
    #for p in parameters:
    #    for r in parameters[p]:
    #        output += p + '=' + r + '\n'
    #start_response('200 OK', [('Content-Type', 'text/plain')])

    #return iter([str.encode(output)])
    output = sub('&', '\n', environ.get('QUERY_STRING', ''))

    start_response('200 OK', [('Content-Type', 'text/plain')])
    return iter([str.encode(output)])
