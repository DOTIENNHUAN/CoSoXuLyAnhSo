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
    # Làm mờ trung bình
    average_blur = cv2.blur(image, (5, 5))

    # Hiển thị ảnh gốc và ảnh đã làm mờ
    cv2.imshow('Anh goc', image)
    cv2.imshow('Anh mo', average_blur)
    
    #Chọn thư mục lưu ảnh
    os.chdir(path1)
    #Đặt tên cho tên ảnh sau khi lưu
    filename = 'anh_mo.png'
    #Lưu ảnh
    cv2.imwrite(filename,average_blur)
    print('Luu thanh cong')
    
    # Chờ cho đến khi người dùng nhấn phím bất kỳ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
