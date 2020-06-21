import random
exitChoice = "Không có gì"
while exitChoice !="Thoát":
    alienDictionary={"chúng tôi":"vorag","tới":"thang","trong":"zong","hòa bình":"argh","xin chào":"kodar","có thể":"znak","tôi":"az","mượn":"liftit","một vài":"zum","tên lửa":"upgoman","nhiên liệu":"kakboom","làm ơn":"selpin","đừng":"baaaaaarn","bắn":"flabil","chào mừng":"unkip","của chúng tôi":"mandig","mới":"brang","người ngoài hành tinh":"marangin","xâm chiếm":"bap"}
    vietnamesePhrase=input("Xin hãy điền một từ hoặc một cụm từ tiếng Việt cần dịch:")
    vietnameseWords=vietnamesePhrase.lower().split()
    alienWords=[]
    for word in vietnameseWords:
        if word in alienDictionary:
            alienWords.append(alienDictionary[word])
        else:
            alienWords.append(word)
    print("Tiếng ngoài hành tinh gọi là:"," ".join(alienWords))
    exitChoice = input("Ấn Enter để chơi lại, hoặc gõ Thoát để đóng chương trính.")