#!/usr/bin/python3
# Author - Bereket Dereje

"""
Phython Script that:
  - fetches https://intranet.hbtn.io/status
  - must use the package requests
  - not allow to import packages other than requests.
"""


if __name__ == '__main__':
    import requests
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(html.text.__class__))
    print("\t- content: {}".format(html.text))
