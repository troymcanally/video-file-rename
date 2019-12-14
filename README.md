<h2>Video File Batch Renaming Script</h2>

***

So I got tired of renaming files for my Plex Media Server, especially when I had an entire season of a show. The Plex convention is "Name of show s01e01" with s being season and e being episode.

I ended up writing this short Python script to do exactly that. It reads the files in my video folder, splits the filenames to preserve the filetype, and asks the user for the name of the show and current season number. The script then iterates through all of the files one by one and renames them in episode order, as they are read into the initial list using the os Python library. The script is hard coded to where video files sit on my PC before I move them to Plex.



