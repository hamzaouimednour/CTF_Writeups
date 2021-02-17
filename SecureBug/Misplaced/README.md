Challenge Name: Misplaced
Level: Easy
Category: Forensics

```sh
binwalk misplaced.zip
```

	DECIMAL       HEXADECIMAL     DESCRIPTION
	--------------------------------------------------------------------------------
	1048576       0x100000        Zip archive data, encrypted at least v2.0 to extract, compressed size: 282364, uncompressed size: 287052, name: Article1.jpg
	1331114       0x144FAA        End of Zip archive, footer length: 64, comment: "Password: 3a24869a641d60c09ceb71af4f99cffc"

```sh
zip -FF misplaced.zip --out output.zip
zip -FF misplaced.zip --out output.zip -P 3a24869a641d60c09ceb71af4f99cffc
7z x -p3a24869a641d60c09ceb71af4f99cffc output.zip
```
	
	Article1.jpg   

```sh
file Article1.jpg                                                                            
#Article1.jpg: Microsoft Word 2007+
mv Article1.jpg Article1.docx
```

just open Article1.docx and u'll get the flag.

__SBCTF{n1c3_c4rv1n6_w3ll_d0n3}__