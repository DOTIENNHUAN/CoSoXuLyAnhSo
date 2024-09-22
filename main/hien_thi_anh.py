#Khai báo thư viện
import cv2 
import os

#Đặt biến đường dẫn tới ảnh
path = r'N:\opencvApp\img\neymarJR.jpg'
path1 = r'N:\opencvApp\img'

#Đọc ảnh 
img = cv2.imread(path)   #Ảnh hiện thị mặc định là ảnh màu

#Hiển thị ảnh
cv2.imshow('Anh hien thi',img)

#Chọn thư mục lưu ảnh
os.chdir(path1)
#Đặt tên cho tên ảnh sau khi lưu
filename = 'anh_moi.png'
#Lưu ảnh
cv2.imwrite(filename,img)
print('Luu thanh cong')

#Thời gian hiển thị ảnh
cv2.waitKey(5000)   #5s
    
