<?php
if ($_FILES['image']['error'] === UPLOAD_ERR_OK) {
    $uploadDir = 'uploads/';
    $filename = uniqid() . '_' . basename($_FILES['image']['name']); // Generate unique filename
    $uploadFile = $uploadDir . $filename;

    if (move_uploaded_file($_FILES['image']['tmp_name'], $uploadFile)) {
        // File uploaded successfully
        $image_url = 'http://' . $_SERVER['HTTP_HOST'] . '/' . $uploadFile; // Adjust URL as needed

        // Connect to the database (replace these values with your actual database credentials)
        $servername = "89.46.111.212";
        $username = "Sql1782534";
        $password = "?Tre432Gre?";
        $dbname = "Sql1782534_1";

        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Prepare SQL statement
        $sql = "INSERT INTO ImageDescriptions (image_name, image_url, created_at, updated_at) 
                VALUES (?, ?, NOW(), NOW())";

        // Prepare and bind parameters
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("ss", $filename, $image_url);

        // Execute the statement
        if ($stmt->execute()) {
            // Record inserted successfully
            http_response_code(200);
        } else {
            // Failed to insert record
            http_response_code(500);
        }

        // Close statement and connection
        $stmt->close();
        $conn->close();
    } else {
        // Failed to move uploaded file
        http_response_code(500);
    }
} else {
    // Error uploading file
    http_response_code(400);
}
?>
