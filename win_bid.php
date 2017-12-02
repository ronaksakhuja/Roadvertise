<?php
$max_bid=$_REQUEST['maxbid'];
$winner=$_REQUEST['winner'];
$time=$_REQUEST['time'];
$con = mysqli_connect('localhost', 'root', '', 'rh3');
$query="UPDATE max_bid SET max_bid='$max_bid',winner='$winner' WHERE time='$time'";
$result=$con->query($query);


?>
