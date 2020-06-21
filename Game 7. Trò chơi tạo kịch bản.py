woman=["một nhà khoa học","một nữ hoàng","một tên cướp biển","một con thỏ khổng lồ"]
man=["một sĩ quan cảnh sát","một nghệ sĩ","ông của bạn","một rô bốt sát thủ"]
place=["trên sao Hỏa","ở siêu thị","trong một cái hang tối tăm ma quái đầy dơi"]
sheWore=["bồ đồ lặn","cánh tiên","một cái túi giấy"]
heWore=["đồ vest tím","đồ hóa trang cá mập","khăn tắm đi biển"]
womanSays=["'Anh là ai?'","'Bao nhiêu hạt đậu thì bằng năm?'","'Tại sao?'"]
manSays=["'Bíp Bóp!'","'Đừng ăn ếch!'","'Mấy giờ cô sẽ gọi cái này?'"]
consequence=["hòa bình thế giới","hỗn loạn","một bàn chân khổng lồ nghiền nát họ","cầu vòng"]
worldSaid=["'Vô nghĩ vớ vẩn'","Phô mai là nhất'","'Tôi đang tan chảy'"]
import random
while True:
    print(random.choice(woman),"gặp",random.choice(man),random.choice(place))
    print("Cô ấy đang mặc", random.choice(sheWore))
    print("Anh ấy đang mặc",random.choice(heWore))
    print("Cô ấy nói",random.choice(womanSays))
    print("Anh ấy nói",random.choice(manSays))
    print("Điều đó dẫn đến",random.choice(consequence))
    print("Thế giới nói",random.choice(worldSaid))
    print()
    input("Ấn Enter để chơi lại")
    print()