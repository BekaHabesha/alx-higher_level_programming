#!/usr/bin/python3
# Author - Bereket Dereje

"""
Python script that:
  - fetches https://intranet.hbtn.io/status
  - must use the package requests
  - not allow to import packages other than requests.
"""

import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
