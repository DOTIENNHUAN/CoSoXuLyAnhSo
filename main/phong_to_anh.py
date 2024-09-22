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
    # Xác định tỷ lệ phóng to, 2.0 để phóng to gấp đôi
    scale_factor = 2.0

    # Tính kích thước mới của ảnh
    new_width = int(image.shape[1] * scale_factor)
    new_height = int(image.shape[0] * scale_factor)
    new_size = (new_width, new_height)

    # Phóng to ảnh
    enlarged_image = cv2.resize(image, new_size, interpolation=cv2.INTER_LINEAR)

    # Hiển thị ảnh gốc và ảnh đã phóng to
    cv2.imshow('Anh goc', image)
    cv2.imshow('Anh phong to', enlarged_image)
    
    #Chọn thư mục lưu ảnh
    os.chdir(path1)
    #Đặt tên cho tên ảnh sau khi lưu
    filename = 'anh_phong_to.png'
    #Lưu ảnh
    cv2.imwrite(filename,enlarged_image)
    print('Luu thanh cong')

    # Chờ cho đến khi người dùng nhấn phím bất kỳ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
