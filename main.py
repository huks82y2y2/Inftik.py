import requests
from flask import Flask
@huks.route("/tiktok/user=<user>")
def h(user):
                url = f"https://tiktok-best-experience.p.rapidapi.com/user/{user}"
                headers = {
		"x-rapidapi-key":"d0cbbe1f79mshe3c74080d9d0da5p1de4ddjsn21db44140e77",
		"x-rapidapi-host":"tiktok-best-experience.p.rapidapi.com",
		"User-Agent":"TikTracker/1.2 (com.markuswu.TikTracker; build:1; iOS 14.4.0) Alamofire/5.4.4"
	}
                r = (requests.get(url,headers=headers).json())
                return r
huks.run()
