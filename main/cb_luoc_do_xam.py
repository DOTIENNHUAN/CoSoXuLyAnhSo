import cv2
import os

#Đặt biến đường dẫn tới ảnh
path = r'N:\opencvApp\img\neymarJR.jpg'
path1 = r'N:\opencvApp\img'

# Đọc ảnh từ tệp dưới dạng ảnh xám (grayscale)
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Kiểm tra nếu ảnh được đọc thành công
if image is None:
    print("Không thể đọc ảnh.")
else:
    # Thực hiện cân bằng lược đồ xám (histogram equalization)
    equalized_image = cv2.equalizeHist(image)

    # Hiển thị ảnh gốc và ảnh sau khi cân bằng lược đồ xám
    cv2.imshow('Anh goc', image)
    cv2.imshow('Anh can bang luoc do xam', equalized_image)

    #Chọn thư mục lưu ảnh
    os.chdir(path1)
    #Đặt tên cho tên ảnh sau khi lưu
    filename = 'Anh_can_bang_luoc_do_xam.jpg'
    
    # Lưu ảnh sau khi cân bằng lược đồ
    cv2.imwrite(filename, equalized_image)

    # Chờ cho đến khi người dùng nhấn phím bất kỳ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
