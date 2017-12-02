<?php
  $con = mysqli_connect('localhost', 'root', '', 'rh3');
    $query="SELECT * FROM max_bid";
    $result=$con->query($query);
    $a=array();
    while($row=mysqli_fetch_assoc($result)){
        array_push($a,$row);
    }
    echo json_encode($a);

?>