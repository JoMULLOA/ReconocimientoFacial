from deepface import DeepFace

# Función para reconocer rostros con DeepFace
def recognize_face_with_deepface(test_image_path, known_faces_path, threshold=0.6):
    # Buscar coincidencias en la base de datos
    results = DeepFace.find(
        img_path=test_image_path,
        db_path=known_faces_path,
        model_name="Facenet",
        enforce_detection=False  # Evitar errores si no detecta rostro
    )
    
    # Verificar si los resultados son una lista de DataFrames
    if isinstance(results, list):
        result_df = results[0]  # Tomar el primer DataFrame de la lista
    else:
        result_df = results

    # Mostrar columnas disponibles para depuración
    print("Columnas disponibles en el DataFrame:", result_df.columns)

    # Verificar si hay coincidencias en el DataFrame
    if not result_df.empty:
        match = result_df.iloc[0]  # Obtener la mejor coincidencia

        # Adaptar a la columna de similitud presente
        similarity_column = [col for col in result_df.columns if "cosine" in col.lower()]
        if similarity_column:
            similarity = match[similarity_column[0]]  # Usar la columna encontrada
        else:
            similarity = 0.0  # Si no hay columna de similitud, usar 0

        return match['identity'], similarity
    else:
        return None, 0.0

# Imagen de prueba
test_image_path = r"C:\Users\manri\OneDrive\Escritorio\CimF\imgtest.jpg"
known_faces_path = r"C:\Users\manri\OneDrive\Escritorio\CimF\know_faces"

# Reconocer el rostro
predicted_name, similarity_score = recognize_face_with_deepface(test_image_path, known_faces_path)

if predicted_name:
    print(f"El rostro pertenece a: {predicted_name} (Similitud: {similarity_score:.2f})")
else:
    print("No se encontró una coincidencia en la base de datos.")
from deepface import DeepFace

# Función para reconocer rostros con DeepFace
def recognize_face_with_deepface(test_image_path, known_faces_path, threshold=0.6):
    # Buscar coincidencias en la base de datos
    results = DeepFace.find(
        img_path=test_image_path,
        db_path=known_faces_path,
        model_name="Facenet",
        enforce_detection=False  # Evitar errores si no detecta rostro
    )
    
    # Verificar si los resultados son una lista de DataFrames
    if isinstance(results, list):
        result_df = results[0]  # Tomar el primer DataFrame de la lista
    else:
        result_df = results

    # Mostrar columnas disponibles para depuración
    print("Columnas disponibles en el DataFrame:", result_df.columns)

    # Verificar si hay coincidencias en el DataFrame
    if not result_df.empty:
        match = result_df.iloc[0]  # Obtener la mejor coincidencia

        # Adaptar a la columna de similitud presente
        similarity_column = [col for col in result_df.columns if "cosine" in col.lower()]
        if similarity_column:
            similarity = match[similarity_column[0]]  # Usar la columna encontrada
        else:
            similarity = 0.0  # Si no hay columna de similitud, usar 0

        return match['identity'], similarity
    else:
        return None, 0.0

# Imagen de prueba
test_image_path = r"C:\Users\manri\OneDrive\Escritorio\CimF\img2.jpg"
known_faces_path = r"C:\Users\manri\OneDrive\Escritorio\CimF\know_faces"

# Reconocer el rostro
predicted_name, similarity_score = recognize_face_with_deepface(test_image_path, known_faces_path)

if predicted_name:
    print(f"El rostro pertenece a: {predicted_name} (Similitud: {similarity_score:.2f})")
else:
    print("No se encontró una coincidencia en la base de datos.")