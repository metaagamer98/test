<?php
if (!isset($_GET["token"])) {
    die("no");
}
if (!isset($_GET["ip"])) {
    die("no");
}
$token = $_GET["token"];
$ip = $_GET["ip"];
$db = new PDO('mysql:host=localhost;dbname=tokens;', 'root', '');
$query = $db->prepare("SELECT * FROM `tokens` WHERE `token` = ? AND `ip` = ?");
$query->execute(array($token, $ip));
$res = $query->fetchAll();
if (count($res) > 0) {
    die("yes");
}
die("no");