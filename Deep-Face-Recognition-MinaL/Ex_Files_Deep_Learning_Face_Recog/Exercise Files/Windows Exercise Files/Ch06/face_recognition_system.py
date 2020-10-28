import face_recognition

# Load the known images
image1 = face_recognition.load_image_file("person_1.jpg")
image2 = face_recognition.load_image_file("person_2.jpg")
image3 = face_recognition.load_image_file("person_3.jpg")

# Get the face encoding of each person. This can fail if no one is found in the photo.
f_encoding = face_recognition.face_encodings(image1)[0]
f_encoding2 = face_recognition.face_encodings(image2)[0]
f_encoding3 = face_recognition.face_encodings(image3)[0]

# Create a list of all known face encodings
known_face_encodings = [
    f_encoding,
    f_encoding2,
    f_encoding3
]

# Load the image we want to check
unknown_img = face_recognition.load_image_file("unknown_1.jpg")

# Get face encodings for any people in the picture
unknown_img_fEncoding = face_recognition.face_encodings(unknown_img)

# There might be more than one person in the photo, so we need to loop over each face we found
for unknown_face_encoding in unknown_img_fEncoding:

    # Test if this unknown face encoding matches any of the three people we know
    results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)

    name = "Unknown"

    if results[0]:
        name = "Person 1"
    elif results[1]:
        name = "Person 2"
    elif results[2]:
        name = "Person 3"

    print(f"Found {name} in the photo!")
