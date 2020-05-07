# py_ver == "3.6.9"
import flask

app = flask.Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    url = flask.request.path
    return """
          <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
          <title>404 Not Found</title>
          <h1>Not Found</h1>
          <p>The requested path <b>%s</b> was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
          """ % url


@app.route('/send_proxy_request')
def send_proxy_request():
    return """
            <html>
                <title>What to GET</title>
                <body>
                    <form action="/proxy_get">
                        Enter URL: <input name="url" type="text" />
                        <input name="submit" type="submit">
                    </form>
                </body>
            </html>
"""


import requests


@app.route('/proxy_get')
def proxy_get():
    url = flask.request.args.get('url')
    if url.startswith(('http://', 'https://')):
        result = requests.get(url)
        return "%s" % result.text
    else:
        return flask.redirect('/send_proxy_request')


if __name__ == '__main__':
    app.run()
