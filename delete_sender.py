import requests

payload = {
	"email": "carter+test2@iterable.com",
	"senderName": "blah blah blah"
}

headers = {
	"authority": "app.iterable.com",
	"Content-type": "application/x-www-form-urlencoded",
	"referer": "https://app.iterable.com/settings/senders"
}

cookie = {
	"iterableEndUserId":"carter+test@iterable.com",
	"ajs_group_id"
	"iterableCookie":"e694b7356bcda103be4eb0b2339cd12dad285cb7b3487e589d42c7f9d0f04a405b1d0b660be28b25aa1970a6e80ae6a2df2c388ddf2ac4c2ad1a4f1b7bc430dde9ab992fc5e95ecf2bc91b43c8b584409822086293e608438613de5a58ea6ca1ae2d7fa0d4f169ef832a94a8e7ddd450d897ad5bf9ea76bca843398302c9832d",
	"ajs_user_id":"demo@iterable.com",
	"PLAY_SESSION": "23dce257a905130351a3f706794ab1ba5333d787-csrfToken=12712afd38c06a0ada2f0ff1acb585b1a1234e5b-1516378330626-f09c7579cacad68c3ec352dd&ViewAsUserAdminCookie=demo@iterable.com&iterableCurrentProjectId=3016"
}

url= "https://api.iterable.com/i/emailAddSubmit"

r = requests.request(method="POST", url=url, data=payload, headers=headers, cookies= cookie)

print(r.json())