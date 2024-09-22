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
    # Xác định tỷ lệ thu nhỏ, 0.5 để thu nhỏ xuống một nửa
    scale_factor = 0.5

    # Tính kích thước mới của ảnh
    new_width = int(image.shape[1] * scale_factor)
    new_height = int(image.shape[0] * scale_factor)
    new_size = (new_width, new_height)

    # Thu nhỏ ảnh
    reduced_image = cv2.resize(image, new_size, interpolation=cv2.INTER_LINEAR)

    # Hiển thị ảnh gốc và ảnh đã thu nhỏ
    cv2.imshow('Anh goc', image)
    cv2.imshow('Anh thu nho', reduced_image)
    
    #Chọn thư mục lưu ảnh
    os.chdir(path1)
    #Đặt tên cho tên ảnh sau khi lưu
    filename = 'anh_thu_nho.png'
    #Lưu ảnh
    cv2.imwrite(filename,reduced_image)
    print('Luu thanh cong')

    # Chờ cho đến khi người dùng nhấn phím bất kỳ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
