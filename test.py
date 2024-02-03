import requests

cookies = {
    'covers_ai_email': 'nkdwkwldnw@gmail.com',
    'covers_ai_artist_id': '7adb65b1-755e-4489-9037-c38fb1e4582f',
    'covers_ai_agrees_to_terms': 'true',
}

headers = {
    'authority': 'covers.ai',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,ja;q=0.8',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjY5NjI5NzU5NmJiNWQ4N2NjOTc2Y2E2YmY0Mzc3NGE3YWE5OTMxMjkiLCJ0eXAiOiJKV1QifQ.eyJwcm92aWRlcl9pZCI6ImFub255bW91cyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9jb3ZlcnMtYWkiLCJhdWQiOiJjb3ZlcnMtYWkiLCJhdXRoX3RpbWUiOjE3MDY5NjM0MjQsInVzZXJfaWQiOiJ5YTh6OGV3SmNUWXpBeDY3ZVFsUFpDSnNiSjczIiwic3ViIjoieWE4ejhld0pjVFl6QXg2N2VRbFBaQ0pzYko3MyIsImlhdCI6MTcwNjk2MzQyNCwiZXhwIjoxNzA2OTY3MDI0LCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7fSwic2lnbl9pbl9wcm92aWRlciI6ImFub255bW91cyJ9fQ.Jm0CG_U6QbQCeoRBUiheJqpoakNkPFpcTiWr9Tt6gB4lWHC_Se0WzhBY_jtUufXwMC9ZI5lLQjJf-9CoKYi1mLk5kL_cYK47PSdqlKdLnnS0p5-2SWiShvJvG0Kvl1nplWiRzf6TmL8m_n7hsfKPYdVxI4h6QJtIDeDom7LDQOutM96ff3YNosLfdcAlbmSfplyvtKKIXmNt15_8mCJdvYz-KgDdZT55Mrn4BrI8EztyfhL9vRu80IyVG2bDmPNTxSi7zPJ9TCwowTuRDU7gbLdP-3cprnDXgBf80wC2YgufXKhMEpFRzfnYuZ1-HldFOz0W4Y5_tSDENhXmPuP9BQ',
    'content-type': 'application/json',
    # 'cookie': 'covers_ai_email=nkdwkwldnw@gmail.com; covers_ai_artist_id=7adb65b1-755e-4489-9037-c38fb1e4582f; covers_ai_agrees_to_terms=true',
    'origin': 'https://covers.ai',
    'referer': 'https://covers.ai/ai-song-generator',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

json_data = {
    'url': 'https://storage.googleapis.com/covers-ai.appspot.com/song_catalog/Lexi%20Jayde%20-%20drunk%20text%20me.mp3',
    'email': 'nkdwkwldnw@gmail.com',
    'name': '7adb65b1-755e-4489-9037-c38fb1e4582f',
    'modelDisplayName': 'Amitabh Bachchan AI FAYK',
    'didAgreeToNotify': True,
    'isDuet': False,
    'secondVoiceId': '',
}

response = requests.post('https://covers.ai/handleRequest', cookies=cookies, headers=headers, json=json_data)

print(response.json())