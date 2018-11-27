import dropbox
dbx = dropbox.Dropbox('ACCESS_TOKEN')

for x in range(0, 15):
    for entry in dbx.files_list_folder('/Photos', limit = 1).entries:
        print(entry.name)
        dbx.files_move_v2('/Photos/'+entry.name,'/Tumblr/'+entry.name, allow_shared_folder=False, autorename=False, allow_ownership_transfer=False)
        x = x+1
    
