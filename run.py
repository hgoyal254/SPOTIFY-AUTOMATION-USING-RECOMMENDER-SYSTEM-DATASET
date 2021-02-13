import os
import songdict
import spotify

song_dic = songdict.createDic()
def run():
    token = "BQDWdI1Z6SYAHUfwuLvLZg_XQeC4IZPfNvaX8wziYY4z-_6T3e31T5YNhU8u292kE_PDyBu9nb0MnTBv6GwSC7LyC5-DmJS3ZrpqqpK2iMfyvmidQ6z72BXSjLdrbRDYfRAIvzMdY3tVTyOJBVsrQaMDgps7bYrX1pafYhBuLmFqyw537vWWDisyQqIXvM8HZCCDNWafs4ZAaWF7p49ibIBHCaRBqrhAF3WfBvBnDccC-16ygozR-IX1GNFlwt86MNy-Ue9KGvvW3k8w2qcxPLsSSvO6V9vjhLM"
    user_id = "g66a4g0hgc0nd0yk6djcv40l6"
    spotify.add_song_playlist(token,song_dic,user_id)
        

if __name__ == '__main__':
    run()