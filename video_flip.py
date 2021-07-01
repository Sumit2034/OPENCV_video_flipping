import cv2

vidcap = cv2.VideoCapture('number_plate_blur (2).avi')
while (vidcap.isOpened()):
  ret, frame = vidcap.read()

  cv2.imshow('original',frame)

  img2 = cv2.flip(frame, -1)
  cv2.imshow('Flipped video', img2)
  if cv2.waitKey(300) & 0xFF == ord('q'):
    break

vidcap.release()
cv2.destroyAllWindows()