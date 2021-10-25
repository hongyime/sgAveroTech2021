# Singapore Avero Tech 2021
code to scrap profile photos of students from school portals (working till June 2021)

<p align="center">
  <img src="https://www.avero-tech.com/assets/img/avero.png" width='400' height='100'/>
</p>

## Disclaimer
1. USE AT OWN DISCRETION
2. FOR EDUCATIONAL PURPOSES ONLY

## Requirements:
Software
1. [Python 3](https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe)

Hardware
1. Laptop / Desktop (running windows or mac)

## Instructions:
1. Download repository as a zip folder
2. Unzip the folder
3. Run [getimages.py](https://github.com/bryanseah234/sgAveroTech2021/main/getimages.py) to use randomised MD5 ids to get images
4. Run [md5generate.py](https://github.com/bryanseah234/sgAveroTech2021/md5generate.py) to generate yr own MD5 to match those in [samplemd5s.txt](https://github.com/bryanseah234/sgAveroTech2021/samplemd5s.txt)
5. Poke around and look at the other stuff uploaded

## Frequently asked questions:
### What schools are affected?
All the schools which use Avero as their school portal. As seen on their website: EJC, NYJC, NYGHS, TJC, VJC, ASRJC, YIJC, JPJC, TMJC.

### How to access the photos?
Basically, each profile image is linked to the student's unique MD5 id (32 characters), but we don't know how each id is created. Photos from the same shcool uses the same base url, like all other files stored on Avero's database. To get the phoot, you change the get request parameters in the url.\
For example: https://portal.ejc.edu.sg/.image?request=preview&type=Student&id=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.

### How can this be misused?
Generating possible MD5 ids is tedious, but not impossible. Any one with enough processing power can easily generate enough MD5 ids to scrap photos, after knowing the base url. Moreover, MD5s can be easily cracked using Rainbow Table etc. Fortunately, a quick crosscheck with online services produces no immediate hits for the MD5 ids scrapped from the school portals. Thus, it is not known how they are generated, but only time will tell. I have uploaded a small sample for anyone who is interested in this project, and would like to help crack the MD5 for the sheer challenge of it.

### Has this been fixed?
Yes, as of August 2021, using the link to access to profile images are no longer working. Avero has patched the loophole.

### Is this a breach of data privacy?
On every school portal, under 'My Profile' > 'Particulars', Avero states "Your profile photo is visible to you, your parents and all staffs, but not other students, parents, alumni, or the public." However, it is clearly seen that the link to the profile images were never private, unti very recently. The links could also be accessed without logging in to any of the portals. Although these links are not scrapped by google, thus not easily found, it is still, in my opinion, a break of data privacy, as anyone who has the will and processing power can easily generate the required links. Also, students are promised that their profile images will be only "visible to you, your parents and all staffs, but not other students, parents, alumni, or the public". The very existence of this repository is to debunk that.
![image](https://user-images.githubusercontent.com/66017805/130156069-37a10a74-3833-4413-9d69-7a16726323fe.png)

<img align="left" width="400" height="300" src="https://www.avero-tech.com/assets/img/portal_nygh.png">
<img align="left" width="400" height="300" src="https://www.avero-tech.com/assets/img/portal_nyjc.png">
<img align="left" width="400" height="300" src="https://www.avero-tech.com/assets/img/portal_tmjc.png">
<img align="left" width="400" height="300" src="https://www.avero-tech.com/assets/img/portal_yijc.png">
<img align="left" width="400" height="300" src="https://www.avero-tech.com/assets/img/portal_jpjc.png">
<img align="left" width="400" height="300" src="https://www.avero-tech.com/assets/img/portal_tjc.png">
<img align="left" width="400" height="300" src="https://www.avero-tech.com/assets/img/portal_ejc.png">
<img align="left" width="400" height="300" src="https://www.avero-tech.com/assets/img/portal_vjc.png">
