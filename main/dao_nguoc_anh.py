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
    # Đảo ngược ảnh theo chiều ngang
    flipped_horizontal = cv2.flip(image, 1)

    # Đảo ngược ảnh theo chiều dọc
    flipped_vertical = cv2.flip(image, 0)

    # Hiển thị ảnh gốc và ảnh đã đảo ngược
    cv2.imshow('Anh goc', image)
    cv2.imshow('Anh dao nguoc ngang', flipped_horizontal)
    cv2.imshow('Anh dao nguoc doc', flipped_vertical)
    
    #Chọn thư mục lưu ảnh
    os.chdir(path1)
    #Đặt tên cho tên ảnh sau khi lưu
    filename1 = 'anh_dao_nguoc_ngang.png'
    filename2 = 'anh_dao_nguoc_doc.png'
    #Lưu ảnh
    cv2.imwrite(filename1, flipped_horizontal)
    cv2.imwrite(filename2, flipped_vertical)
    print('Luu thanh cong')

    # Chờ cho đến khi người dùng nhấn phím bất kỳ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
