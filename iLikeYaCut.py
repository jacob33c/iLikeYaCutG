from TikTokApi import TikTokApi
import time
import os
import random

api = TikTokApi()

def getLikeCount():
    tiktoks = api.byUsername('jayspanks', count=1)
    for tiktok in tiktoks:
        likeCount = tiktok["stats"]["diggCount"]
        shareCount = tiktok["stats"]["shareCount"]
        commentCount = tiktok["stats"]["commentCount"]
        followCount = tiktok["authorStats"]["followerCount"]
        return (likeCount,shareCount,commentCount,followCount)

def iLikeYaCut():
    os.system("afplay iLikeYaCut.mp3 ")

def update():
    initLikeCount = 0
    initShareCount = 0
    initCommentCount  = 0
    initFollowCount = 411000
    while True:
        results = getLikeCount()
        currentNumShares = results[1]
        print("sleepy time")
        time.sleep(5)
        
        
        if currentNumShares > initShareCount:
            newShares = currentNumShares - initShareCount
            initShareCount = currentNumShares
            print("amount of new shares = ", newShares)
            for x in range(newShares):
                print("now playing iLikeyaCut G", x)
                time.sleep(random.randint(0,3))
                iLikeYaCut()
        else:
            print("No new shares!")
            
update()
#getLikeCount()

