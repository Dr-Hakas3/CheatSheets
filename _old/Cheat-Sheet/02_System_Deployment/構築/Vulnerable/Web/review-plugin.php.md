<?php
/*
Plugin Name: Review Manager
Description: 商品レビュー投稿と一覧表示（画像投稿付き）
Version: 1.2
Author: SecurityLearner
*/

function review_menu_page() {
    add_menu_page('レビュー投稿', 'レビュー管理', 'manage_options', 'review-manager', 'review_render_page');
}
add_action('admin_menu', 'review_menu_page');

function review_render_page() {
    $data_file = plugin_dir_path(__FILE__) . 'reviews.txt';
    $upload_dir = plugin_dir_path(__FILE__) . 'uploads/';
    if (!is_dir($upload_dir)) mkdir($upload_dir);

    $products = ['Smartphone', 'Laptop', 'Camera', 'Tablet', 'Headphones'];

    // 削除処理
    if (isset($_GET['delete'])) {
        $index = intval($_GET['delete']);
        $lines = file($data_file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
        if (isset($lines[$index])) {
            $entry = explode('|', $lines[$index]);
            if (!empty($entry[5]) && file_exists($upload_dir . $entry[5])) {
                unlink($upload_dir . $entry[5]); // 画像も削除
            }
            unset($lines[$index]);
            file_put_contents($data_file, implode("\n", $lines) . "\n");
        }
        wp_redirect(admin_url('admin.php?page=review-manager'));
        exit;
    }

    // 投稿処理
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['comment'])) {
        $product = $_POST['product'];
        $author = $_POST['author'];
        $rating = $_POST['rating'];
        $comment = $_POST['comment'];
        $date = date('Y-m-d H:i:s');

        $image_filename = '';
        if (isset($_FILES['image']) && $_FILES['image']['error'] === 0) {
            $image_filename = time() . '_' . basename($_FILES['image']['name']);
            move_uploaded_file($_FILES['image']['tmp_name'], $upload_dir . $image_filename);
        }

        $entry = "$date|$product|$author|$rating|$comment|$image_filename\n";
        file_put_contents($data_file, $entry, FILE_APPEND);

        wp_redirect(admin_url('admin.php?page=review-manager&posted=1'));
        exit;
    }

    if (isset($_GET['posted'])) {
        echo "<p style='color:green;'>レビューが投稿されました。</p>";
    }

    // 投稿フォーム
    echo "<h2>レビュー投稿</h2>";
    echo '<form method="POST" enctype="multipart/form-data">';
    echo '商品名: <select name="product">';
    foreach ($products as $p) {
        echo "<option value=\"$p\">$p</option>";
    }
    echo '</select><br><br>';
    echo '投稿者: <input type="text" name="author"><br><br>';
    echo '星評価 (1〜5): <input type="number" name="rating" min="1" max="5"><br><br>';
    echo 'コメント:<br><textarea name="comment" rows="4" cols="50"></textarea><br><br>';
    echo '画像（任意）: <input type="file" name="image"><br><br>';
    echo '<button type="submit">投稿</button>';
    echo '</form>';

    // 一覧表示
    echo "<hr><h2>レビュー一覧</h2>";
    if (file_exists($data_file)) {
        $lines = file($data_file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
        foreach ($lines as $i => $line) {
            list($date, $product, $author, $rating, $comment, $image_filename) = explode('|', $line);
            echo "<div style='border:1px solid #ccc; margin:10px; padding:10px;'>";
            echo "<strong>日時:</strong> $date<br>";
            echo "<strong>商品:</strong> $product<br>";
            echo "<strong>投稿者:</strong> $author<br>";
            echo "<strong>評価:</strong> $rating / 5<br>";
            echo "<strong>コメント:</strong><br>$comment<br>";
            if (!empty($image_filename) && file_exists($upload_dir . $image_filename)) {
                $image_url = plugins_url('uploads/' . $image_filename, __FILE__);
                echo "<br><img src=\"$image_url\" style='max-width:300px;'><br>";
            }
            echo "<a href='" . admin_url('admin.php?page=review-manager&delete=' . $i) . "' style='color:red;'>[削除]</a>";
            echo "</div>";
        }
    }
}
