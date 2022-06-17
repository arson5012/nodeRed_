# Node-Red + rp2040 + Teachable Machine Streaming
노드레드 안에서 구동되는 머신 러닝 객체 검출과 센서 값
<!-------------------------------------------------------------Part 1------------------------------------------------------------------------------------------>

## 프로젝트 구동 파트
* **비디오 출력 부**
  A. 헤드폰을 쓴 사진(500장)과 쓰지 않은 사진(500장) 촬영 후 tensorflow를 사용하여 학습하고  
     딥 러닝을 쉽게 할 수 있는 파이썬 라이브러리인 케라스(Keras) 파일로 변환하여 객체 검출 한다.
  B. 다음과 같은 코드로 헤드셋 유무를 판별함
     ```python
        if (prediction[0,0] < prediction[0,1]):
             print("헤드폰 없음")
       

        else:
             print('헤드폰 있음')
     ```
  C. 다음과 같은 코드로 base64로 변환함
     ```python 
        def encode_img(image1):
           success, encoded_img =cv.imencode('.png',image1)
           if success:
               return base64.b64encode(encoded_img)
           return ''
    
        encoded_img=encode_img(image1)
        decoded_img=base64.b64decode(encoded_img)
     ```
* **노드 레드(Node-Red)부분**  
    ![노드레드](./img/노드레드.jpg)  
    A. 다음과 같이 노드를 구성하였고 관련된 Node_import 정보는 [이곳](./Node-Red_import/import_node.md)을 참고 바람    
* **노드 레드 대시보드(Node-Red Dashboard)부분**  
    ![대시보드](./img/대시보드.jpg)  
    A. 대시보드는 크게 ***객체 검출**과 ***움직임 차트** 부분으로 나누어져 있음  

    B. 객체 검출 부분에는 수신 받은 머신 러닝 객체 검출 ***영상을 송출***하고 객체 검출 결과를 ***텍스트***로 출력함  

    C. 움직임 차트 부분에는 rp2040부터 받은 3축(X,Y,Z) 가속도와 자이로 센서를 받아서 ***3차원 차트***로 출력하며  
       움직임이 감지될 경우 LED로 움직일 경우 ***초록색LED***를 움직이지 않을 경우 ***빨간색LED***로 한눈에 알아 볼 수 있도록 ***시각화 함***
       
    D. 두개의 ***버튼***을 구성하고 자바스크립트로 개인 네이버 블로그와 깃허브 주소를 연결하여 ***클릭 시 새창 이벤트***로 열릴 수 있게 함
    
    E. Dashboard ***CSS***를 통하여 기존의 딱딱한 노드레드 UI를 깔끔하고 유려하게 바꾸고 사용자 친화적으로 바꿈
* **Rp2040(MicroPyhton)부분**
 
 * **MQTT부**  
