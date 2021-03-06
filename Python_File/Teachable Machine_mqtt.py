from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2 as cv
import base64
import paho.mqtt.client as mqtt


mqtt=mqtt.Client("Client_ID")
mqtt.connect("IP",1883)
mqtt.loop(2)



# Load the model
model = load_model('File_Path')

clesses =['Headphone','Non']
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.

#knn = cv2.ml.KNearest_create()
#knn.train(angle, cv2.ml.ROW_SAMPLE, label)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

size = (224, 224)

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("카메라 없음")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)
    # if frame is read correctly ret is True
    if not ret:
        print("카메라를 찾을 수 없습니다 ... 종료합니다")
        break

    # Our operations on the frame come here
    image1 = cv.resize(frame, size, interpolation=cv.INTER_AREA) 
    image_array = np.asarray(image1)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    def encode_img(image1):
        success, encoded_img =cv.imencode('.png',image1)
        if success:
            return base64.b64encode(encoded_img)
        return ''
    
    encoded_img=encode_img(image1)
    decoded_img=base64.b64decode(encoded_img)
    mqtt.publish("test2",decoded_img,0,False)
    
       
    prediction = model.predict(data)
    idx=np.argmax(prediction)
    
    
    #print(prediction)
    if (prediction[0,0] < prediction[0,1]):
        cv.putText(image1, 'Non', (0, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
        print("헤드폰 없음")
        mqtt.publish("test1","헤드폰 없음")

    else:
        cv.putText(image1, 'Headphone', (0, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
        print('헤드폰 있음')
        mqtt.publish("test1","헤드폰 있음")

    
    #cv.putText(image1, text=classes[idx], org=(0, 25), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 255), thickness=2)
    

    # Display the resulting frameq
    cv.imshow('1701298', image1)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

