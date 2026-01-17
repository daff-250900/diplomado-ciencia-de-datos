from googleapiclient.discovery import build
import json

API_KEY = "AIzaSyBUk3mZH2oXJMjtONFFIk_L2EnqjTCukWw"
VIDEO_ID = "iYLEJfOUiOs"

youtube = build("youtube", "v3", developerKey=API_KEY)

comments = []
next_page_token = None

while True:
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=VIDEO_ID,
        maxResults=100,
        pageToken=next_page_token,
        textFormat="plainText"
    )
    
    response = request.execute()
    
    for item in response["items"]:
        snippet = item["snippet"]["topLevelComment"]["snippet"]
        comments.append({
            "author": snippet["authorDisplayName"],
            "date": snippet["publishedAt"],
            "comment": snippet["textDisplay"],
            "likes": snippet["likeCount"]
        })
    
    next_page_token = response.get("nextPageToken")
    
    if not next_page_token:
        break

with open("youtube_comments.json", "w", encoding="utf-8") as f:
    json.dump(comments, f, ensure_ascii=False, indent=4)

print(f"Total de comentarios extraídos: {len(comments)}")