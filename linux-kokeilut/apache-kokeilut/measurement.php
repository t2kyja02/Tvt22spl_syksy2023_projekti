<?php
$servername = "localhost";
$username = "dbaccess_rw";
$password = "fasdjkf2389vw2c3k234vk2f3";
$dbname = "measurements";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
        }

$sql = "SELECT timestamp, sensor, temperature, location FROM rawdata ORDER BY id DESC LIMIT 5";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
   while($row = $result->fetch_assoc()) {
      echo "Time: " . $row["timestamp"] . " - Sensor: " . $row["sensor"] . " - Temp: " . $row["temperature"] . " - Location: " . $row["location"]  ."<br>" ;
   }
}

$conn->close();
?>

