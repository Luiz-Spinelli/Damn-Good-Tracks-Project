# Damn Good Tracks Project

## 1. The Big Idea
Our team listens to music everytime: studying, walking/driving to classes, working out at the gym, ... you name it. Still, when we try to find other songs to listen to, we fail. 

Luiz has his favorite artists, but don't know where to find new tracks similar to his taste. 
Bruno tried to use Spotify's "Radio" feature, which is a playlist generated from a specific track. The result: these songs seem quite random. Also, the radio keeps changing, so he "loses" good tracks on it without even knowing. 

The **Damn Good Tracks** website helps with that! On it, users will be able to find recommendations of *certified fresh* tracks and albums based on an artist they like. On a high-level, an user can input whether he wants to find tracks or albums recommendations, and say what artist he wants as inspiration. Our website will then show him either a track list or top albums from artists related to the one chosen, with direct links to listen to them right away on Spotify.

If time permits, we will allow users to download the recommended track list as playlist to their very own Spotify account, after giving permission of course. Also, we can add a filter to display feature tracks, as well the latest drops from this artist.

## 2. Learning Goals
The goal of this project is to learn how to use Spotify's Public API to query music data in an integrated way with the core music app we use everyday. Moreover, we want to explore ways to receive custom user inputs (such as picking tracks or albums) to trigger different outcomes, and also how we can better design user action from it - in this case, listening to the recommendations on Spotify's app!

Personally, Luiz wants to learn how to create an end-to-end application that is able to recommend something effective based on user taste. For Bruno, he wants to see if he can use this code to facilitate his day-to-day song-picking process.

## 3. Implementation Plan
Our plan is to use [Spotipy](https://spotipy.readthedocs.io/en/2.21.0/), which is a Python library for the Spotify Web API, to query and manipulate music data. This library will enable us to get artists, tracks and albums information, along with other relevant data such as similar artists and track popularity, which will be core to our backend application. 

In detail, we will have 2 kinds of recommendations: tracks and albums. 

### 3.1. Tracks
For tracks, first we will find the list of artists related to the one chosen by the user. Then, we will get the top tracks for each of these artists along the original one. We will then randomly choose 20 songs, and get the top10 of these ordered by track popularity. This way, users will always get a fresh sample of top tracks related to the chosen artist.

### 3.2. Albums
Similarly, for albums we will gather the list of artists related to the one chosen by the user, and get their albums. Then, we will sort by popularity, and return a random sample of 5 albums from the top10. 

Finally, we will use Flask to create the web pages with connection to the backend, allowing to pass customize user input to select artist, and category of recommendation (tracks or albums).

## 4. Project Schedule
We will divide the project into 4 sections, tackling 1 per week.

| Week      | Objective |
| ----------- | ----------- |
| #1 (11 - 17 Nov)      | Explore API and library documentation and define key methods needed       |
| #2 (18 - 24 Nov)   | Implement backend functions and logic       |
| #3 (25 Nov - 01 Dec)     | Create web application connected to backend using Flask        |
| #4 (02 - 06 Dec)   | Final testing, webpage styling and submission        |

## 5. Collaboration Plan
Our team will be running on "Agile-like". Every week we will define tasks to achieve the week's objective, and split up. At the end of the week cycle, we will gather and review the progress we had so far, and do a planning for the next week.

A priori, for the backend, we will probably start with a fixed period of study, and then split work by functions. For Flask, we will split up in user input & backend connection, and overall UX/UI.

## 6. Risks
We identified 2 main risks on this project: user input format, and relevance of results. 

The former arises from the fact that Spotipy doesn't appear to have a search by keyword. Therefore, we have to figure out a way to match user input to accurately query the right artist, and handle possible errors. 

The latter is inherent for a content recommendations project like ours. Still, we believe that providing novel picks from related artists with an easy way to jump from the web application to the Spotify app can be quite valueable nonetheless - at least from our experience.

## 7. Additional Course Content
From what we learned so far, API requests using encoded URLs, storage and manipulation of data in lists/dictionaries, and Flask will be the 3 main tenets for our application. 

Regarding new content, we believe learning how to use client side APIs would be key to give us confidence on tackling our vision to connect user's Spotify account right away. Also, we restrained on a binary category input (tracks or albums), but other Flask form input types such as a date filter could help in querying more custom results to users. 