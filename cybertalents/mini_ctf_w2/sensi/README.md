it seems like `sensi.txt` a regular txt file (not an archive, not any intersting meta data, contains few lines) but its not, while hex dumping it found many tabs and spaces for a while i thought chall preseting a binary code with those spaces and tabs but after many tries is not.

few minutes later checking google  for steganography in txt files found that tool `stegsnow`([hide text in text files using stegsnow](https://delightlylinux.wordpress.com/2016/12/14/hide-text-in-text-files-using-stegsnow/))

`stegsnow -C sensi.txt` : gives unreadable text, so it's obvious we need a password.

found this tool [SnowCracker](https://github.com/0xMohammed/SnowCracker) by 0xMohammed, it uses stegsnow but with a worlist.

```sh
python3 SnowCracker/snowcracker.py -c N -f sensi.txt -w rockyou.txt |grep -P "flag{(.*)}" --ignore-case
...
Message : flag{it_is_you_sensi_9234872364}
```