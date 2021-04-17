import re

str = """
    560 Military Ave.
    Panama City, FL 32404
    284 Meadow Street
    Newtown, PA 18940
    7755 John St.
    Flowery Branch, GA 30542
    4 NE. Goldfield Dr.
    Port Jefferson Station, NY 11776
    7767 Myrtle Ave.
    Saginaw, MI 48601
    7211 Gainsway Court
    Patchogue, NY 11772
    mrsam@yahoo.com
    rjones@att.net
    mleary@live.com
    lahvak@mac.com
    konst@icloud.com
    mkearl@gmail.com
    smcnabb@icloud.com
    sethbrown@aol.com
    carmena@sbcglobal.net
    qmacro@mac.com
    loscar@aol.com
    weidai@live.com
    7040 Valley Lane
    Fort Lee, NJ 07024
    57 Cleveland Street
    Front Royal, VA 22630
    60 Lower River Street
    Worcester, MA 01604
    16 Mammoth Court
    Emporia, KS 66801
    7143 Tarkiln Hill Rd.
    Statesville, NC 28625
    379 53rd Rd.
    Ada, OK 74820
    8310 Schoolhouse Lane
    Pelham, AL 35124
    7 Elizabeth St.
    Old Bridge, NJ 08857
"""

email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][0-9a-zA-Z._+%]+", str)
print(email)