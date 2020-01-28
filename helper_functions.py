import os

mimetypes = {
	".html":"text/html",
	".js":"application/javascript",
	".json":"application/json",
	".css":"text/css",
	".csv":"text/csv",
	".zip":"application/zip",
	".sql":"application/sql",
	".doc":"application/msword",
	".mp3":"audio/mpeg",
	".ogg":"audio/ogg",
	".txt":"text/plain",
	".jpg":"image/jpeg",
	".jpeg":"image/jpeg",
	".png":"image/png",
	".gif":"image/gif"
}

def getMimeType(filename):
	file_ext = os.path.splitext(filename)[1]
	if(mimetypes.get(file_ext)):
		return mimetypes.get(file_ext)
	else:
		return 'text/plain'
