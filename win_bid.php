<?php
$max_bid=$_REQUEST['maxbid'];
$winner=$_REQUEST['winner'];
$time=$_REQUEST['time'];
$con = mysqli_connect('localhost', 'root', '', 'rh3');
$query_checker="SELECT * FROM max_bid WHERE time='$time'";
$result_checker=$con->query($query_checker);
$row_checker=mysqli_fetch_assoc($result_checker);
if($row_checker['max_bid']>$max_bid){
    $val=$row_checker['max_bid'];
    echo "$val";
}
else{
$query="UPDATE max_bid SET max_bid='$max_bid',winner='$winner' WHERE time='$time'";
$result=$con->query($query);
echo "true";
}

?>
