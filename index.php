<?php

    $conn = pg_connect("host=18.191.13.17 port=5432 dbname=poker-elephant user=remote password=PokerEleph4nt!");
    if($conn){
        // echo $conn;
        echo 'connected';
    }else{
        // echo $conn;
        echo 'not connected';
    }
   
?>
<html>
  <h1>-- html confirmation of that php stuff</h1>
</html>
