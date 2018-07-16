import webview
import threading

"""
This example demonstrates how to load HTML in a web view window
"""


def load_html():
    with open("index.html",'r') as f:
    	l = f.read()
    webview.load_html(l)


if __name__ == '__main__':
    t = threading.Thread(target=load_html)
    t.start()

    webview.create_window('Load HTML Example')