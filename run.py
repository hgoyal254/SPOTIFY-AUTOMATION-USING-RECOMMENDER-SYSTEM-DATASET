import os
import songdict
import spotify

song_dic = songdict.createDic()
def run():
    #enter your userid and token
    token = 
    user_id = 
    spotify.add_song_playlist(token,song_dic,user_id)
        

if __name__ == '__main__':
    run()
