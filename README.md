# SPOTIFY-AUTOMATION-USING-RECOMMENDER-SYSTEM-DATASET
We will first have top 50 songs based on popularity based recommender system then we will create a spotify playlist of these songs.
1. Datasets: 
  a. Triplet file: https://static.turi.com/datasets/millionsong/10000.txt Contains user_id, song_id, ListenCount (in order)

  b. Metadata : https://static.turi.com/datasets/millionsong/song_data.csv

2 Token Generation: As a token gets expired after a few hours so need to generate a new token after it’s expiry. 
  a. Click on get token button: (on this link: https://developer.spotify.com/console/get-search-item/)
  b. This window will be prompted: After selecting the required scopes click on Request token. 
  c. Your new token will be available here, copy it and use it.
  
3. API used: 
  a. Creating a new Playlist: https://developer.spotify.com/console/post-playlists/ 
  b. Searching a song: https://developer.spotify.com/console/get-search-item/ 
  c. Adding song to the Playlist: https://developer.spotify.com/console/post-playlist-tracks/ 
  
4. Command prompt : 
  a. Navigate to the directory of your project and then run the command - “Python run.py” .Here run.py is our python file that is coded by us so as to implement our project. 
  b. The data dictionary of the top 50 songs will be the output in the command prompt.

5. Newly created playlist on spotify : 
  A playlist will be created on our spotify account. 
  
  
HOW TO IMPLEMENT THIS PROJECT IN YOUR SYSTEM 
1. Open the run.py file. 
2. Change the user id to your spotify user id. 
3. Generate the token by following the steps mentioned above. 
4. Now run it in the command prompt as shown above. 
5. The playlist will be created in your spotify account.

