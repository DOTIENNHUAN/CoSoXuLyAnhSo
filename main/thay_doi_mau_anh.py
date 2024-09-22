import cv2
import os

#Đặt biến đường dẫn tới ảnh
path = r'N:\opencvApp\img\neymarJR.jpg'
path1 = r'N:\opencvApp\img'

# Đọc ảnh từ tệp
image = cv2.imread(path)

# Kiểm tra nếu ảnh được đọc thành công
if image is None:
    print("Không thể đọc ảnh.")
else:
    # Chuyển đổi ảnh sang grayscale (ảnh xám)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Hiển thị ảnh gốc và ảnh đã thay đổi màu sắc
    cv2.imshow('Anh goc', image)
    cv2.imshow('Anh xam', grayscale_image)
    
    #Chọn thư mục lưu ảnh
    os.chdir(path1)
    #Đặt tên cho tên ảnh sau khi lưu
    filename = 'anh_xam.png'
    #Lưu ảnh
    cv2.imwrite(filename,grayscale_image)
    print('Luu thanh cong')

    # Chờ cho đến khi người dùng nhấn phím bất kỳ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
