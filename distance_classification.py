import cv2

def load_data():
    img1 = cv2.imread("Dr_Shashi_Tharoor.jpg")
    if img1 is None:
        return False
    
    img2 = cv2.imread("Plaksha_Faculty.jpg")
    if img2 is None:
        return False
    return True

print(load_data())