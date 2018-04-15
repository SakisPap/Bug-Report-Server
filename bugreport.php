<?php
// the message
$msg = $_GET["bodyofmessage"];

// use wordwrap() if lines are longer than 70 characters
$msg = wordwrap($msg,70);

// send email
mail("receive.email@mail.com","BUG-REPORT",$msg);
?>
