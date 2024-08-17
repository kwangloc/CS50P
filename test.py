import requests
import json
    
response = requests.get("https://hugoversary-e959c-default-rtdb.asia-southeast1.firebasedatabase.app/answers.json?fbclid=IwAR1Naf9OxtE4kgaCz56Mmy_E0Dqkh-3IPVgZFwdiCJoZu7pvCx1inDHw_4g")
# print(response.json())
# print(json.dumps(response.json(), indent=2))
json_str = json.dumps(response.json(), ensure_ascii=False, indent=2).encode('utf8')
print(json_str.decode())
# with open('json.txt', 'w', encoding='utf8') as json_str:
#     json.dump(response.json(), json_str, ensure_ascii=False)
# o = response.json()
# for result in o["results"]:
#     print(result["trackName"])

{
"-N_Tp6wLk_XEVjOSVDuX": 
	{
		"bestEvents": {"answer": ["Hugo Camping"], "questions": "Sự kiện nào được tổ chức bởi Hugo đã để lại cho bạn nhiều kỷ niệm khó quên nhất?"}, 
		"bestMembers": {"answer": ["Huỳnh Hoàng Thiện Kim", "Huỳnh Kim Hoàng", "Lê Quang Nhật"], "question": "Theo bạn, Hugoer nào đã hoạt động năng nổ nhất trong nhiệm kỳ vừa qua?"}, 	"isGoing": false, 
		"name": "Hoàng Văn Thắng", 
		"perfectDuos": {"answer": ["Văn Thắng & Bảo Chiến", "Văn Thắng & Nguyên Khánh", "Lê Quang Nhật & Mai Trâm Anh"], "questions": "Bộ đôi nào trong Hugo để lại cho bạn nhiều ấn tượng nhất?"}, 
		"team": {"slogan": "Justice For All", "theme": "red", "value": "Power Rangers"}, 
		"theRookies": {"answer": ["Đặng Bảo Chiến", "Thu Thuỷ", "Minh Tâm"], "question": "Theo bạn, những tân binh nào đã có màn thể hiện ấn tượng nhất trong thời gian vừa qua?"}
	}, 
"-N_TprossGnCWx1oGMyP": 
	{
		"bestEvents": {"answer": ["Hugo Camping", "Hugo Christmas"], "questions": "Sự kiện nào được tổ chức bởi Hugo đã để lại cho bạn nhiều kỷ niệm khó quên nhất?"}, 				"bestMembers": {"answer": ["Huỳnh Hoàng Thiện Kim", "Huỳnh Kim Hoàng", "Nguyễn Đức Quang"], "question": "Theo bạn, Hugoer nào đã hoạt động năng nổ nhất trong nhiệm kỳ vừa qua?"}, 
		"isGoing": false, 
		"name": " Nguyễn Ngọc Tường Vy", 
		"perfectDuos": {"answer": ["Nguyễn Quang Trường Phước & Nguyễn Lê Hồng Giang"], "questions": "Bộ đôi nào trong Hugo để lại cho bạn nhiều ấn tượng nhất?"}, 
		"team": {"slogan": "We Come In Bunch", "theme": "yellow", "value": "Banana"}, 
		"theRookies": {"answer": ["Trần Tuấn Võ", "Đoàn Nhật Huy", "Ngô Thị Mỵ"], "question": "Theo bạn, những tân binh nào đã có màn thể hiện ấn tượng nhất trong thời gian vừa qua?"}
	}, 
"-N_TqWWHzpDoKVrQNXVV": 
	{
		"bestEvents": {"answer": ["My Tet", "Christmas", "Welcome newbie 2023"], "questions": "Sự kiện nào được tổ chức bởi Hugo đã để lại cho bạn nhiều kỷ niệm khó quên nhất?"}, 		"bestMembers": {"answer": ["Anh Khoa", "Huỳnh Kim", "Nguyên Khánh "], "question": "Theo bạn, Hugoer nào đã hoạt động năng nổ nhất trong nhiệm kỳ vừa qua?"}, 
		"isGoing": false, 
		"name": "Phạm Mạnh Dũng", 
		"perfectDuos": {"answer": ["", "Anh Khoa - Ngọc Uyên"], "questions": "Bộ đôi nào trong Hugo để lại cho bạn nhiều ấn tượng nhất?"}, 
		"team": {"slogan": "Justice For All", "theme": "red", "value": "Power Rangers"}, 
		"theRookies": {"answer": ["Dương Thu Hoài", "Trần Tuấn Võ", "Ngô Thị Mỵ"], "question": "Theo bạn, những tân binh nào đã có màn thể hiện ấn tượng nhất trong thời gian vừa qua?"}
	}, 
