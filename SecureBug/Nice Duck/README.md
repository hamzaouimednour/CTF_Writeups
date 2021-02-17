we got pcapng file of http file manager trafic, after checking that with wireshark i noticed that the user open file in this file manager name movie.mp4, so all we need is to recover this file.

	we can done this by python script using scapy or just simply use wireshark (Go to Edit > Preferences > Protocols > TCP. Enable "Allow subdissector to reassemble TCP streams." Then go to File > Export Objects > HTTP. Select the video stream, then click on "Save As" and save with an appropriate extension)

open movie.mp4 and u will get :

__SBCTF{1n53cur3_commun1c471on}__