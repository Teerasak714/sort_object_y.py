obj_detected = {'bottle': [110, 30], 'glass': [60, 35], 'book': [310, 23], 'phone': [90, 33], 'pen': [155, 100], 'mouse': [200, 45], 'remote': [298, 165], 'fan': [300, 36]}

# เรียงลำดับตามแกน y จากน้อยไปมาก
sorted_obj_detected = sorted(obj_detected.items(), key=lambda x: x[1][1])

# แสดงผลลัพธ์
for obj in sorted_obj_detected:
    print(obj[0], obj[1])
